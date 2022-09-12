import requests
import secrets
bot_token = "{}".format(secrets.secrets()["bot_token"])
def updateOffset(update_id):
    parameters={
        "offset" : update_id
    }
    res=requests.get("https://api.telegram.org/bot{}/getUpdates".format(bot_token),params=parameters).json()
    if res["result"]:
        return (res["result"][-1]["update_id"])
def initialOffset(offset):
    offset = updateOffset(offset)
    return offset