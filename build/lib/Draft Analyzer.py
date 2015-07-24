__author__ = 'Ioannis'
# Remember to set verboseFlag in config_handler to False for distribution

import threading
import queue

import download_data
import AH_data_handler
import my_gui
import config_handler

import logging

# These could be changed into better settings
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename='systemlog.log')


def initialize(exQueue):
    download_data.main()
    AH_data_handler.main()
    gui = exQueue.get()                     # Currently used instance of the Gui class
    gui.reload_stats()                      # Possibly problematic if initialize finishes before gui is created

    if config_handler.verboseFlag:
        print("Initialization Complete")

# THREADING WITH GUIS - needs fixing, why is gui not in the main thread
if __name__ == '__main__':
    try:
        exQueue = queue.Queue(maxsize=1)
        threading.Thread(target=initialize, args=(exQueue,)).start()
        my_gui.main(exQueue)
    except:
        logging.exception("Draft Analyzer ERROR:")

