__author__ = 'Ioannis'
# Remember to set verboseFlag in config.ini to False for distribution
# WARNING: Logging does not work in the APIHandler class, but does work for threads spawned from it

import threading
import queue
import logging
import sys

import my_gui
import config_handler


# Initializing and updating stats is better handled in the my_gui module
# def initialize(gui_queue, initLock):
#     print('Draft analyzer initialize')
#     with initLock:
#         AH_data_handler.main()
#     gui_queue.put(('Update', 'Auction House data updated'))
#
#     if config_handler.getter('verboseFlag'):
#         print("Auction House data updated")


def my_handler(type, value, tb):
    logger.exception("Draft Analyzer exception", exc_info=(type, value, tb))


def installThreadExcepthook():
    """
    Workaround for sys.excepthook thread bug
    From
    http://spyced.blogspot.com/2007/06/workaround-for-sysexcepthook-bug.html
    Call once from __main__ before creating any threads.
    """
    init_old = threading.Thread.__init__

    def init(self, *args, **kwargs):
        init_old(self, *args, **kwargs)
        run_old = self.run

        def run_with_except_hook(*args, **kw):
            try:
                run_old(*args, **kw)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                sys.excepthook(*sys.exc_info())
                if config_handler.getter('verboseFlag'):
                    raise
        self.run = run_with_except_hook
    threading.Thread.__init__ = init


# WARNING: Logging does not work in the APIHandler class, but does work for threads spawned from it
# THREADING WITH GUIS - needs fixing, why is gui sometimes not in the main thread
if __name__ == '__main__':
    # create logger
    logger = logging.getLogger('myLogger')
    # Specify logging file
    handler = logging.FileHandler('Draft Analyzer logs.log')
    logger.addHandler(handler)

    # Install exception handler
    sys.excepthook = my_handler

    installThreadExcepthook()           # Makes logging work in threads

    gui_queue = queue.Queue()           # Creates the queue necessary to interact with the GUI
    #threading.Thread(target=initialize, args=(gui_queue, initLock)).start()
    my_gui.main(gui_queue)



