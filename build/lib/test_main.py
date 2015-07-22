__author__ = 'Ioannis'

import threading
import time

import download_data
import AH_data_handler
import my_gui
import draft_pack_testing


def initialize():
    download_data.main()
    AH_data_handler.main()
    print("Initialization Complete")

def test():
    time.sleep(10)
    with myLock:
        draft_pack_testing.test()

# THREADING WITH GUIS - needs fixing, why is gui not in the main thread
if __name__ == '__main__':
    threading.Thread(target=initialize).start()
    threading.Thread(target=test).start()
    myLock = threading.Lock()
    my_gui.main()



