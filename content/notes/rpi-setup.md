---
title: "Raspberry Pi setup"
draft: false
---

## Raspberry Pi setup

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_krkfenre&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_rqh2illx" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Stuff you need (all in your kit)

* Raspberry Pi 4
* micro SD card
* USB-C power supply
* USB-serial adapter, AKA a console cable

You may also need a USB card reader, if you don't have a card slot built into your computer. We have some adapters in the bin under the pickup table that you can borrow to burn your SD card if needed.

To connect the console cable, look at this diagram.

![RPi console cable connection](/img/rpi_console_cable.png)

There are more details if you need them in [Adafruit's console cable tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/connect-the-lead).

## Setup checklist

<ul style="list-style: none;">
  <li><input type="checkbox"> Download OS image</li>
  <li><input type="checkbox"> Burn image to micro SD card with Imager</li>
  <li><input type="checkbox"> Edit config.txt on micro SD card to include: `enable_uart=1`</li>
  <li><input type="checkbox"> Connect RPi to laptop with console cable</li>
  <li><input type="checkbox"> Put micro SD card in slot of Pi</li>
  <li><input type="checkbox"> Open Putty (Windows) or Terminal (macOS)</li>
  <li><input type="checkbox"> Start a session at 115200 bps to the Pi</li>
  <li><input type="checkbox"> Connect USB-C power cable</li>
  <li><input type="checkbox"> Log in with username `pi` and password `raspberry`</li>
  <li><input type="checkbox"> Run `sudo raspi-config` to set up your wireless connection and enable SSH.</li>
</ul>

## Checklist for Tufts_Wireless

<ul style="list-style: none;">
  <li><input type="checkbox"> Figure out the Pi's MAC address with `ifconfig`</li>
  <li><input type="checkbox"> Register that MAC address with Tufts IT</li>
  <li><input type="checkbox"> Wait a few minutes for MAC address permissions to propagate to local wireless access point</li>
  <li><input type="checkbox"> Add network information to `/etc/wpa_supplicant/wpa_supplicant.conf`</li>
  <li><input type="checkbox"> Reboot Pi</li>
</ul>

## Checklist for Tufts_Secure

There's a bug in `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant` in the current version of Raspbian OS (based on Debian 10.4, Buster). This post explains how to fix it, but we haven't verified that it works yet: https://medium.com/@iced_burn/raspberry-pi-connected-to-wifi-of-wpa2-enterprise-ddd5a40c0b07

## FAQ

**What OS image should I use?**

Unless you have a good reason not to, you should start with [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspbian/). Previously called Raspbian, the OS should be based on Debian Buster or newer (as older versions will not work with a Pi 4).

**How do I figure out what name is assigned to the USB-serial adapter when I plug it in?**

On Windows 10, it's usually `COM3` (but it is not uncommon to have a different number). You can check for sure in the Device Manager control panel under Ports (COM & LPT)

On macOS, it's called `/dev/tty.usbserial-123456`, but the numbers at the end change. You can check it by running `ls /dev` in Terminal.

On Linux it's called `/dev/ttyACM0`, but the number will depend on how many USB devices are plugged in. As with macOS, you can check by running `ls /dev` in Terminal.

**When I open config.txt with Notepad, the lines all run together. How do I fix this?**

Use a better text editor, like [Sublime Text](https://www.sublimetext.com/), [Textmate](https://macromates.com/), or [Notepad++](https://notepad-plus-plus.org/). You could also try Wordpad.

**What network settings do I need for the Tufts wireless network?**

<pre class="code">network={
    ssid="Tufts_Wireless"
    key_mgmt=NONE
}
</pre>

**What about Tufts Secure?**

{{< hint danger >}} Read the note above about the bug in `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant`. {{< /hint >}}

The LA's can tell you the Nolop_IOT password; we try to avoid publishing passwords on the internet.

<pre class="code">network={
    ssid="Tufts_Secure"
    key_mgmt=WPA-EAP
    pairwise=CCMP
    eap=PEAP
    identity="Nolop_IOT"
    password="YOU PUT THE PASSWORD HERE IN QUOTES"
    phase2="auth=MSCHAPV2"
}
</pre>

**What if I want to install more software and write cool programs?**

First, update the APT package manager, and you'll probably want to install Pip3, which installs modules for Python 3.

```
sudo apt update
sudo apt install python3-pip
```

Then you can install lots of fun stuff.

```
sudo pip3 install RPi.GPIO
```

**How do I control pins on the Raspberry Pi?**

Here's an example Python 3 script that sets a pin high.

<pre class="code">import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(16, GPIO.OUT)   # like pinMode(16, OUTPUT)
GPIO.output(16, GPIO.HIGH) # like digitalWrite(16, HIGH)
</pre>

Here's another script that checks the state of a pin.

<pre class="code">import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(16, GPIO.IN)       # like pinMode(16, INPUT)
while(1):                     # do this forever
    if(GPIO.input(16)):       # like digitalRead(16)
        print("Pin is high.")
    else:
        print("Pin is low.")
    time.sleep(0.5)           # sleep for 0.5 s
</pre>

**What if I want to control pins through a web browser?**

Try using the Flask web framework:

<pre class="code">from flask import Flask
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/pinon')
def pin_on():
    GPIO.setup(16, GPIO.OUT)   # pinMode(16, OUTPUT)
    GPIO.output(16, GPIO.HIGH) # digitalWrite(16, HIGH)
    return 'I turned on the pin.'

# Make sure the line below has the correct angle brackets in it.
@app.route('/digital/write/<pin_name>/<state>')
def digital_write(pin_name, state):
    pin = int(pin_name)
    if state.upper() in ['1', 'ON', 'HIGH']:
        GPIO.setup(pin, GPIO.OUT)   # pinMode(pin_name, OUTPUT)
        GPIO.output(pin, GPIO.HIGH) # digitalWrite(pin_name, HIGH)
        return 'Set pin {0} to HIGH'.format(pin_name)
    elif state.upper() in ['0', 'OFF', 'LOW']:
        GPIO.setup(pin, GPIO.OUT)   # pinMode(pin_name, OUTPUT)
        GPIO.output(pin, GPIO.LOW)  # digitalWrite(pin_name, LOW)
        return 'Set pin {0} to LOW'.format(pin_name)
    return 'Something went wrong'
</pre>

You also need to install [Flask](https://pypi.org/project/Flask/) for this to work.

**Wait, how do I install Flask?**

```
sudo pip3 install flask
```

Then, start the server (assuming your code is in a file called `server.py`):

```
export FLASK_APP=server.py
python3 -m flask run --host=0.0.0.0
```

By default, Flask will listen on port 5000, so check `http://your.rpi.ip.address:5000` to see if it worked.

**That's cool, but how do I get Flask to start itself when the Pi boots?**

For that, you want to install [Supervisor](http://supervisord.org).

<pre class="code">sudo apt-get install supervisor
</pre>

Check that Supervisor is installed properly and running.

<pre class="code">pi@raspberrypi:~$ sudo supervisorctl
supervisor> status
supervisor> exit
</pre>

Tell supervisor that you want it to run Flask for you by adding something like the lines below to `/etc/supervisor/supervisord.conf`

<pre class="code">[program:flask]
directory=/home/pi
environment=FLASK_APP="server.py"
command=python -m flask run --host=0.0.0.0
</pre>

Then, make Supervisor read the config file.

<pre class="code">sudo supervisorctl
supervisor> update flask
flask: stopped
flask: updated process group
supervisor> status
flask                            RUNNING   pid 14183, uptime 0:00:09
</pre>

If Supervisor can't start Flask for whatever reason, it will write error messages in the log files, which you can find in `/var/log/supervisor/`. In general, it's probably a better idea to debug your Flask code pretty thoroughly before you start using Supervisor, but if bugs come up, the log files are your best hope. You can also just stop Flask under Supervisor and going back to running Flask from the console yourself.

**What do the pin numbers correspond to?**

All the most recent Pi's share a standard pin format. Below is a handy guide. [This site](https://pinout.xyz/) is also an excellent resource for reference.

<p align="center">
  <img src="/img/raspberry-pi-pinout.png" />
</p>
