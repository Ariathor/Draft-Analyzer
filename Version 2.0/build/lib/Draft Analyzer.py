__author__ = 'Ioannis'

import threading
import queue

import download_data
import AH_data_handler
import gui_with_queue


def initialize(exQueue):
    download_data.main()
    AH_data_handler.main()
    gui = exQueue.get()                     # Currently used instance of the Gui class
    gui.reload_stats()                      # Possibly problematic if initialize finishes before gui is created
    #print("Initialization Complete")

# THREADING WITH GUIS - needs fixing, why is gui not in the main thread
if __name__ == '__main__':
    exQueue = queue.Queue(maxsize=1)
    threading.Thread(target=initialize, args=(exQueue,)).start()
    gui_with_queue.main(exQueue)

