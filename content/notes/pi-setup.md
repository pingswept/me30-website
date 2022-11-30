---
title: "Raspberry Pi setup"
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

There are more details if you need them in [Adafruit's console cable tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview). Emily K. also recommends the [Sparkfun tutorial](https://learn.sparkfun.com/tutorials/terminal-basics/all).

## Setup checklist

<ul style="list-style: none;">
  <li><input type="checkbox"> Install the Raspberry Pi Imager from <a href="https://www.raspberrypi.com/software/">the Raspberry Pi Software page</a></li>
  <li><input type="checkbox"> In the Imager, choose the image "Raspberry Pi OS (other)" --> "Raspberry Pi OS Lite (32-bit)"</li>
  <li><input type="checkbox"> Click the gear menu for Advanced Options to enable SSH and set the password for the user <code>pi</code></li>
  <li><input type="checkbox"> Edit config.txt on micro SD card to include: <code>enable_uart=1</code></li>
    <li><input type="checkbox"> Install the <a href="https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads">SiLabs CP210X USB driver</a> for the console cable</li>
  <li><input type="checkbox"> Connect RPi to laptop with console cable</li>
  <li><input type="checkbox"> Put micro SD card in slot of Pi</li>
  <li><input type="checkbox"> Install <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">PuTTY</a> (Windows) or open Applications > Utilities > Terminal (macOS) or install <a href="https://www.decisivetactics.com/products/serial/">Serial</a> (macOS)</li>
  <li><input type="checkbox"> (macOS only) In Terminal, run <code>ls /dev</code> and find the entry that says <code>tty.usbserial-XXYYZZ</code>. Record the numbers you see instead of XXYYZZ. Then run <code>screen /dev/tty.usbserial-XXYYZ 115200</code>) </li>
  <li><input type="checkbox"> (macOS only) If using Serial instead of Terminal, simply open Serial and double click on the USB-serial device that appears</li> 
  <li><input type="checkbox"> (Windows only) In PuTTY, start a serial session at 115200 bps to the Pi</li>
  <li><input type="checkbox"> Connect USB-C power cable. Wait a minute or so for the Pi to boot up</li>
  <li><input type="checkbox"> Log in with username <code>pi</code> and password you set using the Imager</li>
  <li><input type="checkbox"> Run <code>sudo raspi-config</code> to set up your wireless connection</li>
</ul>

## What the Imager should look like

The gear menu doesn't appear until after you choose the Raspberry Pi OS Lite (32-bit) image.

![Raspberry Pi Imager OS selection](/img/pi-imager-with-gear-menu.png)

## The advanced options you should pick

Enable SSH and set the password for the user `pi`.

![Raspberry Pi Imager advanced options](/img/pi-imager-advanced-options.png)

## Checklist for Tufts_Wireless

<ul style="list-style: none;">
  <li><input type="checkbox"> Figure out the Pi's MAC address with <code>ifconfig</code>. Be sure you get the MAC for <code>wlan0</code>, not <code>eth0</code>.</li>
  <li><input type="checkbox"> Register that MAC address with Tufts IT at <a href="http://hostreg.net.tufts.edu/">the Tufts registration page. If using Chrome, you'll probably need to use an Incognito window </a></li>
  <li><input type="checkbox"> Wait a few minutes for MAC address permissions to propagate to local wireless access point</li>
  <li><input type="checkbox"> If you did not use `sudo raspi-config` to list Tufts_Wireless as the network, then add the network settings below to <code>/etc/wpa_supplicant/wpa_supplicant.conf</code></li>
  <li><input type="checkbox"> Reboot Pi</li>
</ul>


### Network settings for Tufts_Wireless
```
network={
    ssid="Tufts_Wireless"
    key_mgmt=NONE
}
```

## Setup for Tufts_Secure

There's a bug in `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant` in the current version of Raspbian OS (based on Debian 10.4, Buster). This post explains how to fix it, but we haven't verified that it works yet: https://medium.com/@iced_burn/raspberry-pi-connected-to-wifi-of-wpa2-enterprise-ddd5a40c0b07

{{< hint danger >}} Read the note above about the bug in `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant`. {{< /hint >}}

The LA's can tell you the Nolop_IOT password; we try to avoid publishing passwords on the internet.

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

### Connecting to your Pi via SSH instead of serial

Once you have your Pi connected to the wireless network, and you use ifconfig to find the IP address it has been assigned, you can log into it through SSH instead of through a USB-serial cable. 
- Have your Pi's IP address handy.
- Make sure your Pi is plugged into power. Do not attach the serial console cable.
- Open a new terminal window.
- Type `ssh your_Pi_username@ip_address_of_your_Pi`
- You should be prompted for your Pi's password, and then you should be logged in!  No serial cable necessary!

## FAQ

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
