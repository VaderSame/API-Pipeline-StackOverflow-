import requests
from flask import current_app

def fetch_stackexchange_questions():
    url = current_app.config["STACKEXCHANGE_API_URL"]
    params = {"order": "desc", "sort": "activity", "site": "stackoverflow"}
    response = requests.get(url, params=params)
    response.raise_for_status()  # fail fast if API call breaks
    return response.json().get("items", [])