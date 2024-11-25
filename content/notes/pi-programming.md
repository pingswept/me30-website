---
title: "Raspberry Pi programming"
draft: false
---

## Raspberry Pi programming

### **What if I want to install more software and write cool programs?**

First, update the APT package manager, and you'll probably want to install PIP, which installs modules for Python 3.

```
sudo apt update
sudo apt install python3-pip
```

Then you can install lots of fun stuff.

```
sudo pip install RPi.GPIO
```

If you get an error when you try to install GPIO using PIP, try using APT instead: 

`sudo apt install python3-rpi.gpio` 

### **How do I write, edit, and save pieces of code on my Raspberry Pi?**  
**nano text editor**

First, you might want to create a new directory (i.e., folder) to store all the code you write. If you are writing Python scripts, you could call your new directory `python-scripts.`  Use the commands `pwd` (print working directory) and `cd` (change directory) to see the current directory and to switch to a different one if needed. Once you are in the `/home/pi` directory, create a new directory to store your scripts. Use the `mkdir` (make directory) command for this.  

```
pi@raspberry:~ $ pwd
/home/pi
pi@raspberry:~ $ mkdir python-scripts
pi@raspberry:~ $ cd python-scripts
pi@raspberry:~/python-scripts $
pi@raspberry:~ $ pwd
/home/pi/python-scripts
```

Next, you may want a text editor that runs in your terminal window to write, edit, and save your scripts. You can use `nano`, which comes pre-installed in the Rasperry Pi OS. To run it, type `nano` in the terminal window once you are logged into your Raspberry Pi.  Within `nano`, use Control-O to save a file ("Writing Out" = saving) and Control-R to open a file ("Reading" = opening).   

![nano window](/img/nano-editor.png)

### **What other useful commands might I need to know?**

* `ls`: list what's in a directory
* `cd`: change to a different directory. `cd ..` goes up one level of the directory tree.
* `sudo`: execute a command as a superuser
* `cat`: print out the contents of a file
* `<tab>`: try to autocomplete the command I am typing
* `<ctrl>c`: interrupt the command in process
* `sudo shutdown`: turn off the Pi

### **What about some more obscure commands that could be useful?**

* `hostname -I`: print the IP address of my Pi
* `which`: show which program gets executed by a command
* `grep`: search a file for a string of text, like `grep "Flask" server.py"`
* `|`: pipe the results of one command into another, like `cat server.py | grep "Flask"`
* `uname -a`: tell me what version of the Linux kernel I am running
* `netstat -plut`: list what programs are listening on what ports
* `wget`: download a file from the internet
* `curl`: read the contents of a file on the internet as text
* `ping`: send a packet to an IP address to see if it's working
* `nmap`: scan a network for IP addresses in use `sudo apt install nmap` first)
* `ps -aux`: list all the processes running
* `top`: show a live list of running programs (q to quit)
* `dig`: look up the IP address of a domain name (`sudo apt install dnsutils` first)

There's even more stuff at [linuxcommandlibrary.com](https://linuxcommandlibrary.com/basics.html)

### **What is something else that you want to mention, but can't quite figure out where to mention it?**

Ah, that would be the crucial difference between Python and Python 3. You should use the commands `python3` and `pip3` exclusively. If you switch to, for example, just `python`, you will find that it will run, but none of the modules that you installed for Python 3 will show up.

You may think to yourself, couldn't I just make `python` into a shortcut for `python3`? You could, but lots of software depends on Python and will fail if executed with the Python 3 interpreter. Unfortunately, the name `python` is probably used up for eternity.

### **How do I control pins on the Raspberry Pi?**

Here's an example Python 3 script that sets a pin high.

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(16, GPIO.OUT)   # like digitalio.DigitalInOut(board.D16)
                            # and digitalio.Direction.OUTPUT
GPIO.output(16, GPIO.HIGH) # like setting digitalio.value = True
```
You can save this as a file and then run it with `python3 name-of-the-file.py`, or you can paste in each line at a Python prompt if you want to play around with it.

Here's another script that checks the state of a pin.

```python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(16, GPIO.IN)       # like digitalio.DigitalInOut(board.D16)
                                # and digitalio.Direction.INPUT

while True:                     # do this forever
    if(GPIO.input(16)):       # like checking digitalio.value
        print("Pin is high.")
    else:
        print("Pin is low.")
    time.sleep(0.5)           # sleep for 0.5 s
```

The script below sets up pin 16's internal pulldown resistor so its default state is ground. Then it checks its value.

```python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Now set pin 16 as input and tie its internal resistor as pulldown
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)       

while True:                     # do this forever
    if(GPIO.input(16)):       # like checking digitalio.value
        print("Pin is high.")
    else:
        print("Pin is low.")
    time.sleep(0.5)           # sleep for 0.5 s
```

### **What about PWM?**

The RPi.GPIO module in Python allows you to vary the output to a pin using PWM. Make sure you choose a pin that is enabled for PWM. On the Pi 4, those pins are 12, 32, 33, and 35, but you can check the [Raspberry Pi pinout diagram](https://pinout.xyz/pinout/pwm) to be sure.


```python

# This code is adapted from SourceForge: https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pin = GPIO.PWM(12, 500)  # channel=12; frequency=500Hz
pin.start(0)            # initializes the duty cycle at 0; (0.0 <= duty cycle <= 100.0)

while True:
    pin.ChangeDutyCycle(25)  # changes the duty cycle to 25% (quarter power)
    time.sleep(3)
    pin.ChangeDutyCycle(50)  # changes the duty cycle to 50% (half power)
    time.sleep(3)
    pin.ChangeDutyCycle(100) # changes the duty cycle to 100% (full power)
    time.sleep(3)

