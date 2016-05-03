
<p><a href="http://forums.cryptozoic.com/showthread.php?t=44232">A simple Draft Analyzer for Hex TCG</a></p>

<p><em>WARNING</em>: You need to read installation instructions carefully. There is no extensive documentation or tooltips, spend 5 minutes reading the instructions to avoid problems down the line.</p>

<h5><a id="user-content-what-does-this-do" class="anchor" href="#what-does-this-do" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>What does this do:</h5>

<p>This is an application developed by myself in my spare time to improve my drafting experience in Hex. It uses the Hex API, the Hex AH Data and the Hex Database(thanks DocX and cwik) to provide you with more information during drafting.</p>

<h5><a id="user-content-features" class="anchor" href="#features" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Features:</h5>

<ul>
<li><p>For each draft pack, you receive a list of cards together with their platinum price and the number you currently have in your collection. The 14-day median is used for the price, unless there have been less than 5 sales in the past 14 days in which case the all-time median is used.</p></li>
<li><p>Two modes: In the collection mode, if you own 4 or more of a card it's show in green. If you don't have a playset of that card it's shown in red instead. In the threshold mode, cards are colored depending on their threshold requirement (Diamond-Grey, Ruby-Red, Sapphire-Blue, Blood-Purple, Wild-Green, Artifacts - Black). This allows you to see at a glance the composition of the pack. For example, you can quickly check how many diamond cards you passed in pack 1 to adjust your expectations for pack 2 (if you passed a ton of great diamond cards, your neighbor is probably in diamond and won't be passing you the good diamond cards in pack 2).</p></li>
<li><p>Warning sounds. You get a short soundtrack whenever a draft fires. Never miss your first pick again because you went to the next room to get a glass of water. Additionally you get a much shorter sound whenever a game starts, so you can alt-tab in peace. You can change these sounds by replacing the files in the sound directory (just make sure your replacement sounds have the same name/format).</p></li>
<li><p>Improved syncing with Hex TCG Browser. If you have syncing with Hex TCG Browser enabled, you might have noticed your client getting unresponsive for 30-120 seconds at the end of each draft before you start building your deck. That happens due to a bug in the Hex client. The Hex API tries to sync your collection 45 times (one for each card you drafted) and hangs until all 45 times are completed. If you do that over the internet it takes a noticeable amount of time, especially for large collections. If you enable syncing through the draft analyzer, the hex client only has to transfer the data locally, which is much faster and then the draft analyzer forwards the data to Hex TCG Browser.</p></li>
<li><p>Writes the total value of your draft after each pick your make. You can force it to ignore non-legendary cards that sell for the platinum floor (commons that sell for less than 5 plat, uncommons that sell for less than 12 and rares that sell for less than 32), by changing trimprices to True in the config.ini and restarting the application.</p></li>
<li><p>Exporting your collection to an excel-readable CSV file. Exports your collection adding some extra information for those who like to keep track of it in a spreadsheet. The exported spreadsheet can be found under Collection/My_Collection.csv</p></li>
</ul>

<p>Screenshots: <a href="http://imgur.com/a/zUdr7">http://imgur.com/a/zUdr7</a></p>

<h5><a id="user-content-installation-instructions" class="anchor" href="#installation-instructions" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Installation instructions:</h5>

<ul>
<li>Download the zip file</li>
<li>Right-click and select "Extract All"</li>
<li>Run Draft Analyzer.exe</li>
<li>WARNING: The first time you launch the application you might need to wait some minutes (depending on your internet connection), until all the AH-Data is downloaded. The application is NOT stuck. You can check the AH-Data folder to see the progression. After all data is downloaded, the application will launch normally.</li>
<li>(Optional) Set up syncing with Hex TCG Browser. Find your syncing URL by following instructions here – <a href="http://hex.tcgbrowser.com/tools/sync/">http://hex.tcgbrowser.com/tools/sync/</a>. Copy-Paste the entire link in the text box that appears and submit (careful to not include extra spaces). If you want to disable the syncing feature in the future, just click on syncing again and submit without typing anything.</li>
<li>Go to your Hex installation directory (usually C:\Program Files\Hex) and open the config.ini with a text editor. Add the following lines:</li>
</ul>

<pre><code>    Notifications=http://localhost:18888/draft_analyzer
    TypesForwarded=All
</code></pre>

<p>This is to enable the Hex API. Don't worry, it only sends data to your computer and will never broadcast any sensitive data. If want to add another application for syncing, you can separate the addresses by ||. For example:</p>

<pre><code>    Notifications=http://localhost:18888/draft_analyzer || SECOND_URL_HERE
    TypesForwarded=All
</code></pre>

<ul>
<li>Start the Hex Client (restart if it was already running).</li>
<li>With the draft analyzer still running, list a card on the Auction House and cancel it. This is to force the API to export your collection.</li>
<li>Jump into a draft and watch the magic happen.</li>
</ul>

