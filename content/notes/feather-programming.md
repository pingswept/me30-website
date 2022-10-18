---
title: "Feather programming"
draft: false
---
## Programming your Feather RP2040 microcontroller


## Stuff You Need

*   A computer, plus the admin password to install software
*   An Adafruit Feather RP2040
*   A USB-C cable with the right ends to connect the Feather to the computer


## Software check 

Before you can actually make a Feather do anything, you have to install a code editor on your computer. We'll use the Mu Editor, which works well with Adafruit CircuitPython boards, including the Feather. 

To install the Mu Editor, [download it](https://codewith.mu/en/) from the Mu website. 

You're on your own for the actual installation, but it consists of pressing "OK" and "Next" and things like that a few times. Adafruit's CircuitPython tutorial provides step-by-step instructions for installing Mu here: https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

Your goal is to see something like the image below on your screen.

![The Mu Editor](/img/Mu_blankeditor.png)

The first time you run Mu, you'll need to select its "mode." Choose "CircuitPython."

![Selecting the Mu mode](/img/Mu_mode.png)

## Hardware check 

### Plug in your Feather to your computer

The next step is to plug in your Feather to your computer with a USB data cable. When you plug it in, you should see a  light on the board near the number 13, showing that the Feather is getting electricity. **Make sure to use a data cable, not just a power cable!**

### Install CircuitPython on your Feather

Once the board powers up, it's time to load CircuitPython onto it. 

To install CircuitPython on your Feather, follow the basic steps below. These steps are adapted from Adafruit's CircuitPython tutorial. You can find more details at https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython.

1. To your computer, [download](https://circuitpython.org/board/adafruit_feather_rp2040/) the latest version of CircuitPython for the Feather RP2040. Putting CircuitPython on your computer is an intermediate step. You are not going to run CircuitPython onto your computer - your eventual goal is to get CircuitPython onto your Feather.
2. Enter the "bootloader" mode on your Feather by **holding down the BOOTSEL button as you press and release the RESET button. Continue to hold down the BOOTSEL button until the Feather's bootloader drive appears as "RPI-RP2" on your computer** (to which the Feather is plugged in). You need your Feather board in bootloader mode to install or update Circuit Python.
3. Find the CircuitPython file that you downloaded onto your computer. Drag that file to the Feather's boot drive (the **RPI-RP2** drive).
4. Watch for the Feather's light to flash again and for **RPI-RP2** to disappear, and for a new drive to appear on your computer called **CIRCUITPY**.
5. When you see the **CIRCUITPY** drive, you know that your Feather now has CircuitPython installed on it, and it is ready to receive, store, and execute Python files. Congratulations!

![The CIRCUITPY drive](/img/circuitpy_drive.png)


### Load a Python program onto your Feather.

The next step is to load your first Python program onto your Feather.

With CircuitPython installed, your Feather will look for and execute any Python program named **code.py** that is saved in the **CIRCUITPY** drive. Your Feather will do this on its own every time it starts up or resets. Every time the contents of the **code.py** file are changed, the Feather is triggered to reset -- and therefore to execute the updated code. You do not need to manually run the new code.

You can save code files with other file  names, besides **code.py**, on your Feather's CIRCUITPY drive, but they won't be executed by your Feather. You will need to change their name to **code.py** in order for them to be run.

To create and load your first Feather program, follow these steps:
1. Open the Mu editor.
2. Click the Load button, find the **CIRCUITPY** drive, and choose **code.py**.
3. Copy and paste this code into the Mu editor 

<pre class="code">
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
</pre>

![First code.py on Mu](/img/firstcode.png)

To load it onto the Feather, click the "Save" button in the Mu editor's top menu. Navigate to the **CIRCUITPY** drive and save the file as **code.py.**

![Saving code.py](/img/save-code-py.png)

As the code is uploaded, you'll see the larger circular LED on the Feather board flash rapidly green for a moment. 

After the code is saved on the Feather, you should see the on-board red LED blinking once per second.

If you've made it this far, your hardware and software are working properly. Congratulations! Go get a drink of cool, delicious water!

## Alternative Feather programming tutorials

Adafruit's [CircuitPython Tutorials](https://learn.adafruit.com/welcome-to-circuitpython) are great if you're new to this stuff. Please take the time to run through them; it's an investment worth making. Microcontrollers are not going away soon.

## When stuff goes wrong

The most common problem with microcontrollers is difficulty communicating between the computer and the microcontroller. You might see messages like "Circuit Python device not connected."

In this case, you should hold down the BOOTSEL button while pressing and releasing the RESET button, to make sure your computer sees the Feather's CIRCUITPY drive.

You can also try unplugging the Feather and plugging it in again and restarting the Mu Editor. 


## So, how do I make this "code" you mention?

Start by exploring the CircuitPython tutorial provided by Adafruit, starting at the page [Exploring Your First CircuitPython Progarm](https://learn.adafruit.com/welcome-to-circuitpython/exploring-your-first-circuitpython-program) and working through the next several pages.

Learn the [basics of Python syntax](https://www.w3schools.com/python/python_syntax.asp) at the easy-to-follow Python W3 Schools website.

Then review and bookmark the [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials) page from Adafruit.

- - -

## Using Mu to run code on your Feather

Save your Python code as the file code.py on your Feather, and it will start running immediately.  

To interrupt your Feather and stop the code, open the Mu Serial monitor, click within the Serial  monitor, and use CTRL-C.

To return the Feather to running the code, use CTRL-D in the serial monitor.

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

## A few exciting commands in some CircuitPython-specific libraries

Here are some Python commands that you might want to start with. To use all but the print() command, you need to start your Python code by importing the libraries specified below (TIME, BOARD, DIGITALIO, PWMIO, ANALOGIO).

**print(<variable>)**: Prints the value of whatever variable is listed inside the ().

**print(“[string]”)**: Prints exactly the text included inside the (“ “)

To see the text generated by print(), be sure the serial monitor in your Mu Editor is open.

**print(([variable],))**:  With the extra parentheses and comma, creates a “tuple” (a pair of values) that the Mu editor will show on its x-y plotter

To see the points generated by print(([var],)), be sure the plotter in Mu is open.

### TIME library

To use this command, include the command “import time” at the start of your code.

**time.sleep(N)**: do nothing for N seconds

### BOARD and DIGITALIO library

To use these commands, include the command “import board” and “import digitalio” at the start of your code.

**dir(board)**: spits out the names of the all the pins available on your Feather

**xyz = digitalio.DigitalInOut(board.[pin name or number])**: calls up the digitalio library and creates a new object called xyz that will hold information about a specific pin on a microcontroller board.  The pin names and numbers are on the board’s pinout diagram, e.g, D6, D5, LED, etc.

**xyz.direction = digitalio.Direction.OUTPUT**: tells the Feather to treat the pin for object xyz as a voltage output, not an input

**xyz.direction = digitalio.Direction.INPUT**: tells the Feather to treat the pin for object xyz as a voltage input

**xyz.value**: the voltage value at the pin for object xyz

**xyz.value = 1**: sets the voltage at the pin for xyz to be “high.” For the Feather, that's 3.3 V
    
**xyz.value = True**: another way to set the voltage high

**xyz.value = 0** sets the voltage for the digital variable xyz to be “low,” i.e., ground or 0 V
    
**xyz.value = False**: another way to set the voltage low

### PWMIO library

To use these commands, include the command “import pwmio” at the start of your code.

**xyz = pwmio.PWMOut(board.[pin name or number], frequency =[initial PWM frequency], duty_cycle=[initial PWM duty cycle])**

creates a new object called “xyz” that will hold all the information about sending out pulse-width modulation at a particular pin 

**xyz.duty_cycle = 32000**
    
at whatever Feather pin belongs to the PWM object xyz, changes the duty cycle of the PWM voltage to 32000.  For the RP2040 chip on the Feather, the duty cycle maximum is 65535; max duty cycle means the output is high 100% of the time.

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


If you want to check the details of these functions or see what else is available, the canonical reference is [the CircuitPython Essentials page](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials). 



