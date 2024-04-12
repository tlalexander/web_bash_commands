
I had a simple issue, fixed it with some code, and am now sharing it as
a simple example in case anyone else wants to do something similar.

My issue: my desktop would connect to my bluetooth headphones and did not share
them nicely with my phone when they were both connected. The result was that I
could not listen to audio from my phone over bluetooth when my desktop bluetooth
was on.

This script lets me toggle on and off the bluetooth on my linux desktop using
siri from my phone. Since this is only an issue when I am trying to listen
to audio on my phone, using siri is a convenient way to activate the toggle.

When I say "Siri Desktop Off" this turns off my desktop's bluetooth within
about two seconds. I use a "shortcut", a feature built in to the iphone, to
tell siri to call a web page URL when I say "desktop on" or "desktop off".
(I found that if my activation phrase included the word 'bluetooth', siri got
confused)

This program hosts a web page on my local desktop. So if your desktop was called
"desktop" then the URL would be:
http://desktop.local/

Which displays "Hello World".

You can turn on bluetooth with:
http://desktop.local/bluetooth/on

And turn it off with:
http://desktop.local/bluetooth/off

Use the Shortcuts app on your iphone to program siri to hit these web URLS
using the "Get Contents of URL" function.

Make sure to run this program as root (required to share the web page on port 80)

You may want to set a cron job to run this program @reboot
