# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import os
from os.path import join as pjoin
import datetime
import time
import threading
import pyglet
import json
import requests
import queue
from http.server import BaseHTTPRequestHandler, HTTPServer

import collection_handler
import config_handler
import card_info_handler


class APIHandler(BaseHTTPRequestHandler):
    # Possible improvement: call __init__, make variables instance variables instead of class
    # def __init__(self, request, client_address, server):
    #    super().__init__(request, client_address, server)

    os.makedirs('API_logs', exist_ok=True)                  # Create directory API_logs if it does not already exist

    verboseFlag = config_handler.getter('verboseFlag')
    startTime = 0

    draftValue = 0
    store_path = pjoin(os.getcwd(), 'API_logs', datetime.date.today().strftime('%d-%m-%Y') + '.json') #Stores the data in a json folder with today's date
    collectionLock = threading.Lock()
    previousData = False

    TCG_Browser_URL = config_handler.getter('tcg_browser_url')

    def play_sound(self, sound_path):
        sound = pyglet.media.load(sound_path, streaming=False)
        sound.play()

    # Tries to send data to hex.tcgbrowser
    def send_to_browser(self, data):
        try:
            r = requests.post(self.TCG_Browser_URL, data=data)
        except Exception:
            if self.verboseFlag:
                print('Couldn\'t connect to hex.tcgbrowser')


    # Handles an incoming message depending on the type
    # See draft_pack_testing.py for examples on jsonDict formatting
    def my_data_parsing(self, jsonDict):

        # Write data to log
        #if jsonDict['Message'] not in ('PlayerUpdated', 'CardUpdated') or self.verboseFlag:
        if config_handler.getter('API_logging'):
            with open(APIHandler.store_path, 'a') as fp:
                fp.write(datetime.datetime.now().strftime('%H:%M:%S') + '\t' + str(jsonDict) + '\n')

        myMessage = ('', '')
        # First DraftPack for the last 20 minutes
        if jsonDict['Message'] == 'DraftPack' and len(jsonDict['Cards']) == 17 and (time.time() - APIHandler.startTime) >= 1500:
            threading.Thread(target=self.play_sound, args=('Sounds/short_ringtone.wav',)).start()
            APIHandler.startTime = time.time()
            gui_queue.put(('Reset', 'Reset draft value'))

        if jsonDict['Message'] == 'GameStarted':
            threading.Thread(target=self.play_sound, args=('Sounds/game_start.wav',)).start()

        if jsonDict['Message'] == 'DraftPack':
            # jsonDict['Cards'] is a list of card-dictionaries.
            # Each card-dictionary has the Guid, Flags and Gems keys
            draftPack = [card_info_handler.simple_guid_to_names(x['Guid']['m_Guid']) for x in jsonDict['Cards']]
            myMessage = ('DraftPack', draftPack)
            gui_queue.put(myMessage)

        elif jsonDict['Message'] == 'DraftCardPicked':
            card_picked = card_info_handler.simple_guid_to_names(jsonDict['Card']['Guid']['m_Guid'])
            myMessage = ('CardPicked', card_picked )
            gui_queue.put(myMessage)

            #threading.Thread(target=collection_handler.update_draft_value, args =(ahData[jsonDict[2][0]],)).start()
            # Needs updating to new format
            # collection_handler.draft_card_picked('Collection/My_Drafted_Cards.json', jsonDict['Card'])

        elif jsonDict['Message'] == 'Collection':
            if not os.path.isfile('Collection/My_Collection.json') and jsonDict['Action'] == 'Overwrite':
                gui_queue.put(('Update', 'Collection updated'))
            with APIHandler.collectionLock:
                collection_handler.collection_update(jsonDict)


        # I should handle other interesting cases here like collection.

    def handle_expect_100(self):
        if self.verboseFlag:
            print('Handing expect-100')                         # For testing only
        self.send_response_only(100)
        self.send_header("Content-Length", '0')
        self.end_headers()
        return True

    def do_POST(self):
        if self.path == '/draft_analyzer':

            length = self.headers['content-length']
            data = self.rfile.read(int(length))

            jsonDict = json.loads(data.decode())
            if self.verboseFlag and jsonDict['Message'] not in ('PlayerUpdated', 'CardUpdated'): # Prevent spam
                print("Got a connection from", self.client_address)
                print(data)

            # Forward the data if not identical to previous data (dirty hack to fix the double-event bug)
            # Not resolved in March 2016
            if data != APIHandler.previousData or jsonDict['Message'] not in ('DraftPack', 'DraftCardPicked'):
                threading.Thread(target=self.my_data_parsing, args=(jsonDict,)).start()
            if self.TCG_Browser_URL != '':
                threading.Thread(target=self.send_to_browser, args=(data,)).start()          # Forwards the data to hex.tcgbrowser
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
    global gui_queue          # Dirty hack, ideally I should be passing this to the __init__ function of the API_handler class
    gui_queue = q
    server = HTTPServer(('localhost', 18888), APIHandler)
    server.serve_forever()


if __name__ == '__main__':
    q = queue.Queue()
    start_server(q)

