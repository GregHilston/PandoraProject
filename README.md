PandoraProject
==============
<i>Note: Tested on Google Chrome Version 36.0.1985.125 </i>

As there is no official API for Pandora and the unofficial API hasn't been working as expected, I'll be writing scripts to grab the data I need from Pandora.
If you're like me, you have many likes on Pandora. As of writing this, I have over 700 thumbed up tracks. Pandora has made it quite difficult to get access to this data. I believe they hide this, so users cannot easily take their data and go to competitors such as Spotify or making a youtube playlist. These scripts should assist you in pulling data from Pandora. Enjoy!

How To Execute: In Google Chrome press [Ctrl + Shift + J] and in the console

<h4>[Automate Show More](https://github.com/GregHilston/PandoraProject/blob/master/automate_show_more.js)</h4>

When browsing http://www.pandora.com/profile/likes/[username] Pandora hides your likes behind a "show more" button. Upon each click, the next five songs are displayed.

This script will automate the process of clicking the "show more" button as many times as needed.


<h4>[Get Thumbed Up Tracks](https://github.com/GregHilston/PandoraProject/blob/master/print_thumbed_up_songs.js)</h4>

Prints to the console every thumbed up song on the page. Executing this script after "Automate Show More", will print every song you've thumbed up.
