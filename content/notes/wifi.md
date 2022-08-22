---
title: "Wifi"
draft: false
---

## Wifi at Tufts

Network details from IT wizard Dave DeChellis. Thanks, Dave!


### Tufts_Guest

* Meant for short time visitors to the University – no password but a click-through AUP must be “read” and accepted
* All IP addresses are not visible to the rest of the campus (for security reasons) and sent out a separate ISP connection through one of our providers
* Rate-limiting also in place for clients 

### Tufts_Wireless

* Tied to the Tufts Host Registration system for MAC address-based authentication
* Considered an open SSID since there is no PSK or Tufts Username authentication
* No over-the-air encryption; packets in the clear
* Meant for IOT-esque “stuff” – Google Home, Sonos, etc
* There is a single subnet for these devices on each campus, which allows a device on Tufts_Wireless to find another device on Tufts_Wireless – perfect for upnp and other “consumer” grade devices
* RFC1918 space on campus, NAT-ed to the Internet

### Tufts_Secure

* Based on Tufts username and password for authentication (talks to Active Directory backend domain controllers through our Radius infrastructure)
* Over the air 802.1X encryption
* Uses DHCP pooling to accommodate the 15-20k concurrent users on the service on each campus
* MDNS and some multicast is shared between these subnets to allow for device discovery but we have found limitations such as upnp – Google chromecasts and Apple AirPlay seem to work
* RFC1918 space on campus – NAT-ed to the Internet
