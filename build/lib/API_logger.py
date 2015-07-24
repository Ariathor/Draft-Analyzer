# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import os
from os.path import join as pjoin
import datetime
import time
import threading
#import winsound
import json
import requests
import queue
from http.server import BaseHTTPRequestHandler, HTTPServer

import collection_handler
import AH_data_handler
import config_handler



class APIHandler(BaseHTTPRequestHandler):
    # Possible improvement: call __init__, make variables instance variables instead of class
    # def __init__(self, request, client_address, server):
    #    super().__init__(request, client_address, server)

    os.makedirs('API_logs', exist_ok=True)                  # Create directory API_logs if it does not already exist

    verboseFlag = config_handler.verboseFlag
    startTime = 0
    collectionAccessTime = 0

    # Imports the cards' value dictionary. Uses trimmed values if trimmedValues = true
    trimmedValues = config_handler.read_price_mode()
    ahData = AH_data_handler.open_trimmed_values() if trimmedValues else AH_data_handler.open_simple_median()
    draftValue = 0
    store_path = pjoin(os.getcwd(), 'API_logs', datetime.date.today().strftime('%d-%m-%Y') + '.json') #Stores the data in a json folder with today's date
    previousData = False

    forwardingFlag, TCG_Browser_URL = config_handler.read_url()

    # disabled for Mac build
    #def play_sound(self, sound_path):
    #   winsound.PlaySound(sound_path, winsound.SND_FILENAME)

    # Tries to send data to hex.tcgbrowser
    def send_to_browser(self, data):
        try:
            r = requests.post(self.TCG_Browser_URL, data=data)
        except:
            if self.verboseFlag:
                print('Couldn\'t connect to hex.tcgbrowser')


    # Handles an incoming message depending on the type
    # See draft_pack_testing.py for examples on jsonDict formatting
    def my_data_parsing(self, jsonDict):
        # Write data to log
        if jsonDict['Message'] not in ('PlayerUpdated', 'CardUpdated') or self.verboseFlag:
            with open(APIHandler.store_path, 'a') as fh:
                fh.write(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + str(jsonDict) + '\n')


        myMessage = ('', '')

        # disabled for Mac build
        #if jsonDict['Message'] == 'DraftPack' and len(jsonDict['Cards']) == 15 and (time.time() - APIHandler.startTime) >= 1200:         # Play a sound if this is the first DraftPack for the last 25 minutes
        #    threading.Thread(target=self.play_sound, args=('Sounds/short_ringtone.wav',)).start()
        #    APIHandler.startTime = time.time()
        #    APIHandler.draftValue = 0

        # disabled for Mac build
        #if jsonDict['Message'] == 'GameStarted':
        #    threading.Thread(target=self.play_sound, args=('Sounds/game_start.wav',)).start()

        if jsonDict['Message'] == 'DraftPack':
            draftPack = [x['Name'] for x in jsonDict['Cards']]  # jsonDict['Cards'] is a list of card-dictionaries
            myMessage = ('DraftPack', draftPack)
            dataQueue.put(myMessage)

            # if len(jsonDict[2]) == 1:
            #    lastCard = True
        elif jsonDict['Message'] == 'DraftCardPicked':
            myMessage = ('CardPicked', jsonDict['Card']['Name'])
            try:
                cardWithoutCommas = jsonDict['Card']['Name'].replace(',', '')                     # AH Data has no commas
                APIHandler.draftValue += self.ahData[cardWithoutCommas]
            except KeyError:
                pass
            dataQueue.put(myMessage)
            #threading.Thread(target=collection_handler.update_draft_value, args =(ahData[jsonDict[2][0]],)).start()
            dataQueue.put(('DraftValue', self.draftValue))
            collection_handler.draft_card_picked('Collection/My_Drafted_Cards.json', jsonDict['Card'])
        elif jsonDict['Message'] == 'Collection':
            if not os.path.isfile('Collection/My_Collection.json'):
                dataQueue.put(('Update', 'Collection updated'))
            collection_handler.collection_dump('Collection/My_Collection.json', jsonDict['Cards'])

        # I should handle other interesting cases here like collection. I should also save draft picks.

    def handle_expect_100(self):
        if self.verboseFlag:
            print('Handing expect-100')                         # For testing only
        self.send_response_only(100)
        self.send_header("Content-Length", '0')
        self.end_headers()
        return True

    def do_POST(self):
        if self.path == '/draft_analyzer':
            if self.verboseFlag:
                print("Got a connection from", self.client_address)
            length = self.headers['content-length']
            data = self.rfile.read(int(length))
            if self.verboseFlag:
                print(data)

            jsonDict = json.loads(data.decode())
            # Ugly fix to the collection spam at the end of draft problem
            #if jsonDict['Message'] != 'Collection' or time.time() - APIHandler.collectionAccessTime >= 20:
            if data != APIHandler.previousData:
                threading.Thread(target=self.my_data_parsing, args=(jsonDict,)).start()  # Forwards the data to the other functions
                if self.forwardingFlag:
                    threading.Thread(target=self.send_to_browser, args=(data,)).start()          # Forwards the data to hex.tcgbrowser
                if jsonDict['Message'] == 'Collection':
                    APIHandler.collectionAccessTime = time.time()
            APIHandler.previousData = data
            # Send proper response
            expect = self.headers.get('Expect', "")
            if expect.lower() == "100-continue":
                self.handle_expect_100()
            else:
                self.send_response_only(200)
                self.send_header("Content-Length", '0')
                self.end_headers()



# Can no longer run the server alone, it needs to be passed the queue created by the GUI
def start_server(q):
    global dataQueue          # Dirty hack, ideally I should be passing this to the __init__ function of a class
    dataQueue = q
    server = HTTPServer(('localhost', 18888), APIHandler)
    server.serve_forever()


if __name__ == '__main__':
    q = queue.Queue()
    start_server(q)

