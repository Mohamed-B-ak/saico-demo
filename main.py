from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Serve /static for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# --------------------------
# 1️⃣ Webhook Receiver & Viewer
# --------------------------
latest_webhook = {"data": "No webhook received yet."}


@app.post("/webhook")
async def receive_webhook(payload: dict):
    """
    Webhook endpoint: receives JSON and stores last payload in memory.
    """
    global latest_webhook
    latest_webhook = payload
    return {"status": "received", "data": latest_webhook}


import json

@app.get("/", response_class=HTMLResponse)
async def view_webhook(request: Request):
    """
    First page: displays the last received webhook with real Unicode (Arabic, Chinese...)
    """
    pretty_webhook = json.dumps(latest_webhook, indent=2, ensure_ascii=False)
    return templates.TemplateResponse(
        "webhook_view.html",
        {"request": request, "webhook_json": pretty_webhook},
    )


# --------------------------
# 2️⃣ Sondos AI – API Actions Console
# --------------------------

BASE_URL = "https://app.sondos-ai.com/api/user"


def sondos_request(method: str, endpoint: str, api_key: str, **kwargs):
    """
    Helper to call Sondos API safely and return a clean JSON response.
    """
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {api_key}"

    try:
        resp = requests.request(
            method=method,
            url=f"{BASE_URL}{endpoint}",
            headers=headers,
            **kwargs,
        )
    except requests.RequestException as e:
        return {
            "ok": False,
            "error": "request_exception",
            "details": str(e),
        }

    try:
        data = resp.json()
    except ValueError:
        data = {"raw_text": resp.text}

    return {
        "ok": resp.ok,
        "status_code": resp.status_code,
        "data": data,
    }


@app.get("/api-actions", response_class=HTMLResponse)
async def api_actions_page(request: Request):
    """
    Second page: UI for all Sondos actions.
    """
    return templates.TemplateResponse("api_actions.html", {"request": request})


# ---------- A. Assistants ----------

@app.post("/actions/assistants/get")
async def get_assistants(api_key: str = Form(...)):
    """
    GET /assistants/get
    """
    return sondos_request("GET", "/assistants/get", api_key)


@app.post("/actions/assistants/create")
async def create_assistant(
    api_key: str = Form(...),
    assistant_name: str = Form(...),
    voice_id: int = Form(...),
    language: str = Form(...),
    llm_model: str = Form(...),
    calls_direction: str = Form("outbound"),
    engine_type: str = Form("sondos"),
    timezone: str = Form("Asia/Riyadh"),
    initial_message: str = Form(...),
    system_prompt: str = Form(...),
    phone_number_id: int = Form(...),
    webhook_url: str = Form(""),
):
    """
    POST /assistant
    SIMPLE MODE:
    - Only the main fields come from the form.
    - The rest uses reasonable defaults.
    """
    payload = {
        "assistant_name": assistant_name,
        "voice_id": voice_id,
        "language": language,
        "llm_model": llm_model,
        "calls_direction": calls_direction,
        "engine_type": engine_type,
        "timezone": timezone,
        "initial_message": initial_message,
        "system_prompt": system_prompt,
        "phone_number_id": phone_number_id,
        "endpoint_type": "sip",
        "endpoint_sensitivity": 5,
        "interrupt_sensitivity": 5,
        "ambient_sound_volume": 0,
        "post_call_evaluation": True,
        "send_webhook_only_on_completed": True,
        "include_recording_in_webhook": True,
        "is_webhook_active": bool(webhook_url),
        "webhook_url": webhook_url,
        "use_min_interrupt_words": True,
        "min_interrupt_words": 2,
        "variables": {},
        "post_call_schema": [],
        "llm_temperature": 0.3,
        "voice_stability": 0.7,
        "voice_similarity": 0.7,
        "speech_speed": 1.0,
        "allow_interruptions": True,
        "filler_audios": True,
        "re_engagement_interval": 0,
        "max_call_duration": 900,
        "max_silence_duration": 30,
        "end_call_on_voicemail": True,
        "noise_cancellation": True,
        "record_call": True,
        "who_speaks_first": "assistant",
    }

    return sondos_request(
        "POST",
        "/assistant",
        api_key,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


@app.post("/actions/assistants/delete")
async def delete_assistant(
    api_key: str = Form(...),
    assistant_id: int = Form(...),
):
    """
    DELETE /assistant/{id}
    """
    endpoint = f"/assistant/{assistant_id}"
    return sondos_request("DELETE", endpoint, api_key)


@app.post("/actions/assistants/languages")
async def get_languages(api_key: str = Form(...)):
    """
    GET /assistants/languages
    """
    return sondos_request("GET", "/assistants/languages", api_key)


# ---------- B. Calls ----------

@app.post("/actions/calls")
async def get_calls(api_key: str = Form(...)):
    """
    GET /calls
    """
    return sondos_request("GET", "/calls", api_key)


@app.post("/actions/make-call")
async def make_call(
    api_key: str = Form(...),
    phone_number: str = Form(...),
    assistant_id: int = Form(...),
    customer_name: str = Form(""),
    email: str = Form(""),
):
    """
    POST /make_call
    """
    variables = {}
    if customer_name:
        variables["customer_name"] = customer_name
    if email:
        variables["email"] = email

    payload = {
        "phone_number": phone_number,
        "assistant_id": assistant_id,
        "variables": variables,
    }

    return sondos_request(
        "POST",
        "/make_call",
        api_key,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


# ---------- C. Leads ----------

@app.post("/actions/leads")
async def get_leads(api_key: str = Form(...)):
    """
    GET /leads
    """
    return sondos_request("GET", "/leads", api_key)
