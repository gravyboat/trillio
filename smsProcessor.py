#!/usr/bin/python

import urllib2
import json
import argparse

#Your id and other ID info goes here, this should be available if you enabled things at Trello.
boardID = "your_board_id"
devKey = "your_dev_key"
authToken = "your_auth_token"

class smsProcessFlow(object):
    def __init__(self,
                boardID = boardID,
                devKey = devKey,
                authToken = authToken):
        self.boardID = boardID
        self.devKey = devKey
        self.authToken = authToken
    def findBoardName(self):
        # Here we will display all cards associated with a project just titles, and their colum
        trelloBoardUrl = "https://api.trello.com/1/board/{0}?key={1}&token={2}".format(
                                                                        self.boardID,
                                                                        self.devKey,
                                                                        self.authToken)
        trelloBoardPage = urllib2.Request(trelloBoardUrl)
        trelloBoardOpener = urllib2.build_opener()
        trelloBoardOpened = trelloBoardOpener.open(trelloBoardPage)
        trelloBoardJson = json.load(trelloBoardOpened)
        return(trelloBoardJson['name'])

    def findTrelloCards(self):
        # Here we are going to (based on who the person wants) find card info.
        #self.trelloUser = trelloUser
        trelloCardList = []
        trelloStatusList = []
        trelloCardUrl = "https://api.trello.com/1/members/my/cards?key={0}&token={1}".format(
                                                                                    self.devKey,
                                                                                    self.authToken)
        trelloCardPage = urllib2.Request(trelloCardUrl)
        trelloCardOpener = urllib2.build_opener()
        trelloCardOpened = trelloCardOpener.open(trelloCardPage)
        trelloCardJson = json.load(trelloCardOpened)
        for cardName in trelloCardJson:
            cleanString = str(cardName['name'])
            trelloCardList.append(cleanString)
        return(trelloCardList)

    def findCardStatus(self):
        # Here we will provide info back to the user regarding cards
        trelloStatusIdList = []
        trelloStatusList = []
        trelloCardUrl = "https://api.trello.com/1/members/my/cards?key={0}&token={1}".format(
                                                                                    self.devKey,
                                                                                    self.authToken)
        trelloCardPage = urllib2.Request(trelloCardUrl)
        trelloCardOpener = urllib2.build_opener()
        trelloCardOpened = trelloCardOpener.open(trelloCardPage)
        trelloCardJson = json.load(trelloCardOpened)
        for trelloStatusName in trelloCardJson:
            trelloStatusId = str(trelloStatusName['idList'])
            trelloStatusIdList.append(trelloStatusId)

        for trelloStatus in trelloStatusIdList:
            trelloStatusUrl = "https://api.trello.com/1/lists/{0}?fields=name&cards=open&card_fields=name&key={1}&token={2}".format(
                trelloStatus,
                self.devKey,
                self.authToken)
            trelloStatusPage = urllib2.Request(trelloStatusUrl)
            trelloStatusOpener = urllib2.build_opener()
            trelloStatusOpened = trelloStatusOpener.open(trelloStatusPage)
            trelloStatusJson = json.load(trelloStatusOpened)
            trelloStatusUpdate = ("".join([str(trelloStatusJson['name']), ":", str(trelloStatusJson['cards'][0]['name'])]))
            trelloStatusList.append(trelloStatusUpdate)
        return(trelloStatusList)

if __name__ == '__main__':
    smsProcessor = smsProcessFlow()
    print(smsProcessor.findCardStatus())
