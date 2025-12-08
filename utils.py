from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv("SONDOS_API_KEY")
ASSISTANT_ID = os.getenv("SONDOS_ASSISTANT_ID")

def make_call(
    phone_number: str,
    customer_name: str,
    email: str,
):
    """
    POST /make_call using API key & assistant ID from .env
    """
    url = "https://app.sondos-ai.com/api/user/make_call"

    payload = {
        "phone_number": phone_number,
        "assistant_id": int(ASSISTANT_ID),
        "variables": {
            "customer_name": customer_name,
            "email": email
        }
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

