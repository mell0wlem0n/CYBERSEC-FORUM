import json
import requests
from flask_babel import _
from flask import current_app


def detect_language(text):
    # Use the Translator detect function
    path = "/detect"
    url = current_app.config["ENDPOINT"] + path
    # Build the request
    params = {"api-version": "3.0"}
    headers = {
        "Ocp-Apim-Subscription-Key": current_app.config["MS_TRANSLATOR_KEY"],
        "Ocp-Apim-Subscription-Region": current_app.config["REGION"],
        "Content-type": "application/json",
    }
    body = [{"text": text}]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get language
    language = response[0]["language"]
    # Return the language
    return language


def translate(text, source_language, target_language):
    # Use the Translator translate function
    url = current_app.config["ENDPOINT"] + "/translate"
    # Build the request
    params = {"api-version": "3.0", "from": source_language, "to": target_language}
    headers = {
        "Ocp-Apim-Subscription-Key": current_app.config["MS_TRANSLATOR_KEY"],
        "Ocp-Apim-Subscription-Region": current_app.config["REGION"],
        "Content-type": "application/json",
    }
    body = [{"text": text}]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get translation
    translation = response[0]["translations"][0]["text"]

    # Return the translation
    return translation
