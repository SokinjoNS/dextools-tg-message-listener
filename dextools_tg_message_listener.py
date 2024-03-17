import requests
import json
from telegram_alerts import handle_and_send_message

def load_telegram_credentials():
    with open('credentials_telegram.json') as f:
        credentials = json.load(f)
    return credentials

def get_token_address_from_dextools(url, dextools_api_key):
    try:
        # Extracting the pair address from the URL
        pair_address = url.split("pair-explorer/")[-1].split("?")[0]
    except Exception as e:
        print(f"Error extracting pair address from Dextools URL: {e}")
        return None
    
    # Making the API call to Dextools
    api_url = "https://api.dextools.io/v1/pair"
    headers = {"X-API-Key": dextools_api_key}
    params = {"chain": "ether", "address": pair_address}
    
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "token" in data["data"] and "address" in data["data"]["token"]:
            return data["data"]["token"]["address"]
    return None

def handle_dextools_message(message):
    credentials = load_telegram_credentials()
    dextools_api_key = credentials['dextools_api_key']
    if "dextools.io/app/en/ether/pair-explorer/" in message:
        token_address = get_token_address_from_dextools(message, dextools_api_key)
        if token_address:
            # Structure the details dictionary correctly for handle_and_send_message
            details = {
                'token_address': token_address  # Key change to align with handle_and_send_message expectations
            }
            # Send message using the 'dextools' source
            handle_and_send_message('dextools', details, credentials)
        else:
            print("Failed to fetch token address from Dextools URL.")
