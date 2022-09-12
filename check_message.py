def checkUserInput(data,userInput):
    finalAnswer = ""
    for cryptoSymbol in data:
        if userInput == "/get " + cryptoSymbol:
            finalAnswer = cryptoSymbol
    if finalAnswer:
        return finalAnswer
    else:
        return False

