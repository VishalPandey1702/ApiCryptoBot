import datafetch # Data
import updateOffset # LatestOffset
import requests
import check_message # verifies command
import checkUserInput # Fetch User Latest Input
import secrets
def sendPostData(MessageData,data):    
    params={
        "chat_id" : "{}".format(secrets.secrets()["chat_id"]),
        "text" : "{}".format(data[MessageData][0]+" : "+"{:.2f}".format(float(data[MessageData][1]))+"USD")
    }
    requests.get("https://api.telegram.org/bot{}/sendMessage".format(secrets.secrets()["bot_token"]),params=params)
def main():
    data = datafetch.dataFetch()
    offset = updateOffset.initialOffset(0)
    userInput = checkUserInput.checkUserInput(offset)
    checkMessage = check_message.checkUserInput(data,userInput) # False / ETH,BTC (/get ETH) (/get BTC)
    offset2 = offset
    if checkMessage:
        sendPostData(checkMessage,data)
        offset2+=1
    while True:
        offset = updateOffset.initialOffset(0)
        if offset == offset2:
            main()
main()