<h5><a id="user-content-troubleshooting" class="anchor" href="#troubleshooting" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Troubleshooting:</h5>

<p>In case of problems, before posting on the forums try the following steps:</p>

<ul>
<li> Restart Hex and Draft Analyzer.</li>
<li> Make sure the files of the Draft Analyzer directory are not used by any other application.</li>
<li> Delete the AH-Data directory and relaunch the application. This should solve problems with strange numbers, but you will need to wait until all the data is downloaded again.</li>
<li> Run with administrator privileges. This will definitely be needed if you placed the folder in Program Files.</li>
<li> The nuclear option: delete the whole Draft Analyzer directory and download again.</li>
<li> If nothing helps you can contact me. Make sure to include Draft Analyzer.log and the API_logs from the day of the problem.</li>
<li> Depending on interest I might also stream some drafts and show people how I use the Draft Analyzer: <a href="http://www.twitch.tv/ariathor/profile">http://www.twitch.tv/ariathor/profile</a></li>
</ul>

<h5><a id="user-content-uninstalling" class="anchor" href="#uninstalling" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Uninstalling:</h5>

<p>Just delete the Draft Analyzer folder. Everything is self-contained.</p>

<h5><a id="user-content-in-the-future" class="anchor" href="#in-the-future" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>In the Future:</h5>

<ul>
<li>The application will need to be updated next week, due to some (great) changes to the Hex API. I will post up the new version as soon as the patch hits. O</li>
<li>One of the features I have planned is to show cards that were in the pack and didn't wheel, for picks 8-15.</li>
<li>I also have a working bargain-hunting module, that suggests what cards in your collection you can sell for a reasonable price, but I would need some time to create a working GUI and allow the user chose the options (without changing the source code0.</li>
<li>If you want to help with development you are welcome to look at the source code (in the build directory). You will probably notice that I could use some help from a threading or a gui (tkinter) expert.</li>
</ul>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="hidden">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59 0.4 0.07 0.55-0.17 0.55-0.38 0-0.19-0.01-0.82-0.01-1.49-2.01 0.37-2.53-0.49-2.69-0.94-0.09-0.23-0.48-0.94-0.82-1.13-0.28-0.15-0.68-0.52-0.01-0.53 0.63-0.01 1.08 0.58 1.23 0.82 0.72 1.21 1.87 0.87 2.33 0.66 0.07-0.52 0.28-0.87 0.51-1.07-1.78-0.2-3.64-0.89-3.64-3.95 0-0.87 0.31-1.59 0.82-2.15-0.08-0.2-0.36-1.02 0.08-2.12 0 0 0.67-0.21 2.2 0.82 0.64-0.18 1.32-0.27 2-0.27 0.68 0 1.36 0.09 2 0.27 1.53-1.04 2.2-0.82 2.2-0.82 0.44 1.1 0.16 1.92 0.08 2.12 0.51 0.56 0.82 1.27 0.82 2.15 0 3.07-1.87 3.75-3.65 3.95 0.29 0.25 0.54 0.73 0.54 1.48 0 1.07-0.01 1.93-0.01 2.2 0 0.21 0.15 0.46 0.55 0.38C13.71 14.53 16 11.53 16 8 16 3.58 12.42 0 8 0z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.07325s from github-fe127-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15.72 12.5l-6.85-11.98C8.69 0.21 8.36 0.02 8 0.02s-0.69 0.19-0.87 0.5l-6.85 11.98c-0.18 0.31-0.18 0.69 0 1C0.47 13.81 0.8 14 1.15 14h13.7c0.36 0 0.69-0.19 0.86-0.5S15.89 12.81 15.72 12.5zM9 12H7V10h2V12zM9 9H7V5h2V9z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-PwLymWYsJfjsDCMHlc6VkgDecPxtObovAU9mD4n2MBo=" src="https://assets-cdn.github.com/assets/frameworks-3f02f299662c25f8ec0c230795ce959200de70fc6d39ba2f014f660f89f6301a.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-s09U6rzND/qQ4yLP/bDbI51JK5qYYJLxqmAsXPhNNrQ=" src="https://assets-cdn.github.com/assets/github-b34f54eabccd0ffa90e322cffdb0db239d492b9a986092f1aa602c5cf84d36b4.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15.72 12.5l-6.85-11.98C8.69 0.21 8.36 0.02 8 0.02s-0.69 0.19-0.87 0.5l-6.85 11.98c-0.18 0.31-0.18 0.69 0 1C0.47 13.81 0.8 14 1.15 14h13.7c0.36 0 0.69-0.19 0.86-0.5S15.89 12.81 15.72 12.5zM9 12H7V10h2V12zM9 9H7V5h2V9z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