```

### **What if I want to control pins through a web browser?**

Try using the Flask web framework.   

First, you need to install [Flask](https://pypi.org/project/Flask/) onto your Pi for this to work.

**Wait, how do I install Flask?**

```
sudo pip3 install flask
```

or

```
sudo apt install python3-flask
```

**What kind of Python script should I create?**

To create a server, you can use the python script below. It uses Flask to take input from a web browser and then uses that input to set a Raspberry Pi pin either HIGH or LOW. You could create this script and save it as server.py.

```python
from flask import Flask
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/pinon')
def pin_on():
    GPIO.setup(16, GPIO.OUT)   # like digitalio.DigitalInOut(board.D16)
                                # and digitalio.Direction.OUTPUT
    GPIO.output(16, GPIO.HIGH) # like setting digitalio.value = True
    return 'I turned on the pin.'

# Below, we take input from a web browser and channel it to GPIO pin.
# app.route refers to your Pi's IP address, which you'll type into
# a web browser URL line when you want to control this code.
# For example, to set pin 16 on your Pi to HIGH, you'll type
# [your Pi IP address]/digital/write/16/HIGH into your web browser. 
# Make sure the line below has the correct angle brackets in it.

@app.route('/digital/write/<pin_name>/<state>')
def digital_write(pin_name, state):
    pin = int(pin_name)
    if state.upper() in ['1', 'ON', 'HIGH']:
        GPIO.setup(pin, GPIO.OUT)   # make the pin an output
        GPIO.output(pin, GPIO.HIGH) # turn the pin on
        return 'Set pin {0} to HIGH'.format(pin_name)
    elif state.upper() in ['0', 'OFF', 'LOW']:
        GPIO.setup(pin, GPIO.OUT)   # make the pin an output 
        GPIO.output(pin, GPIO.LOW)  # turn the pin off
        return 'Set pin {0} to LOW'.format(pin_name)
    return 'Something went wrong'
```

**How do I get this Python script to run as a server on the internet?**

Finally (assuming you've installed Flask in your Pi), start the server by typing the commands below (into your Terminal, assuming you are logged into your Pi). We're assuming your code is in a file on your Pi called `server.py`. The `--host=0.0.0.0` in the command below means that your Flask instance (on your Pi) will listen on whatever IP addresses it has, instead of just for connections from itself, which is the default for testing. 

```
export FLASK_APP=server.py
python3 -m flask run --host=0.0.0.0
```

By default, Flask will listen on port 5000, so check `http://your.rpi.ip.address:5000` to see if it worked.

### **That's cool, but how do I get Flask to start itself when the Pi boots?**

If you are logged in to your Pi remotely via SSH, you can just type in the commands above to start Flask and run a python script within it. But if you want Flask to start itself automatically when the Pi boots, then you'll want to install [Supervisor](http://supervisord.org).

```
sudo apt install supervisor
```

Check that Supervisor is installed properly and running.

```
pi@raspberrypi:~$ sudo supervisorctl
supervisor> status
supervisor> exit
```

Tell supervisor that you want it to run Flask for you by adding something like the lines below to `/etc/supervisor/supervisord.conf` (You'll need to change directories to go up to the highest level directory on your Pi. Once you get to the /etc/supervisor directory, use `sudo nano` to open and edit the file.)

```
[program:flask]
directory=/home/pi
environment=FLASK_APP="server.py"
command=python3 -m flask run --host=0.0.0.0
```

Then, make Supervisor read the config file.

```
sudo supervisorctl
supervisor> update flask
flask: stopped
flask: updated process group
supervisor> status
flask                            RUNNING   pid 14183, uptime 0:00:09
```

If Supervisor can't start Flask for whatever reason, it will write error messages in the log files, which you can find in `/var/log/supervisor/`. In general, it's probably a better idea to debug your Flask code pretty thoroughly before you start using Supervisor, but if bugs come up, the log files are your best hope. You can also just stop Flask under Supervisor and going back to running Flask from the console yourself.

### **What if I want to make web page buttons that send GET HTTP requests?**

Brought to us by a session with ChatGPT, below is a simple HTML page with JavaScript that includes a button. When the button is pressed, it triggers a GET request to the specified URL (the IP address of a Raspberry Pi, which you should replace with your Pi's IP address).

(Here's the prompt we gave to ChatGPT: *Please write a webpage made of HTML and Javascript that has a big button in the middle that issues a GET request to http://10.247.10.22/drivefast when I press the button.*)

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Drive Fast Button</title>
</head>
<body>
  <div style="text-align: center; margin-top: 50px;">
    <button onclick="issueGetRequest()">Drive Fast</button>
  </div>
  <script>
    function issueGetRequest() {
      // Create a new XMLHttpRequest object
      var xhr = new XMLHttpRequest();
      // Define the GET request and the target URL
      xhr.open("GET", "http://10.247.10.22/drivefast", true);

      // Set up a callback function to handle the response
      xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
          // You can handle the response here if needed
          console.log("GET request successful");
        }
      };
      // Send the GET request
      xhr.send();
    }
  </script>
</body>
</html>
```

ChatGPT also tells us: *Save this code in an HTML file, and when you open it in a web browser, you'll see a button labeled "Drive Fast." Clicking this button will trigger a GET request to the specified URL (`http://10.247.10.22/drivefast`). The console will log "GET request successful" if the request is successful. Note that if the target server doesn't allow cross-origin requests, you might need to handle CORS (Cross-Origin Resource Sharing) accordingly.*
