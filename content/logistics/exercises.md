---
title: "Exercises"
draft: false
---
# In-class exercises

## 1: Project #0: Power an LED with "wall" power (Sep. 6)

This is a warm-up activity to power an LED with "wall" power through our DC power supply and control it with a push button. 

Your goal is to create a circuit on your breadboard that lights up an LED with power from the wall, directed through your kit's DC power supply. This circuit should have the following characteristics:

- It is implemented on a breadboard.
- It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
- It turns on an LED when a push button is pressed.

The components are:

1. DC power supply
2. One power (barrel) jack
3. One LED
4. One resistor (What size? See [these notes](http://andnowforelectronics.com/notes/resistors/#typical-application-current-limiter).)
5. One pushbutton
6. Various wires and a breadboard

The image below is a circuit diagram representation of what you're building.

![Wall-powered LED circuit](/img/project0_circuit.png)

{{< hint danger >}}
**Important note: the pins on the power jack are weird! More details below.**

There's a cryptic diagram in the [datasheet](http://andnowforelectronics.com/notes/datasheets/) for the PJ-102AH power jack, shown below.

![power jack pinout](/img/power-jack-pinout.jpg)

One part is obvious: the pin in the middle is connected to pin 1.

But what is that little arrow/bump thing with pins 2 and 3?

That's trying to tell you that when the jack is empty (i.e. no plug inserted), pins 2 and 3 are connected together. When you insert the plug, the barrel pushes on the bump at the end of the pin 2 contact, which bends it away from the pin 3 arrow, breaking the connection to pin 3. It's so that you can detect whether there's a plug inserted or not, which can be useful for battery-powered systems. You don't need to implement that feature on your regulator board; you can just use pins 1 and 2.
{{< /hint >}}

*For an extension to this exercise, re-arrange your circuit so you have one LED that stays on permanently and another that is powered by the button.*


## 2. Build voltage dividers (Sep. 8)

![Voltage dividers](/img/voltage-dividers-2022.png)



## 3: Build a voltage regulation circuit (Sep. 13)

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors


## 4. Motor power supply PCB with indicator LED (Sep. 20)

The goal of this exercise is to give you more practice with Kicad while also demonstrating how one might use the PCB you've been working on for Project 1.

Imagine you've received your breadboard power supply PCB (project 1) back from OSH Park, and you've soldered on all of the components. You plug it into one end of your breadboard. With it plugged in, you have one of your positive breadboard rails powered at 5 V, the other positive rail powered at 3.3 V, and a screw terminal powered at 12 V.

Now we'll design a second PCB that will plug into the other end of your breadboard. Let's call this a motor power supply.

**In this exercise, your task is to design the PCB layout for this new board in Kicad so that it works with your P1 PCB.**

Today's new PCB has two functions:

1. It lights an LED to show when 5 V is available on your breadboard, and 
2. When you push a button, it runs a motor at 12 V, through a screw terminal. 

Pretend that you've already created a breadboard prototype of this motor power supply PCB.  A schematic diagram for your motor power supply shows that it's really just two simple circuits:

![Motor supply schematic](/img/motorsupply-PCB.jpg)

Your new PCB should include the following components:
* 2 screw terminals
* some header pins
* 1 LED
* 1 resistor
* 1 push button

Shared doc for posting your work and questions:
https://docs.google.com/document/d/1ONtsG_-AVNehNyhWbaVRlC9eLj0BGLUVzQcgiZofu24/edit?usp=sharing


## 5. Control a motor with a BJT (Sep. 27)

Making a motor spin is pretty simple: apply sufficient voltage across its leads. When we want to control things like motors (or LEDs, buzzers, etc.) electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off a motor.

You need 4 things:

1. A 5 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. A DC gear motor
4. An appropriately-sized current-limiting resistor for the BJT

The picture below shows the concept of what you're building. In place of the 24 V source, we'll use your 12 V source.

![Typical BJT circuit](/img/typical-bjt-circuit.png)


## 5.5 Determine pin voltages and ideal resistor value for a BJT circuit (Sep. 29)

1. Fill in the table below to indicate the voltage at E, B, and C when the input is (a) at ground and (b) at 3.3 V.
2. What is an ideal value for the current-limiting resistor?


|  | V_E  | V_B   | V_C |
|:----:|:-----:|:----:|:----:|
|  Input at O V   |    |   |     |
|  Input at 3.3 V   |    |   |     |


## 6. Control a motor with a MOSFET (Sep. 29)

You've used a bipolar junction transistor to control a motor. Now try using the other main class of transistor: a metal oxide semiconductor field effect transistor, or MOSFET.  The main difference between the [two types of transistors](http://andnowforelectronics.com/notes/low-power-high-power/) is that BJTs are current-controlled, and MOSFETs are voltage-controlled.

You need 5 things:

1. 3.3 V voltage source, which you can make using the 3.3V regulator in your kit
2. 12 V voltage source
3. An N-channel MOSFET
4. A DC gear motor
5. A pull-down resistor for the MOSFET

![MOSFET circuit](/img/mosfet-controller.jpg)

## 7. H-bridge circuit analysis, part 1 (Oct. 4)

You've just wired up the top left corner of an H-bridge circuit using a P-channel MOSFET. You connect the other motor lead to ground so that you can test this corner before wiring up the transistors at any other corners.  If this corner is wired correctly, what should happen to the motor when the MOSFET gate is connected:

- to 12 V?  
- to ground?  

Sketch the current path for each of those gate states.

![Top left corner of an H-bridge](/img/Hbridge-corner.png)

Now you add a BJT as a different method for switching on the P-channel MOSFET. Again, you want to test this corner before moving on to other sections of the H-bridge. If the BJT and P-channel MOSFET in this corner are wired correctly, what should happen to the motor when the BJT base is:

- at 3.3 V?  
- at ground?  

Sketch the current path for each of those base states.

![add BJT to corner of an H-bridge](/img/Hbridge-corner-BJT.jpg)


## 7. H-bridge circuit analysis, part 2 (Oct. 4)

Please click the link below to view and analyze a full H-bridge circuit, with BJT controllers for the P-channel MOSFETs. This analysis will help you know what to expect and how to test your own full H-bridge prototype.

https://tufts.qualtrics.com/jfe/form/SV_086kK9vBZbSdqqG


**This H-bridge circuit has four inputs, shown at locations 1, 2, 3, and 4. Each input turns a transistor on or off.**

![H-bridge inputs not set](/img/Hbridgeplain.jpeg)

*Question #1: What should be the state of each input to turn the motor ON? It doesn't matter what direction it spins.* 

{{< expand "See the answer" "..." >}}
To spin the motor in one direction, put corners 1 and 3 at 3.3 V while corners 2 and 4 are at ground (0 V). To reverse directions, do the opposite - put corners 2 and 4 at 3.3 V while corners 1 and 3 are at ground. The upper corners turn "on" when their BJT transistors are set to 3.3 V because when the BJT is "on" and current can flow across it, the gate (G) of the P-channel MOSFET has a direct connection to ground. When the gate (G) of a P-channel is at a lower voltage than its source (S), it turns "on" and allows current to flow across the source-drain pathway.  If the diagonal bottom N-channel MOSFET is also allowing current to flow, then the circuit now has a pathway for current to flow from 12 V, across the motor, and to ground. 
{{< /expand >}}


*Question #2: What should be the state of each input to turn the motor OFF?*

{{< expand "See the answer" "..." >}}
The top corners (1 and 4) need to both be set to ground to block current flow to the motor. But it's a good idea to set everything to ground when you want the motor to be off.
{{< /expand >}}


*Question #3: If all four switches were connected to 3.3 V (as shown below), what would happen and why?*  

![H-bridge inputs all at 3.3 V](/img/Hbridge_all3v.jpeg)

{{< expand "See the answer" "..." >}}
**Don't do this -  it will short the circuit!!** In this H-bridge, setting a corner input to 3.3 V turns that corner's MOSFET "on," allowing current to across the source-drain pathway. If all 4 MOSFETs are allowing current to flow, then this circuit's easiest path to ground will be down the two sides of the "H."  No current will flow through the highly resistive motor. The motor will not spin, and the rest of the circuit will get very hot.
{{< /expand >}}

## 8. Measure a DC gearmotor (Power In) (Oct. 6)

Here are a few basic measurements you can make to understand your DC gearmotor better. The overall goal is to determine the efficiency of the motor by comparing the electrical power that goes into it ("power in") with the mechanical power it delivers ("power out"). 

We'll start with determing the minimum and maximum current that the motor draws.

1. When your motor is stalled (like if you're trying to lift something too heavy with it), it behaves like a resistor. This is when your motor draws maximum current, so checking the resistance is a good way to estimate the maximum current for whatever drive voltage you choose. Using the resistance-measuring setting of your multimeter (the omega symbol, Ω, represents ohms), measure the resistance of the coils of your motor.
2. Make your DC gearmotor spin by connecting your motor directly to your 12 V DC power supply using alligator clips. Then, measure the current the motor draws with no load attached by putting your multimeter in series with the motor. You should switch your multimeter to the A setting (for Amps), and move the red lead to the port on the left side of the meter that is labeled "A". The black lead stays in the black port labeled "COM".

With measurement #1 above (the resistance of the coils), you can estimate the **maximum current** the motor will draw at any voltage. With measurement #2, you can find the **minimum current at 12 V**. 

When you know the current and the voltage, you can multiply them to find the electrical power going into the motor.

If you can estimate how much power a task will require, you can start to figure out what voltage this motor would need to deliver that power (assuming perfect efficiency, for now). That's the first step toward deciding whether this is the right motor for whatever you're building.

## 9. Measure a DC gearmotor (Power Out) (Oct. 6)

The next step is to determine how much mechanical power the motor actually delivers ("power out"). One way to do this is to measure the time it takes to perform a certain amount of work (i.e., to add energy to a system).

1. Use tape and string to hang a water bottle from your motor shaft.
2. Measure the time it takes your motor to lift around 0.5 kg of water 0.5 m. Compute the amount of work done in lifting the water. With these two values, you can find "power out."
3. Compare "power in" and "power out" to estimate the motor's efficiency.

Post your group's results here: https://docs.google.com/spreadsheets/d/1hPOLsmSsdGBHga9NMayhIXqW0E7COHThiejLpnPMqj8/edit?usp=sharing


## 10. Test the current limit of your P1 PCB, plus P2 Q & A (Oct. 11)

The voltage regulators on your P1 PCB are specified (on their data sheets) to be able to handle current at the level of 1.5 A (the 5V regulator) and 0.8 A (the 3.3 V regulator). But the question is - **once soldered into your P1 PCB, can they still perform up to their specified max current limit?**  

**Test your P1 PCB by determining how much current your regulators can actually send out to loads at your output pins before going into thermal shutdown.**

General procedure (details left to your group):
- Determine the resistance (it will be a low value!) you should attach to your 3.3 V and 5 V output so that something close to the specified max current is drawn (0.8 A or 1.5 A, respectively)
- Attach those low-ohm resistors to the output. These resistors stand in for a motor or other load to which you would want to supply 3.3 V or 5 V
- Monitor the voltage drop across that resistive load - that is, the voltage drop between the output of the regulator and ground
- Once that voltage drop begins to decrease lower than 3.3 V or 5 V, your regulator has gone into thermal shutdown (you may feel the regulators getting very hot before this happens)

Use this shared doc to post questions about the P1 PCB test and about P2 circuit board design:

https://docs.google.com/document/d/1atNNbe8rjqZZtX7Foj0LWxPWZwktrCwlViqzWgFVHoU/edit?usp=sharing


## 11. Feather challenges (Oct. 18 and 20)

Learn to program your Feather by working through these 10 challenges. You'll want to consult the [Feather programming](http://andnowforelectronics.com/notes/feather-programming/) resources.

http://andnowforelectronics.com/notes/feather-challenges/

## 12. Project 2.5 motor hub testing (Oct. 25)

Form a group of ~8 students. Using water bottles and a scale, create a set of 8 different weights ranging from the weight of an empty bottle to the weight of a full bottle. (Yes, each group of 8 will have a different set of 8 weights, but as long as you have a range, your group will be able to do this activity.)

For each motor hub, begin with the lowest weight and attach it to the hub with a paper clip (through the hole placed ~15 mm from the shaft axis) and a length of string. Supply 12 V to the motor and see if it can lift the weight without slipping of the hub. If it succeeds, move on to the next highest weight. Repeat until you get to a weight that either stalls the motor or makes the hub slip around the motor shaft.  Record this as your "slip/stall weight." 

Multiply your hub's "slip/stall weight" by the distance between your shaft axis and your paper clip attachment point (it should be 15 mm, but measure just to be sure).  The results is your "slip/stall torque."

Take a photo of your motor hub attachment. Place it on the class histogram in the column find that corresponds approximately to your slip/stall torque.
https://docs.google.com/spreadsheets/d/1Y_V_8rgQhnSgg5z3wRCmGc2mLD-aFtRIoKs-uJ67k6A/edit?usp=sharing

## 13. Recognizing common errors in Feather Challenge #7 (Oct. 27)

Challenge #7 asks you to control a motor's on/off state with a Feather output pin. Below are two approaches to setting up the circuitry. Each has problems that will prevent it from working correctly. What do you think those problems are?

![Feather challenge 7 problems](/img/challenge7.png)

*What are the problems with approach #1?*

{{< expand "See the answer" "..." >}}
(a) The Feather GND pin is not tied to the same ground as the motor circuitry.

(b) There is no current-limiting resistor between the Feather output and the BJT base. We want to keep the current through the base-emitter diode to about 10% of the collector-to-emitter current. If the motor is drawing 150 mA, then we want the base-emitter current to be about 15 mA. And we know that when the BJT is on, its base voltage is 0.6 V. Since the Feather output supplies 3.3 V, we need a resistor to drop the voltage by 2.7 V and limit the current to 15 mA.
{{< /expand >}}

*What are the problems with approach #2?*

{{< expand "See the answer" "..." >}}
(a) The motor is "below" the N-channel MOSFET. When the gate is supplied with voltage, **for a very brief moment** the gate voltage will be higher than the source voltage, and current will flow from drain to source and therefore through the motor.  But once current starts to be drawn through the motor, the voltage at the source will rise to somewhere near 12 V. At this point, the gate voltage of 3.3 V will be less than the source voltage, and the MOSFET will no longer allow current flow to the motor.

(b) The MOSFET gate does not have a pull-down resistor to ground.

(c) The Feather GND pin is not tied to the same ground as the motor circuitry.

{{< /expand >}}

## 14. How to code your Feather to constantly check an input while also running actuators (Nov. 1)

Suppose you want to check for the state of inputs while also running motors, lights, and other actuators. In particular, you want to flash an LED, constantly check for a button press that sets an input pin HIGH, and flash a different LED when the button is pressed.

### The naive approach

Here's how a novice programmer might try to set up a microcontroller to check for input and flesh a second LED when a button is pressed.  Why will this code probably **not work very well** to accomplish the goal stated above?

{{< expand "Click to see the code that won't work very well" "..." >}}
<pre class="code">
import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

other_led = dio.DigitalInOut(board.D5)
other_led.direction = dio.Direction.OUTPUT

led.value = False

while True:
    if led.value is True:
        led.value = False
    else:
        led.value = True

    time.sleep(1.0)

    if button.value is True:
        other_led.value = True
    else:
        other_led.value = False
</pre>
{{< /expand >}}

### Try a state machine instead!

Writing code for “state machines” is a better technique for this situation. At this [link](https://gist.github.com/pingswept/1d37a74943f73a6266688db44f3e382d) (and in the box below) is one way to set up state machines in CircuitPython. 

{{< expand "Click to see the state machine code" "..." >}}
<pre class="code">
import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

other_led = dio.DigitalInOut(board.D5)
other_led.direction = dio.Direction.OUTPUT

STATE_TOGGLE = 1
STATE_CHECK_BUTTON = 2

state = STATE_TOGGLE
next_toggle = 0
led.value = False

while True:
    if state is STATE_TOGGLE:
        if led.value is True:
            led.value = False
        else:
            led.value = True
        next_toggle = time.monotonic() + 1.0
        state = STATE_CHECK_BUTTON
    elif state is STATE_CHECK_BUTTON:
        if button.value is True:
            other_led.value = True
        else:
            other_led.value = False
        if time.monotonic() > next_toggle:
            state = STATE_TOGGLE
</pre>
{{< /expand >}}

