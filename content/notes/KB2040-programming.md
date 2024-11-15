---
title: "KB2040 programming"
draft: false
---
## Programming your KB2040 microcontroller

- - -

## Set-up procedure

### Stuff you need

*   A computer, plus the admin password to install software
*   An Adafruit KB2040 microcontroller board
*   A USB-C **data** cable with the right ends to connect the KB2040 to your computer

## Hardware setup

### Step 1: plug in your KB2040 to your computer

The next step is to plug in your KB2040 to your computer with a USB data cable. When you plug it in, you should see a green light on the board near the USB C jack, showing that the KB2040 is getting electricity. **Make sure to use a data cable, not just a power cable!**

Once the board powers up, it's time to load CircuitPython onto it.

### Step 2: download CircuitPython to your laptop

To your computer, [download](https://circuitpython.org/board/adafruit_kb2040/) the latest version of CircuitPython for the KB2040. Putting CircuitPython on your computer is an intermediate step. You are not going to run CircuitPython onto your computer - your eventual goal is to get CircuitPython onto your KB2040.

### Step 3: enter bootloader mode

Enter the "bootloader" mode on your KB2040 by **holding down the BOOT (boot select) button as you press and release the RST (reset) button. Continue to hold down the BOOT button until the KB2040's bootloader drive appears as "RPI-RP2" on your computer**. You need your KB2040 board in bootloader mode to install or update Circuit Python.

### Step 4: copy CircuitPython onto your KB2040

Find the CircuitPython file that you downloaded onto your computer. Drag that file to the KB2040's boot drive (the **RPI-RP2** drive).

### Step 5: be patient

Watch for **RPI-RP2** to disappear and a new drive to appear on your computer called **CIRCUITPY**. When you see the **CIRCUITPY** drive, you know that your KB2040 now has CircuitPython installed on it, and it is ready to receive, store, and execute Python files. Congratulations!

![The CIRCUITPY drive](/img/circuitpy_drive.png)

The steps above are adapted from Adafruit's CircuitPython tutorial. You can find more details at https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython.

## Software setup

Before you can actually make a microcontroller do anything, you have to install a code editor on your computer. We'll use the Mu Editor, which works well with Adafruit CircuitPython boards, including the KB2040. 

To install the Mu Editor, [download it](https://codewith.mu/en/) from the Mu website. 

You're on your own for the actual installation, but it consists of pressing "OK" and "Next" and things like that a few times. Adafruit's CircuitPython tutorial provides step-by-step instructions for installing Mu here: https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

Your goal is to see something like the image below on your screen.

![The Mu Editor](/img/Mu_blankeditor.png)

The first time you run Mu, you'll need to select its "mode." Choose "CircuitPython."

![Selecting the Mu mode](/img/Mu_mode.png)

## Make the software talk to the hardware

### Load a Python program onto your KB2040.

The next step is to load your first Python program onto your KB2040.

With CircuitPython installed, your KB2040 will look for and execute any Python program named **code.py** that is saved in the **CIRCUITPY** drive. Your KB2040 will do this on its own every time it starts up or resets. Every time the contents of the **code.py** file are changed, the KB2040 is triggered to reset -- and therefore to execute the updated code. You do not need to manually run the new code.

You can save code files with other file  names, besides **code.py**, on your KB2040's CIRCUITPY drive, but they won't be executed by your KB2040. You will need to change their name to **code.py** in order for them to be run.

To create and load your first program, follow these steps:
1. Open the Mu editor.
2. Click the Load button, find the **CIRCUITPY** drive, and choose **code.py**.
3. Copy and paste this code into the Mu editor

<pre class="code">
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
</pre>

![First code.py on Mu](/img/firstcode.png)

To load it onto the KB2040, click the "Save" button in the Mu editor's top menu. Navigate to the **CIRCUITPY** drive and save the file as **code.py.**

![Saving code.py](/img/save-code-py.png)

As the code is uploaded, you might see the green power LED flash rapidly for a moment. 

After the code is saved on the KB2040, if you wire an external LED from pin D4 to the GND pin, you should see it blinking once per second.

If you've made it this far, your hardware and software are working properly. Congratulations! Go get a drink of cool, delicious water!

## Alternative KB2040 programming tutorials

Adafruit's [CircuitPython Tutorials](https://learn.adafruit.com/welcome-to-circuitpython) are great if you're new to this stuff. Please take the time to run through them; it's an investment worth making. Microcontrollers are not going away soon.

## When stuff goes wrong

The most common problem with microcontrollers is difficulty communicating between the computer and the microcontroller. You might see messages like "Circuit Python device not connected."

In this case, you should hold down the BOOTSEL button while pressing and releasing the RESET button, to make sure your computer sees the KB2040's CIRCUITPY drive.

You can also try unplugging the KB2040 and plugging it in again and restarting the Mu Editor. 

Make sure you are using a cable that can transfer data, not just power. This is the most common source of trouble.

## So, how do I make this "code" you mention?

Start by exploring the CircuitPython tutorial provided by Adafruit, starting at the page [Exploring Your First CircuitPython Progarm](https://learn.adafruit.com/welcome-to-circuitpython/exploring-your-first-circuitpython-program) and working through the next several pages.

Learn the [basics of Python syntax](https://www.w3schools.com/python/python_syntax.asp) at the easy-to-follow Python W3 Schools website.

Then review and bookmark the [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials) page from Adafruit.

- - -

## Using Mu to run code on your KB2040

Save your Python code as the file code.py on your KB2040, and it will start running immediately.  

Open the serial monitor in Mu to see any error messages.

To interrupt your KB2040 and stop the code, click within the Serial  monitor, and use CTRL-C.

To return the KB2040 to running the code, use CTRL-D in the serial monitor.

## Things to know about Python syntax

- In Python, a line break (new line) indicates a new command. You might have seen other programming languages use semicolons or parentheses.
- In Python, indentation (space at the beginning of a line) is very important! To indicate nested or sub-section blocks of code (e.g., of a loop or function), you must use indentation from the left edge of the screen. Python uses whitespace (indentation amount) to determine “scope” — that is, to figure out what blocks of code define other code, or belong within a higher level of code.
- Use the # symbol to indicate the start of a comment (indicate that certain text is documentation of your code, rather than a command).

<pre class="code">
# Python interprets this line as a comment.
print(“Hello ME 30!”)
</pre>

## Python variables

Create a variable by assigning a value to it. Python will automatically determine what type of variable it is (e.g., an integer, a decimal, a string) based on its initial assignment.

<pre class="code">
x = 30
y = 30.0
address = “200 Boston Ave.”
</pre>

Python has no command for simply declaring the existence of a variable.

## How to see text output by a Python program

You’ll need to open the serial monitor in the Mu editor.

- - -

## A few exciting commands in some CircuitPython-specific libraries

Here are some Python commands that you might want to start with. To use all but the print() command, you need to start your Python code by importing the libraries specified below (TIME, BOARD, DIGITALIO, PWMIO, ANALOGIO).

### Print Commands

**print(<variable>)**: Prints the value of whatever variable is listed inside the ().

**print(“[string]”)**: Prints exactly the text included inside the (“ “)

To see the text generated by print(), be sure the serial monitor in your Mu Editor is open.

**print(([variable],))**:  With the extra parentheses and comma, creates a “tuple” (a pair of values) that the Mu editor will show on its x-y plotter

To see the points generated by print(([var],)), be sure the plotter in Mu is open.

### TIME library

To use this command, include the command “import time” at the start of your code.

**time.sleep(N)**: do nothing for N seconds

**time.monotonic()**: returns the current time in seconds, related to some unknown reference time


### BOARD and DIGITALIO library

To use these commands, include the command “import board” and “import digitalio” at the start of your code.

**dir(board)**: spits out the names of the all the pins available on your KB2040

**xyz = digitalio.DigitalInOut(board.[pin name or number])**: calls up the digitalio library and creates a new object called xyz that will hold information about a specific pin on a microcontroller board.  The pin names and numbers are on the board’s pinout diagram, e.g, D6, D5, LED, etc.

**xyz.direction = digitalio.Direction.OUTPUT**: tells the KB2040 to treat the pin for object xyz as a voltage output, not an input

**xyz.direction = digitalio.Direction.INPUT**: tells the KB2040 to treat the pin for object xyz as a voltage input

**xyz.value**: the voltage value at the pin for object xyz

**xyz.value = 1**: sets the voltage at the pin for xyz to be “high.” For the KB2040, that's 3.3 V
    
**xyz.value = True**: another way to set the voltage high

**xyz.value = 0** sets the voltage for the digital variable xyz to be “low,” i.e., ground or 0 V
    
**xyz.value = False**: another way to set the voltage low

Here's an example of how you might use commands from the **board** and **digitalio** libraries to set the voltage at pin D4 high (True), then low (False), and repeat.

<pre class="code">
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
</pre>



### PWMIO library for motor speed control

To use these commands, include the command “import pwmio” at the start of your code.

**xyz = pwmio.PWMOut(board.[pin name or number], frequency =[initial PWM frequency], duty_cycle=[initial PWM duty cycle])**

creates a new object called “xyz” that will hold all the information about sending out pulse-width modulation at a particular pin 

**xyz.duty_cycle = 32000**
    
at whatever KB2040 pin belongs to the PWM object xyz, changes the duty cycle of the PWM voltage to 32000.  For the RP2040 chip on the KB2040, the duty cycle maximum is 65535; max duty cycle means the output is high 100% of the time.
 
**What is the difference between *frequency* and *duty cycle* in PWM?**
- Frequency: This CircuitPython parameter refers to the number of motor control cycles (voltage pulse initiations) per second
Set this to 500 for the KB2040, because its main processing chip can handle outputting that many cycles per second.
- Duty_cycle: This CircuitPython parameter refers to the duration of time within one motor control cycle at which the voltage is ON or HIGH (i.e., 3.3 V).

For the KB2040, a duty cycle value of 65536 corresponds to the voltage being turned on for 100% of the cycle, which means the motor gets 100% of the voltage available to it.

Because 50% of 65536 is about 32800, a duty cycle of about 32800 corresponds to the voltage being set high for 50% of the cycle, or the motor getting about 50% of the voltage available to it. The motor will spin at half speed.

A duty cycle of about 6500 corresponds to the voltage being set high for 10% of the cycle, or the motor getting about 10% of the voltage available to it.  The motor would spin at 10% speed IF that is enough voltage to overcome its internal friction (you’ll probably find that it’s not enough voltage for the motor to turn at all).

Here is some sample CircuitPython code that uses PWM to run a motor first at full speed, then at half speed, and then at quarter speed. Note that we have to import the pwmio library to run this code, and we have to initiate a pin as a pwmio.PWMOut pin.

<pre class="code">
import board
import pwmio
import time

my_control_pin = pwmio.PWMOut(board.D6, frequency=500, duty_cycle=0)
# creates a new object called “my_control_pin” that will hold all 
    # the information about sending out 
    # pulse-width modulation at pin D6

while True:
    my_control_pin.duty_cycle = 65535
    time.sleep(3)
    my_control_pin.duty_cycle = 32800
    time.sleep(3)
    my_control_pin.duty_cycle = 16400
    time.sleep(3)
</pre>



### ANALOGIO library

**xyz = analogio.AnalogIn(board.A1)**: creates an object called xyz and connects xyz to A1 as an analog input.

The code below will plot the value of the voltage coming in at analog input pin A1.

<pre class="code">
import time
import analogio
import board

inputvoltage = analogio.AnalogIn(board.A1)

while True:
    print((inputvoltage.value,))
    time.sleep(0.1)
</pre>
    
## Sensors
    
If you want to program more specialized devices like stepper motors or particular sensors, you may need to download additional CircuitPython libraries (that don't come with CircuitPython uf2 file itself) onto your KB2040. You can learn about how that works at the Welcome to CircuitPython libraries [page](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)

The full set of CircuitPython libraries for the KB2040 can be downloaded [here](https://circuitpython.org/libraries).

**NOTE:** We recommend downloading the entire bundle to your **laptop,** and then transferring ONLY the libraries you need to your KB2040. Transferring the entire bundle to your KB2040 will take quite a long time.
    
For distance sensor reading, check out [this page](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython) to see what libraries you need.

## Stepper Motors

For stepper motor control, you'll need the **adafruit_motor library** (and two H-bridges). All CircuitPython libraries for the KB2040 can be downloaded [here](https://circuitpython.org/libraries). Download the entire library bundle to your **laptop,** and then transfer ONLY the libraries you need to your KB2040. 

You can find helpful stepper motor wiring diagrams [here](https://lastminuteengineers.com/stepper-motor-l298n-arduino-tutorial/).
    
{{< expand "Click to see some stepper motor code" "..." >}}
<pre class="code">
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Use this example for digital pin control of a motor driver with two H-bridges
# which you can make on two breadboards or find pre-made on a L298N PCB.
# This code uses the adafruit_motor library, available for download at
# https://circuitpython.org/libraries

import time
import board
import digitalio
from adafruit_motor import stepper

# Set DELAY as the length of time that the motor runs for each step. Adafruit suggests 0.01, but ME 30 folks have found this delay value needs to be much shorter. If 0.01 doesn't work, try something as short as 0.005.

DELAY = 0.01

# Set the number of steps for one rotation of the motor. For the stepper motor in the ME 30 kit, one rotation takes 200 steps.

STEPS = 200

# You can use any available GPIO pin on a microcontroller.
# The following pins are simply a suggestion. If you use different pins, 
# update the following code to use your chosen pins.

coils = (
    digitalio.DigitalInOut(board.D4),  # A1
    digitalio.DigitalInOut(board.D5),  # A2
    digitalio.DigitalInOut(board.D6),  # B1
    digitalio.DigitalInOut(board.D7),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
    
# The next line is essential. It creates an 
# object, 'motor' (you can name it anything)
# to hold the details about your stepper motor wiring. 
# It uses the stepper command from the adafruit_motor library.

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

# The for loop below represents just one approach to taking a step. 
# For more info on the arguments for the 'onestep' command, see 
# the "Stepper Motors" section of this page: 
# https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing/circuitpython

for step in range(STEPS):
    motor.onestep()
    time.sleep(DELAY)

motor.release()

</pre>
{{< /expand >}}


    
## State Machine Code

Often when using a microcontroller within a electromechanical system, you need to be able to check for the state of inputs while also running motors, lights, and other actuators. Writing code for "state machines" is a useful technique for this situation. Below is code that shows one way to set up state machines in CircuitPython.     

This code carries out these two tasks at once:

1. flash one LED, 3 seconds on, 3 seconds off.
2. constantly check for a button press that sets an input pin HIGH.
3. flash a *different* LED when the button is pressed.


{{< expand "Click to see the state machine code" "..." >}}
<pre class="code">

# This purpose of this code is to carry out two tasks at once:
# 1. Repeatedly flash a green LED, 3 seconds on, 3 seconds off.
# 2. Constantly check for a button press that sets an input pin HIGH.
# and flash a *different* LED when the button is pressed.

import board
import digitalio as dio
import time

led_green = dio.DigitalInOut(board.D4)
led_green.direction = dio.Direction.OUTPUT

led_red = dio.DigitalInOut(board.D5)
led_red.direction = dio.Direction.OUTPUT
    
button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

STATE_TOGGLE = 1       # these are just arbitrary constants used to number the states
STATE_CHECK_BUTTON = 2 # the values 1 and 2 are not significant

state = STATE_TOGGLE
next_toggle = 0
led_1.value = False

while True:
    if state is STATE_TOGGLE:
        if led_green.value is True:
            led_green.value = False
        else:
            led_green.value = True
        next_toggle = time.monotonic() + 3.0 # this is like setting a timer to expire 3 seconds in the future
        state = STATE_CHECK_BUTTON
    elif state is STATE_CHECK_BUTTON:
        if button.value is True:
            led_red.value = True
        else:
            led_red.value = False
        if time.monotonic() > next_toggle:
            state = STATE_TOGGLE
</pre>
{{< /expand >}}



    
## CircuitPython Reference Pages
If you want to check the details of these functions or see what else is available, the canonical reference is [the CircuitPython Essentials page](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials). 



