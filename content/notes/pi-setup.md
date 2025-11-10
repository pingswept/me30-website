---
title: "Class 19: Raspberry Pi setup"
draft: false
---

## Raspberry Pi setup

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_krkfenre&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_rqh2illx" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

{{< hint danger >}}
**Video omission**

Warning! The video above leaves out the step explained below where you enable SSH and set the password. If you get to the login prompt successfully, but the (obsolete) default password doesn't work, that's probably why.
{{< /hint >}}

## Stuff you need (all in your kit)

* Raspberry Pi 4
* micro SD card
* USB-C power supply
* USB-serial adapter, AKA a console cable

You may also need a USB card reader, if you don't have a card slot built into your computer. We have extra adapters that you can borrow to write data to your SD card if needed.

To connect the console cable, look at this diagram.

![RPi console cable connection](/img/rpi-console-cable.png)

There are more details about the console cable if you need them in [Adafruit's console cable tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview). If you want to go deeper on how console cables and terminals work, try the [Sparkfun tutorial](https://learn.sparkfun.com/tutorials/terminal-basics/all).

## Setup checklist 1: "Image" the OS to the SD card

<ul style="list-style: none;">
  <li><input type="checkbox"> Install the Raspberry Pi Imager from <a href="https://www.raspberrypi.com/software/">the Raspberry Pi Software page</a></li>
  <li><input type="checkbox"> Plug your microSD card into your computer.</li>
  <li><input type="checkbox"> In the Imager, set "Raspberry Pi Device" to "Raspberry Pi 4".</li>
  <li><input type="checkbox"> Choose the image "Raspberry Pi OS (other)" --> "Raspberry Pi OS Lite (64-bit)"</li>
  <li><input type="checkbox"> Set "Storage" to be your microSD card. You can identify it by its size, which is probably 32 GB.
  <li><input type="checkbox"> Click "Next" and then "Edit Settings" in the "Use OS Customisation?" pop-up.
  <li><input type="checkbox"> In the "General" tab, set the username as <code>pi</code> and set the password to <code>ME30</code>.</li>
  <li><input type="checkbox"> Also in the "General" tab, check the "Configure wireless LAN" box and set the SSID to "Tufts_Wireless."</li>
  <li><input type="checkbox"> In the "Services" tab, enable SSH. <code>pi</code></li>
  <li><input type="checkbox"> <b>The moment of truth!</b> Erase the card and write the new OS to the card.
  <li><input type="checkbox"> Edit config.txt on the microSD card to include on the last line: <code>enable_uart=1</code></li>
</ul>

## Setup checklist 2: Connect to your Pi via serial console cable, and find out your Pi's MAC address

### Mac laptops

<ul style="list-style: none;">
  <li><input type="checkbox"> Connect the Pi to your laptop with the console cable</li>
  <li><input type="checkbox"> Put the microSD card in slot of Pi</li>
  <li><input type="checkbox"> Open Applications > Utilities > Terminal (macOS)</li>
  <li><input type="checkbox"> In Terminal, run <code>ls /dev</code> and find the entry that says <code>tty.usbserial-XXYYZZ</code>.</li> 
  <li><input type="checkbox"> Record the numbers you see instead of XXYYZZ. Then run <code>screen /dev/tty.usbserial-XXYYZZ 115200</code> </li>
  <li><input type="checkbox"> Connect USB-C power cable. Wait a minute or so for the Pi to boot up</li>
  <li><input type="checkbox"> Log in with the username <code>pi</code> and password you set using the Imager </li>
  <li><input type="checkbox"> To figure out the Pi's MAC address, type the command <code>ifconfig</code>. Be sure you get the MAC for <code>wlan0</code>, not <code>eth0</code>. As shown in the screenshot below, the MAC address is something like <code>e4:5f:01:3b:33:fb</code> and appears after the word <code>ether</code>.</li>
</ul>

### PC/Windows laptops

<ul style="list-style: none;">
  <li><input type="checkbox"> Install the <a href="https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads">SiLabs CP210X USB driver</a> for the console cable. (You won't need this on a newish Mac.)</li>
  <li><input type="checkbox"> Connect the Pi to your laptop with the console cable</li>
  <li><input type="checkbox"> Put the microSD card in slot of Pi</li>
  <li><input type="checkbox"> Install <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">PuTTY</a> (Windows)</li>
  <li><input type="checkbox"> Use Device Manager to determine what COM port your serial cable is communicating with</li>
  <li><input type="checkbox"> In PuTTY, start a serial session at 115200 bps to the Pi</li>
  <li><input type="checkbox"> Connect USB-C power cable. Wait a minute or so for the Pi to boot up</li>
  <li><input type="checkbox"> Log in with the username <code>pi</code> and password you set using the Imager</li>
  <li><input type="checkbox"> To figure out the Pi's MAC address, type the command <code>ifconfig</code>. Be sure you get the MAC for <code>wlan0</code>, not <code>eth0</code>. As shown in the screenshot below, the MAC address is something like <code>e4:5f:01:3b:33:fb</code> and appears after the word <code>ether</code>.</li>
</ul>


![MAC address screenshot](/img/finding-mac-address.jpg)

## Set-up checklist 3: Get your Pi on IP address on Tufts_Wireless

<ul style="list-style: none;">
  <li><input type="checkbox"> Register that MAC address with Tufts IT at <a href="https://access.tufts.edu/manual-non-browser-device-registration">the Tufts registration page.</a> If using Chrome, you'll probably need to use an Incognito window </li>
  <li><input type="checkbox"> Wait a few minutes for MAC address permissions to propagate to local wireless access point</li>
  <li><input type="checkbox"> Use the `ifconfig` or `hostname -I` command to find the IP address assigned to your Pi by Tufts_Wireless.</li>
  <li><input type="checkbox"> Type `logout` to disconnect your Terminal from your Pi so that you can switch to logging in via SSH.</li>
</ul>

![IP address screenshot](/img/finding-ip-address.jpg)


## Set-up checklist 4: Connect to your Pi via SSH instead of serial

Once you have your Pi connected to the wireless network, you can log into it through SSH instead of through a USB-serial cable. 
- Have your Pi's IP address handy (do that when still connected by serial cable; use the `ifconfig` or `hostname -I` command).
- Make sure your Pi is plugged into power. Do not attach the serial console cable.
- Open a new terminal window.
- Type `ssh your_Pi_username@ip_address_of_your_Pi`
- You should be prompted for your Pi's password, and then you should be logged in!  No serial cable necessary!


## Setup for Tufts_Secure

**Not needed if your Pi is already connected to Tufts_Wireless**

Use the Nano text editor (opened within the Terminal window) to edit the file at **/etc/wpa_supplicant/wpa_supplicant.conf.** 

- To open this file in the Nano text editor, type the command <code>sudo nano /etc/wpa_supplicant/wpa_supplicant.conf</code> into the Terminal window where you've logged into your Pi.
- The <code>sudo</code> part sets you as a "super user" with permission to edit the file. Add the text from the gray box below - with the password inserted - to the wpa_supplicant.conf file.
- Ask an instructor or LA or friend for the Nolop_IOT password; we try to avoid publishing passwords on the internet.
- The purpose of the text below is to tell your Raspberry Pi to log into the Tufts_Secure network under the username "Nolop_IOT," which the Tufts IT department created just for class purposes like this one. It is okay for many users to be logged in under this Tufts_Secure account.
- After you've edited the wpa_supplicant.conf file, when you next boot up your Pi, it should log in to Tufts_Secure and be given an IP address. Type `hostname -I` to print the IP address of your Pi.

### Network settings for Tufts_Secure

```
network={
    ssid="Tufts_Secure"
    key_mgmt=WPA-EAP
    pairwise=CCMP
    eap=PEAP
    identity="Nolop_IOT"
    password="YOU PUT THE PASSWORD HERE IN QUOTES"
    phase2="auth=MSCHAPV2"
}
```


## What the Imager should look like

![Raspberry Pi Imager OS selection](/img/pi-imager-os-selection.png)

## The OS customization options you should pick

Make sure you set the password for the user `pi`. You should probably write it down somewhere else too.

You should also enable SSH, but you could also do that later with the command <code>sudo raspi-config</code>.

![Raspberry Pi Imager options](/img/pi-imager-options.png)


## FAQ

### **How do I turn off my Pi?**

Type the command `sudo shutdown`


### **What if I forgot to choose Tufts_Wireless as my network when I imaged my SD card?**

<ul style="list-style: none;">
  <li><input type="checkbox"> Follow checklist 2 above to log into your Pi with a serial console cable.
  <li><input type="checkbox"> Type the command <code>sudo raspi-config</code> to list Tufts_Wireless as the network.</li>
  <li><input type="checkbox"> In <code>raspi-config</code>, pick <code>System Options > Wireless LAN</code></li>
  <li><input type="checkbox"> Enter <code>Tufts_Wireless</code> for the SSID and leave the passphrase blank. Exit raspi-config. </li>
</ul>

### **Is there a way to change my login password when I'm already logged in to my Pi?**

You can change some of your Pi's settings, including its password, with the Raspi-Config application. To run it, type the command `sudo raspi-config`

### **What operating system should I use on my Pi?**

Unless you have a good reason not to, you should start with the Lite version of Raspberry Pi OS. The Raspberry Pi imager will download it for you. Previously called Raspbian, the OS should be based on Debian Buster or newer (as older versions will not work with a Pi 4).

### **How do I figure out what name is assigned to the USB-serial adapter when I plug it in?**

On Windows 10, it's usually `COM3` (but it is not uncommon to have a different number). You can check for sure in the Device Manager control panel under Ports (COM & LPT)

On macOS, it's called `/dev/tty.usbserial-123456`, but the numbers at the end change. You can check it by running `ls /dev` in Terminal.

On Linux it's called `/dev/ttyACM0`, but the number will depend on how many USB devices are plugged in. As with macOS, you can check by running `ls /dev` in Terminal.

### **When I open config.txt with Notepad, the lines all run together. How do I fix this?**

Use a better text editor, like [Sublime Text](https://www.sublimetext.com/), [Textmate](https://macromates.com/), or [Notepad++](https://notepad-plus-plus.org/). You could also try Wordpad.

### **What do the pin numbers correspond to?**

All the most recent Pi's share a standard pin format. Below is a handy guide. [This site](https://pinout.xyz/) is also an excellent resource for reference.

![RPi pinout](/img/raspberry-pi-pinout.png)

Tutorials from the Raspberry Pi Foundation on using the GPIO pins:

https://projects.raspberrypi.org/en/projects/physical-computing/1
