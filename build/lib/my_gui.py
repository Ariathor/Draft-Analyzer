# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import tkinter as tk
import queue
import threading
import math

import API_logger
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
        if self.myCollection == {}:                     # If collection is empty
            self.dataQueue.put(('Print', "Please update your collection by listing a card in the Auction House and then cancelling your auction"))
        self.cardColors = card_info_handler.simple_colors()                 # A dict of cards and their colors
        self.platIcon = tk.PhotoImage(file='Icons/plat_icon.gif')
        self.packNum = 0
        self.packs = {}                                                     # Save packs to show missing cards
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

        #self.searchBox = tk.Entry(self.menuBar)
        #self.searchBox.pack(side=tk.RIGHT, fill=tk.BOTH)


        # Tag configuration for collection mode and threshold mode
        # In case of an insert with multiple tags, the last configured tag applies
        self.text.tag_config("Strikethrough", overstrike = True)
        self.text.tag_config("Unknown", foreground='pink')
        self.text.tag_config("Colorless", foreground="black")
        self.text.tag_config("Diamond", foreground='grey')
        self.text.tag_config("Ruby", foreground='red')
        self.text.tag_config("Blood", foreground='purple')
        self.text.tag_config("Wild", foreground='green')
        self.text.tag_config("Sapphire", foreground="blue")
        self.text.tag_config("missing", foreground='red')
        self.text.tag_config("playset", foreground="green")
        self.text.tag_config("normal", foreground='black')

        if config_handler.read_color_mode() == 'thresholdMode':
            self.switch_colors()

        self.after_idle(self.poll)

    def write_one_line(self, line, *tags):
        try:
            tags = tuple(tags[0])
        except IndexError:                                  # *tags could be an empty tuple
            pass
        self.text.insert('1.0', line, tags)

    def write_multicolored(self, line, tags):
        # Careful if I add more tags
        # Tags are either (color1, color2, playsetTag) or (color1, color2, playsetTag, Strikethrough)
        print(tags)
        colorTags, *otherTags = tags
        colorTags = [x.strip() for x in colorTags.split(',')]  # Splitting tags on comma and stripping whitespace
        numColors = len(colorTags)
        counter = 0
        self.text.insert('1.0', '\n')
        for char in line[:-1]:                             # Ignoring the last character, which is a newline
            tags = (colorTags[counter%numColors], otherTags)   # Alternating between colorTags
            counter += 1
            self.text.insert('1.end', char, tags)

    def parse_request(self, msgTuple):
        # myMessage from API_logger
        # Format: ('DraftPack', Cardarray) or ('CardPicked', card) or ('DraftValue', value) or
        # ('Print', message) or ('Update', 'Collection updated')
        event,msg = msgTuple
        self.text['state'] = 'normal'

        self.write_one_line('\n')

        if event == 'DraftPack':
            try:
                if len(msg) < 8:
                    newPack = msg
                    msg = self.packs[8-len(msg)]
            except KeyError:
                pass
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
                line = card + '-' + str(numberOwned)+'\n'
                #line = '{0: <40}\n'.format(line)                    # Pads the line - Can't insert to tkinter past lineend
                tags = []
                try:
                    tags.append(self.cardColors[card])
                except KeyError:
                    tags.append("Unknown")
                if numberOwned <= 3:
                    tags.append('missing')
                elif numberOwned >=4:
                    tags.append('playset')
                try:
                    if card not in newPack:
                        tags.append("Strikethrough")
                except UnboundLocalError:
                    pass

                if ',' not in tags[0]:                                  # Non-multicolored cards
                    self.write_one_line(line, tags)
                elif ',' in tags[0]:                                    # Multicolored tags are seperated by commas
                    self.write_multicolored(line,tags)
                #self.text.insert('1.end', ' '*(40-len(line)))
                # Line is padded, else can't insert at 40. Consider removing normal tag if unhelpful.
                self.text.insert('1.end', ' '*(40-len(line)) + 'Price:' + str(platPrice), "normal")
                self.text.image_create('1.5 lineend', image=self.platIcon)

            # Initializes the pack number. Will work, as long as it's picks 1-15 (pack 1)
            if self.packNum == 0:
                self.packNum = 15 - len(msg) + 1
            else:
                self.packNum += 1
                if self.packNum > 45:
                    self.packNum = 1        # Reset to 1 if new draft was started

            pickNum = (self.packNum-1)%15+1
            numWheel = str(8-pickNum) if pickNum < 8 else 'No'
            line = 'Pack ' + str(math.ceil(self.packNum/15)) + ', Pick ' + str(pickNum) + '(' + str(numWheel) + ' cards wheel)\n\n'
            self.write_one_line(line)       # Pack X, Pick Y, (Z cards wheel)
            if pickNum <= 8:                # Only need to save packs 1-7
                self.packs[pickNum] = msg


        if event == 'CardPicked':
            self.write_one_line('Card Picked: ' + msg + '\n')

        if event == 'DraftValue':
            self.write_one_line('Total Draft Value: ' + str(msg))
            self.text.image_create('1.5 lineend', image=self.platIcon)

        if event == 'Print':
            self.write_one_line(msg + '\n')

        if event == 'Update':
            self.reload_stats()
            self.write_one_line(msg + '\n')


        self.text['state'] = 'disabled'

    def poll(self):
        try:
            data = self.dataQueue.get_nowait()              # data = (event, message)
        except queue.Empty:
            pass
        else:
            self.parse_request(data)
        self.after(500, self.poll)

    #Swaps colors between collection and threshold mode
    def switch_colors(self):
        if self.text.tag_names()[-2] != "playset":
            self.text.tag_raise("missing")
            self.text.tag_raise("playset")
            self.text.tag_raise("normal")
            config_handler.set_color_mode("collectionMode")                     # Update config.ini
        elif self.text.tag_names()[-2] == "playset":
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

    # Implement a search box in the future
    # def find(self):
    #     self.text.tag_remove('found', '1.0', tk.END)
    #     s = self.searchBox.get()
    #     if s:
    #         idx = '1.0'
    #         while 1:
    #             idx = self.text.search(s, idx, nocase=1, stopindex=tk.END)
    #             if not idx: break
    #             lastidx = '%s+%dc' % (idx, len(s))
    #             self.text.tag_add('found', idx, lastidx)
    #             idx = lastidx
    #         self.text.tag_config('found', foreground='red')
    #     self.searchBox.focus_set()


    #def switch_price(self):
    #    state = self.priceUsed.get()
    #    if state:



def main(exQueue):
    q = queue.Queue()
    myServer = threading.Thread(target=API_logger.start_server, args=(q,))
    myServer.daemon = True
    myServer.start()

    app = Gui(q)
    app.iconbitmap(default='Icons/D-Icon.ico')
    exQueue.put(app)                            # Put app in an external queue so the Draft Analyzer module can interact with it

    app.mainloop()

if __name__ == '__main__':
    testQueue = queue.Queue()
    main(testQueue)

