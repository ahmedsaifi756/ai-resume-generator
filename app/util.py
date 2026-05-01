import json

def clean_json_response(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return text


def parse_json_safe(text: str):
    try:
        return json.loads(text), None
    except Exception as e:
        return None, str(e)