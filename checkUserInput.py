import updateOffset
import requests
import secrets
def checkUserInput(offset):
    params={
        "offset" : offset
    }
    data = requests.get("https://api.telegram.org/bot{}/getUpdates".format(secrets.secrets()["bot_token"]),params=params).json()
    return data["result"][0]["message"]["text"]
