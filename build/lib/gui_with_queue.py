# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import tkinter as tk
import queue
import threading

import API_logger_with_GUI
import collection_handler
import AH_data_handler
import card_info_handler
import config_handler



class Gui(tk.Tk):
    def __init__(self, dataQueue):
        tk.Tk.__init__(self)
        self.wm_title('Draft Analyzer')
        self.dataQueue = dataQueue
        self.ahData = AH_data_handler.open_simple_median()            # Imports the cards' value dictionary
        self.myCollection = collection_handler.collection_open('Collection/My_Collection.json')  # Imports the collection dictionary
        self.cardColors = card_info_handler.simple_colors()                 # A dict of cards and their colors
        self.platIcon = tk.PhotoImage(file='Icons/plat_icon.gif')
        #self.priceUsed = tk.BooleanVar()
        #self.priceUsed.set(True)
        #self.priceUsed.trace('w', self.switch_price)

        # Create menu on top
        self.menuBar = tk.Menu(self)
        self.menuBar.add_command(label="Switch Colors", command=self.switch_colors)
        self.menuBar.add_command(label="Syncing", command=self.click_syncing)
        #self.menuBar.add_checkbutton(label="PriceUsed", onvalue=True, offvalue=False, variable=self.priceUsed)
        self.menuBar.add_command(label="Export Collection", command=collection_handler.export_collection)
        self.menuBar.add_command(label="Clear", command=self.clear)
        self.config(menu=self.menuBar)

        # Main part of the GUI
        # A frame contains the text widget and the scrollbar
        text_frame = tk.Frame(borderwidth=1, relief="sunken")
        self.text = tk.Text(wrap="word", background="white", state='disabled', borderwidth=0, highlightthickness=0)
        self.vsb = tk.Scrollbar(orient="vertical", borderwidth=1,command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(in_=text_frame,side="right", fill="y", expand=False)
        self.text.pack(in_=text_frame, side="left", fill="both", expand=True)
        text_frame.pack(side="bottom", fill="both", expand=True)


        # Tag configuration for collection mode and threshold mode
        # In case of an insert with multiple tags, the last configured tag applies
        self.text.tag_config("Unknown", foreground='pink')
        self.text.tag_config("Colorless", foreground="black")
        self.text.tag_config("Diamond", foreground='grey')
        self.text.tag_config("Ruby", foreground='red')
        self.text.tag_config("Blood", foreground='purple')
        self.text.tag_config("Wild", foreground='green')
        self.text.tag_config("Sapphire", foreground="blue")
        self.text.tag_config("missing", foreground='red')
        self.text.tag_config("playset", foreground="green")

        if config_handler.read_color_mode() == 'thresholdMode':
            self.switch_colors()

        self.after_idle(self.poll)

    def write_one_line(self, line, *tags):
        try:
            tags = tuple(tags[0])
        except IndexError:                                  # *tags could be an empty tuple
            pass
        self.text.insert('1.0', line, tags)


    def write_to_log(self, msgTuple):
        event = msgTuple[0]
        msg = msgTuple[1]
        self.text['state'] = 'normal'

        self.write_one_line('\n')

        if event == 'DraftPack':
            for card in msg:
                try:
                    numberOwned = self.myCollection[card]
                except KeyError:
                    numberOwned = 0
                try:
                    cardWithoutCommas = card.replace(',', '')                     # AH Data has no commas
                    platPrice = self.ahData[cardWithoutCommas]
                except KeyError:
                    platPrice = 0
                line = card + '-' + str(numberOwned)
                line = '{0: <36}Price:{1}\n'.format(line, platPrice)              # Pads the line and adds the price
                tags = []
                try:
                    tags.append(self.cardColors[card])
                except KeyError:
                    tags.append("Unknown")
                if numberOwned <= 3:
                    tags.append('missing')
                elif numberOwned >=4:
                    tags.append('playset')

                self.write_one_line(line, tags)
                self.text.image_create('1.5 lineend', image=self.platIcon)

            numWheel = str(len(msg) - 8) if len(msg) - 8 > 0 else "None"
            self.write_one_line('Number of cards that will wheel: ' + numWheel + '\n\n')

        if event == 'CardPicked':
            self.write_one_line('Card Picked: ' + msg + '\n')

        if event == 'DraftValue':
            self.write_one_line('Total Draft Value: ' + str(msg))
            self.text.image_create('1.5 lineend', image=self.platIcon)

        self.text['state'] = 'disabled'

    def poll(self):
        try:
            data = self.dataQueue.get_nowait()              # data = (event, message)
        except queue.Empty:
            pass
        else:
            self.write_to_log(data)
        self.after(1000, self.poll)

    #Swaps colors between collection and threshold mode
    def switch_colors(self):
        if self.text.tag_names()[-1] != "playset":
            self.text.tag_raise("missing")
            self.text.tag_raise("playset")
            config_handler.set_color_mode("collectionMode")                     # Update config.ini
        elif self.text.tag_names()[-1] == "playset":
            self.text.tag_lower("missing")
            self.text.tag_lower("playset")
            config_handler.set_color_mode("thresholdMode")


    def click_syncing(self):
        def set_url(url):
            url = url.get()

            # Modifies variables in API_logger_with_GUI for this instance of the program
            # Possible improvent: Implement the variables as instance variables in APIHandler and modify them with a function
            if not isinstance(url, str) or url == "":
                API_logger_with_GUI.APIHandler.forwardingFlag = False
            else:
                API_logger_with_GUI.APIHandler.TCG_Browser_URL = url
                API_logger_with_GUI.APIHandler.forwardingFlag = True

            # Save url in config.ini for future use
            config_handler.set_url(url)
            toplevel.destroy()

        # Possible improvement: Use trace to react to change in variable automatically
        url = tk.StringVar()
        toplevel = tk.Toplevel()
        label1 = tk.Label(toplevel, text="Enter the FULL Hex tcgBrowser URL to sync. Leave empty to disable syncing.", height=0, width=65)
        label1.pack()
        urlEntry = tk.Entry(toplevel, width=65, textvariable=url, bd=5)
        urlEntry.pack()
        b = tk.Button(toplevel, text="Submit", command=lambda: set_url(url))
        b.pack(side=tk.BOTTOM)

    def clear(self):
        self.text['state'] = 'normal'
        self.text.delete("1.0", tk.END)
        self.text['state'] = 'disabled'
        self.reload_stats()

    def reload_stats(self):
        self.ahData = AH_data_handler.open_simple_median()
        self.myCollection = collection_handler.collection_open('Collection/My_Collection.json')

    #def switch_price(self):
    #    state = self.priceUsed.get()
    #    if state:



def main(exQueue):
    q = queue.Queue()
    myServer = threading.Thread(target=API_logger_with_GUI.start_server, args=(q,))
    myServer.daemon = True
    myServer.start()

    app = Gui(q)
    app.iconbitmap(default='Icons/D-Icon.ico')
    exQueue.put(app)                            # Put app in an external queue so the Draft Analyzer module can interact with it

    app.mainloop()

if __name__ == '__main__':
    testQueue = queue.Queue()
    main(testQueue)

