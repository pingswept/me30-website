---
title: "Servers and clients"
draft: false
---
## Servers and clients

A server is a program that listens for requests from clients. When it receives requests, it replies to them.

A client is a program that makes requests of servers.

## Implementation on microcontrollers

There are zillions of ways to write servers and clients-- lots of different programming languages, architectures, and libraries you could use. But, to narrow things down a little bit, here are a few places to start with the Raspberry Pi and Arduino.

### Arduino MKR Wifi 1010 server

Example code for [WiFiNINA WiFiWebServer](https://www.arduino.cc/en/Tutorial/LibraryExamples/WiFiNINAWiFiWebServer)

### Arduino MKR Wifi 1010 client

Example code for [WiFiNINAWiFi WebClient](https://www.arduino.cc/en/Tutorial/LibraryExamples/WiFiNINAWiFiWebClient)

### Raspberry Pi server

See the [Flask example on our Raspberry Pi setup page](http://andnowforelectronics.com/notes/rpi-setup/#what-if-i-want-to-control-pins-through-a-web-browser-flask).

### Raspberry Pi client

Try using the Python library called [Requests](https://requests.readthedocs.io/en/master/).

You can install it with: `sudo pip3 install requests`

Your code might start like this:

```
import requests
reply = requests.get('http://192.168.1.123/sensor/reading')
print(reply.text)
```
![server-client architecture](/img/server-client-architecture.jpg)
