import requests

url = "https://app.sondos-ai.com/api/user/assistants/get"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())

#-----------------------------

import requests

url = "https://app.sondos-ai.com/api/user/assistants/outbound"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())


#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistant"

payload = {
    "assistant_name": "<string>",
    "voice_id": 123,
    "language": "<string>",
    "llm_model": "<string>",
    "calls_direction": "<string>",
    "engine_type": "<string>",
    "timezone": "<string>",
    "initial_message": "<string>",
    "system_prompt": "<string>",
    "phone_number_id": 123,
    "endpoint_type": "<string>",
    "endpoint_sensitivity": 123,
    "interrupt_sensitivity": 123,
    "ambient_sound_volume": 123,
    "post_call_evaluation": True,
    "send_webhook_only_on_completed": True,
    "include_recording_in_webhook": True,
    "is_webhook_active": True,
    "webhook_url": "<string>",
    "use_min_interrupt_words": True,
    "min_interrupt_words": 123,
    "variables": {},
    "post_call_schema": [
        {
            "post_call_schema[].name": "<string>",
            "post_call_schema[].type": "<string>",
            "post_call_schema[].description": "<string>"
        }
    ],
    "end_call_tool.description": "<string>",
    "llm_temperature": 123,
    "voice_stability": 123,
    "voice_similarity": 123,
    "speech_speed": 123,
    "allow_interruptions": True,
    "filler_audios": True,
    "re_engagement_interval": 123,
    "max_call_duration": 123,
    "max_silence_duration": 123,
    "end_call_on_voicemail": True,
    "noise_cancellation": True,
    "record_call": True,
    "who_speaks_first": "<string>"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistant/{id}"

payload = {
    "assistant_name": "<string>",
    "voice_id": 123,
    "language": "<string>",
    "llm_model": "<string>",
    "calls_direction": "<string>",
    "engine_type": "<string>",
    "timezone": "<string>",
    "initial_message": "<string>",
    "system_prompt": "<string>",
    "phone_number_id": 123,
    "endpoint_type": "<string>",
    "endpoint_sensitivity": 123,
    "interrupt_sensitivity": 123,
    "ambient_sound_volume": 123,
    "post_call_evaluation": True,
    "send_webhook_only_on_completed": True,
    "include_recording_in_webhook": True,
    "is_webhook_active": True,
    "webhook_url": "<string>",
    "use_min_interrupt_words": True,
    "min_interrupt_words": 123,
    "variables": {},
    "post_call_schema": [
        {
            "post_call_schema[].name": "<string>",
            "post_call_schema[].type": "<string>",
            "post_call_schema[].description": "<string>"
        }
    ],
    "end_call_tool.description": "<string>",
    "llm_temperature": 123,
    "voice_stability": 123,
    "voice_similarity": 123,
    "speech_speed": 123,
    "allow_interruptions": True,
    "filler_audios": True,
    "re_engagement_interval": 123,
    "max_call_duration": 123,
    "max_silence_duration": 123,
    "end_call_on_voicemail": True,
    "noise_cancellation": True,
    "record_call": True,
    "who_speaks_first": "<string>"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistant/{id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/enable-inbound-webhook"

payload = {
    "assistant_id": 123,
    "webhook_url": "<string>"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/disable-inbound-webhook"

payload = { "assistant_id": 123 }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/disable-webhook"

payload = { "assistant_id": 123 }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/languages"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/languages"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/models"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/assistants/models"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/calls"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/make_call"

payload = {
    "phone_number": "<string>",
    "assistant_id": 123,
    "variables": {
        "customer_name": "<string>",
        "email": "<string>"
    }
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/calls/{call}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/leads"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/lead"

payload = {
    "phone_number": "<string>",
    "campaign_id": 123,
    "variables": {
        "customer_name": "<string>",
        "email": "<string>"
    },
    "allow_dupplicate": True,
    "secondary_contacts": [
        {
            "phone_number": "<string>",
            "variables": {
                "customer_name": "<string>",
                "email": "<string>"
            }
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/leads/{id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/campaigns"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
#-----------------------------
import requests

url = "https://app.sondos-ai.com/api/user/campaigns/update-status"

payload = {
    "campaign_id": 123,
    "action": "<string>"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
#-----------------------------

import requests

url = "https://app.sondos-ai.com/api/user/sms"

payload = {
    "from": 123,
    "to": "<string>",
    "body": "<string>"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
