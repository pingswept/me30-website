---
title: "Class 10: KB2040 challenges"
draft: false
---

## KB2040 challenges

## Resource: 1-page summary of basic CircuitPython commands: 

https://tufts.box.com/s/lczswqulqewphbxyku1zpvazp73govzi

### Challenges Set 1

1. Make your KB2040 flash an external LED so there are 2 flashes per second, controlled by pin D5.
2. Make your KB2040 send the text, "I, for one, welcome our new insect overlords." to your serial monitor once per second.[^1]
3. Use a 10k resistor to pull pin D5 "high" or "low" (i.e., physically toggle between attaching it to either 3.3 V or 0 V, through a resistor). Print out the pin's state as "HIGH" or "LOW" on the serial monitor every time it changes.
4. Make an LED on D6 mirror the state of D5, controlled by the 10k resistor as in the previous challenge.
5. Make an LED attached to pin D6 send Morse code for "TUFTS".
6. Turn your gearmotor on for 5 seconds, then off for 5 seconds, then repeat, using pin D6. You'll need a transistor for this.

### KB2040 + H-bridge challenge
Use an H-bridge circuit to make your gearmotor spin clockwise for 5 seconds, then counterclockwise for 5 seconds, using pins D5 and D6.

### Challenges Set 2

7. Make your gearmotor slowly increase in speed for 5 seconds, then slowly decrease in speed for 5 seconds, then repeat, using pin D6.
8. Use your potentiometer to make a variable voltage. Read the voltage with pin A0, then print the voltage (in volts) to the serial monitor.
9. Use your potentiometer on pin A0 to control the speed of your gearmotor on pin D6.
10. Use a resistor in series with your photoresistor to make a voltage that changes with light exposure. Use that voltage to control the speed of your gearmotor on pin D6.
11. Use a pushbutton on pin D5 to control when your motor is on and off, using D6 for motor control.


### Solutions for Set 1

{{< expand "See the schematic diagrams for 1 to 6" "..." >}}

![Schematics for challenges 1 to 6](/img/challenge-schematic-1-6.jpg)

{{< /expand >}}


{{< expand "See breadboard wiring sketches for 1 to 6" "..." >}}

![Schematics for challenges 1 to 6](/img/challenge-wiring-1-6.jpg)

{{< /expand >}}


{{< expand "See CircuitPython code for 1 to 6" "..." >}}

```python
###############################

#Challenge 1

import digitalio
import time
import board

led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.25)
    led.value = False
    time.sleep(0.25)

###############################

#Challenge 2

import time

while True:
    print("I, for one, welcome our new insect overlords.")
    time.sleep(1)

###############################

#Challenge 3

import digitalio
import time
import board

pin5 = digitalio.DigitalInOut(board.D5)
pin5.direction = digitalio.Direction.INPUT

while True:
    if pin5.value is True:
        print("HIGH")
    else:
        print("LOW")
    time.sleep(0.01)

###############################

#Challenge 4

import digitalio
import time
import board

pin5 = digitalio.DigitalInOut(board.D5)
pin5.direction = digitalio.Direction.INPUT

pin6 = digitalio.DigitalInOut(board.D6)
pin6.direction = digitalio.Direction.OUTPUT

while True:
    if pin5.value is True:
        pin6.value = True
    else:
        pin6.value = False
    time.sleep(0.01)

#alternate method
    # pin6.value = pin5.value
    #time.sleep(0.01)

###############################

#Challenge 6

import digitalio
import time
import board

gate = digitalio.DigitalInOut(board.D6)
gate.direction = digitalio.Direction.OUTPUT

while True:
    gate.value = True
    time.sleep(5)
    gate.value = False
    time.sleep(5)

###############################

#H-bridge Challenge

import digitalio
import time
import board

diagonal1 = digitalio.DigitalInOut(board.D5)
diagonal1.direction = digitalio.Direction.OUTPUT

diagonal2 = digitalio.DigitalInOut(board.D6)
diagonal2.direction = digitalio.Direction.OUTPUT

while True:
    diagonal1.value = False
    diagonal2.value = True
    time.sleep(5)

    diagonal2.value = False
    diagonal1.value = True
    time.sleep(5)

###############################

```

{{< /expand >}}


### Solutions for H-bridge and Set 2

{{< expand "See the schematic diagrams for Set 2" "..." >}}

![Schematic for challenges 8 to 11](/img/challenge-schematic-8-11.jpg)

{{< /expand >}}


{{< expand "See breadboard wiring sketches for H-Bridge and Set 2" "..." >}}

![Schematics for challenges 8 to 10](/img/challenge-wiring-8-10.jpg)
![Schematics for challenges 11 and H-bridge](/img/challenge-wiring-11-hbridge.jpg)


{{< /expand >}}


{{< expand "See CircuitPython code for H-bridge and Set 2" "..." >}}
###############################

#H-bridge Challenge

import digitalio
import time
import board

diagonal1 = digitalio.DigitalInOut(board.D5)
diagonal1.direction = digitalio.Direction.OUTPUT

diagonal2 = digitalio.DigitalInOut(board.D6)
diagonal2.direction = digitalio.Direction.OUTPUT

while True:
    diagonal1.value = False
    diagonal2.value = True
    time.sleep(5)

    diagonal2.value = False
    diagonal1.value = True
    time.sleep(5)

###############################

#Challenge 7

import time
import board
import pwmio

gate = pwmio.PWMOut(board.D9, frequency=500, duty_cycle=0)

i = 1
# declaring a counter variable

while True:
    while i < 51:
        gate.duty_cycle = int(65535*(i/50))
        print(gate.duty_cycle)
        # int command converts decimal to integer
        # for PWM on the KB2040, 65535 means 100% pulse width
        time.sleep(0.1)
        # choosing 0.1 sec as the duration for each motor speed level
        # if each speed level lasts for 0.1 sec, we need 50 levels to
        # last for 5 seconds
        i = i+1
        print(i)
    i = 50
    while i > 0:
        gate.duty_cycle = int(65535*(i/50))
        time.sleep(0.1)
        i = i-1

###############################

#Challenge 8

import time
import board
import analogio

inputvoltage = analogio.AnalogIn(board.A0)

while True:
    print((inputvoltage.value,))
    time.sleep(0.1)

###############################

#Challenges 9 & 10

import time
import board
import analogio
import pwmio

gate = pwmio.PWMOut(board.D6, frequency=500, duty_cycle=0)

inputvoltage = analogio.AnalogIn(board.A0)
MAX_VOLTAGE = 1000
# this max value determined experimentally
# by testing input sensor in challenge 8

while True:
    print((inputvoltage.value,))
    gate.duty_cycle = int(65535*(inputvoltage.value/MAX_VOLTAGE))
    # for PWM on the KB2040, 65535 means 100% pulse width
    time.sleep(0.1)

###############################

#Challenge 11

import digitalio
import time
import board

button = digitalio.DigitalInOut(board.D5)
button.direction = digitalio.Direction.INPUT

gate = digitalio.DigitalInOut(board.D6)
gate.direction = digitalio.Direction.OUTPUT

while True:
    print(button.value)
    gate.value = button.value
    time.sleep(0.1)

###############################




{{< /expand >}}


[^1]: If you're like Kristen and didn't get this cultural reference, here's an explanation: https://knowyourmeme.com/memes/i-for-one-welcome-our-new-insect-overlords
