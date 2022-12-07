---
title: "Servers and clients"
draft: false
---
## Servers and clients

A server is a program that listens for requests from clients. When it receives requests, it replies to them.

A client is a program that makes requests of servers.

## Implementation on microcontrollers

There are zillions of ways to write servers and clients-- lots of different programming languages, architectures, and libraries you could use. But, to narrow things down a little bit, here are a few places to start with the Raspberry Pi.

![server-client architecture options](/img/Client-server-table.jpeg)


### Raspberry Pi server

![Pi as server set up](/img/Pi-as-server.jpeg)

For code, try writing a function that executes if a specific HTTP request is made, like the `/senddata/` example below. 

```python
from flask import Flask
app = Flask(__name__)

import gpiozero
from gpiozero import DistanceSensor

# Waits for an HTTP request ending in "senddata"
@app.route('/senddata')
def send_data():
    # echo and trigger of the sensor are connected to GPIO pins 23 and 24
    ultrasonic = DistanceSensor(echo=23, trigger=24)
    reading = int(ultrasonic.distance)
    # returns to the client the value of the variable <reading>
    return 'sensor reading is {0}'.format(reading)
 ```   
    
For more details, see the [Flask example on our Raspberry Pi setup page](http://andnowforelectronics.com/notes/rpi-setup/#what-if-i-want-to-control-pins-through-a-web-browser-flask).


### Raspberry Pi client

![Pi-as-client set up](/img/Pi-as-client.jpeg)

For code, try using the Python library called [Requests](https://requests.readthedocs.io/en/master/).

You can install it with: `sudo pip3 install requests`

Your code might start like this:

```
import requests
reply = requests.get('http://192.168.1.123:5000/sensor/reading')
print(reply.text)
```

### Demo videos showing some client/server setup

Check them out [here](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup)
