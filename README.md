# Draft-Analyzer
A simple Draft Analyzer for Hex TCG

# Draft-Analyzer
[A simple Draft Analyzer for Hex TCG](http://forums.cryptozoic.com/showthread.php?t=44232)

*WARNING*: You need to read installation instructions carefully. There is no extensive documentation or tooltips, spend 5 minutes reading the instructions to avoid problems down the line.

#####What does this do:

This is an application developed by myself in my spare time to improve my drafting experience in Hex. It uses the Hex API, the Hex AH Data and the Hex Database(thanks DocX and cwik) to provide you with more information during drafting.

#####Features:

- For each draft pack, you receive a list of cards together with their platinum price and the number you currently have in your collection. The 14-day median is used for the price, unless there have been less than 5 sales in the past 14 days in which case the all-time median is used.

- Two modes: In the collection mode, if you own 4 or more of a card it's show in green. If you don't have a playset of that card it's shown in red instead. In the threshold mode, cards are colored depending on their threshold requirement (Diamond-Grey, Ruby-Red, Sapphire-Blue, Blood-Purple, Wild-Green, Artifacts - Black). This allows you to see at a glance the composition of the pack. For example, you can quickly check how many diamond cards you passed in pack 1 to adjust your expectations for pack 2 (if you passed a ton of great diamond cards, your neighbor is probably in diamond and won't be passing you the good diamond cards in pack 2).

- Warning sounds. You get a short soundtrack whenever a draft fires. Never miss your first pick again because you went to the next room to get a glass of water. Additionally you get a much shorter sound whenever a game starts, so you can alt-tab in peace. You can change these sounds by replacing the files in the sound directory (just make sure your replacement sounds have the same name/format).

- Improved syncing with Hex TCG Browser. If you have syncing with Hex TCG Browser enabled, you might have noticed your client getting unresponsive for 30-120 seconds at the end of each draft before you start building your deck. That happens due to a bug in the Hex client. The Hex API tries to sync your collection 45 times (one for each card you drafted) and hangs until all 45 times are completed. If you do that over the internet it takes a noticeable amount of time, especially for large collections. If you enable syncing through the draft analyzer, the hex client only has to transfer the data locally, which is much faster and then the draft analyzer forwards the data to Hex TCG Browser.

- Writes the total value of your draft after each pick your make. You can force it to ignore non-legendary cards that sell for the platinum floor (commons that sell for less than 5 plat, uncommons that sell for less than 12 and rares that sell for less than 32), by changing trimprices to True in the config.ini and restarting the application.

- Exporting your collection to an excel-readable CSV file. Exports your collection adding some extra information for those who like to keep track of it in a spreadsheet. The exported spreadsheet can be found under Collection/My_Collection.csv


Screenshots: http://imgur.com/a/zUdr7



#####Installation instructions:

- Download the zip file
- Right-click and select "Extract All"
- Run Draft Analyzer.exe
- WARNING: The first time you launch the application you might need to wait some minutes (depending on your internet connection), until all the AH-Data is downloaded. The application is NOT stuck. You can check the AH-Data folder to see the progression. After all data is downloaded, the application will launch normally.
- (Optional) Set up syncing with Hex TCG Browser. Find your syncing URL by following instructions here – http://hex.tcgbrowser.com/tools/sync/. Copy-Paste the entire link in the text box that appears and submit (careful to not include extra spaces). If you want to disable the syncing feature in the future, just click on syncing again and submit without typing anything.
- Go to your Hex installation directory (usually C:\Program Files\Hex) and open the config.ini with a text editor. Add the following lines:
```
    Notifications=http://localhost:18888/draft_analyzer
    TypesForwarded=All
```
  This is to enable the Hex API. Don't worry, it only sends data to your computer and will never broadcast any sensitive data. If want to add another application for syncing, you can separate the addresses by ||. For example:
```
    Notifications=http://localhost:18888/draft_analyzer || SECOND_URL_HERE
    TypesForwarded=All
```
- Start the Hex Client (restart if it was already running).
- With the draft analyzer still running, list a card on the Auction House and cancel it. This is to force the API to export your collection.
- Jump into a draft and watch the magic happen.




#####Troubleshooting:

In case of problems, before posting on the forums try the following steps:

-  Restart Hex and Draft Analyzer.
-  Make sure the files of the Draft Analyzer directory are not used by any other application.
-  Delete the AH-Data directory and relaunch the application. This should solve problems with strange numbers, but you will need to wait until all the data is downloaded again.
-  Run with administrator privileges. This will definitely be needed if you placed the folder in Program Files.
-  The nuclear option: delete the whole Draft Analyzer directory and download again.
-  If nothing helps you can contact me. Make sure to include Draft Analyzer.log and the API_logs from the day of the problem.
-  Depending on interest I might also stream some drafts and show people how I use the Draft Analyzer: http://www.twitch.tv/ariathor/profile



#####Uninstalling:

Just delete the Draft Analyzer folder. Everything is self-contained.



#####In the Future:

  - The application will need to be updated next week, due to some (great) changes to the Hex API. I will post up the new version as soon as the patch hits. O
  - One of the features I have planned is to show cards that were in the pack and didn't wheel, for picks 8-15.
  - I also have a working bargain-hunting module, that suggests what cards in your collection you can sell for a reasonable price, but I would need some time to create a working GUI and allow the user chose the options (without changing the source code0.
  - If you want to help with development you are welcome to look at the source code (in the build directory). You will probably notice that I could use some help from a threading or a gui (tkinter) expert.
