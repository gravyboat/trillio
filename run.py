#!/usr/bin/python

from flask import Flask, request, redirect, session
import twilio.twiml
from smsProcessor import smsProcessFlow

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = #your secret key goes here 

#put some callers in here
callers = { "+11231231234": "User" }



@app.route("/", methods=['GET', 'POST'])
def TrillioData():
    """Respond to SMS and provide information about what's going on over at Trillio."""

    fromNumber = request.values.get('From')
    trelloInfoRequest = request.values.get('Body').lower()
    if fromNumber in callers:
        name = callers[fromNumber]
    else:
        name = "User"
    if trelloInfoRequest == 'board':
        trelloBoard = smsProcess.findBoardName()
        message = "".join([name, ", the board name is ", str(trelloBoard), "."])
    elif trelloInfoRequest == 'cards':
        trelloCards = smsProcess.findTrelloCards()
        message = "".join([name, ", the cards are ", str(trelloCards), "."])
    elif trelloInfoRequest == 'status':
        trelloStatus = smsProcess.findCardStatus()
        message = "".join([name, ", the status is", str(trelloStatus), "."])
    else:
        message = "".join([name, ", your options are board, cards, or status. Please use those options."])
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)


if __name__ == "__main__":
    smsProcess = smsProcessFlow()
    app.run(host="0.0.0.0", debug=True)

