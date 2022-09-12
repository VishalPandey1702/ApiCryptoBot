from typing import final
import requests
import secrets
api_key = "{}".format(secrets.secrets()["api_key"])
def makeDictionary(symbol,namePrice):
    finalData = {}
    for i in range(0,len(symbol)):
        finalData.update({symbol[i]:namePrice[i]})
    return finalData
def dataFetch():
    symbol = []
    namePrice = []
    head = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '{}'.format(api_key)
    }
    param = {
        'start' : '1',
        'limit' : '500',
        'convert' : 'USD'
    }
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=head, params=param).json()
    # Fetching Crypto Symbol
    tempString = ""
    for i in data["data"]:
        for j in i["symbol"]:
           tempString += j
        symbol.append(tempString)
        tempString = ""
    tempList = []
    for i in range(0,int(param["limit"])):
        tempList.append(data["data"][i]["name"])
        tempList.append("{}".format(data["data"][i]["quote"]["USD"]["price"]))
        namePrice.append(tempList)
        tempList=[]
    return makeDictionary(symbol,namePrice)
