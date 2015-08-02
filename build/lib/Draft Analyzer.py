__author__ = 'Ioannis'
# Remember to set verboseFlag in config_handler to False for distribution

import threading
import queue
import logging
import sys

import download_data
import AH_data_handler
import my_gui
import config_handler


def initialize(exQueue):
    download_data.main()
    AH_data_handler.main()
    gui = exQueue.get()                     # Currently used instance of the Gui class
    gui.reload_stats()                      # Possibly problematic if initialize finishes before gui is created

    if config_handler.verboseFlag:
        print("Initialization Complete")

# # create logger
# logger = logging.getLogger('myLogger')
# handler = logging.FileHandler('my_draft_analyzer.log')
# logger.addHandler(handler)
#
# def my_handler(type, value, tb):
#     logger.error("Draft Analyzer exception", exc_info=(type, value, tb))
#     if config_handler.verboseFlag:
#         print(type, value, tb)
#
#
# # Install exception handler
# sys.excepthook = my_handler

# THREADING WITH GUIS - needs fixing, why is gui not in the main thread
if __name__ == '__main__':
    exQueue = queue.Queue(maxsize=1)
    threading.Thread(target=initialize, args=(exQueue,)).start()
    my_gui.main(exQueue)


