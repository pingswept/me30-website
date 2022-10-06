---
title: "Exercises"
draft: false
---
## In-class exercises

### 1: Project #0: Power an LED with "wall" power (Sep. 6)

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


### 2. Build voltage dividers (Sep. 8)

![Voltage dividers](/img/voltage-dividers-2022.png)



### 3: Build a voltage regulation circuit (Sep. 13)

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors


### 4. Motor power supply PCB with indicator LED (Sep. 20)

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


### 5. Control a motor with a BJT (Sep. 27)

Making a motor spin is pretty simple: apply sufficient voltage across its leads. When we want to control things like motors (or LEDs, buzzers, etc.) electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off a motor.

You need 4 things:

1. A 5 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. A DC gear motor
4. An appropriately-sized current-limiting resistor for the BJT

The picture below shows the concept of what you're building. In place of the 24 V source, we'll use your 12 V source.

![Typical BJT circuit](/img/typical-bjt-circuit.png)


### 5.5 Determine pin voltages and ideal resistor value for a BJT circuit (Sep. 29)

Fill in the table below to indicate the voltage at E, B, and C when the input is (a) at ground and (b) at 3.3 V.

(Graphic to be added)

### 6. Control a motor with a MOSFET (Sep. 29)

You've used a bipolar junction transistor to control a motor. Now try using the other main class of transistor: a metal oxide semiconductor field effect transistor, or MOSFET.  The main difference between the [two types of transistors](http://andnowforelectronics.com/notes/low-power-high-power/) is that BJTs are current-controlled, and MOSFETs are voltage-controlled.

You need 5 things:

1. 3.3 V voltage source, which you can make using the 3.3V regulator in your kit
2. 12 V voltage source
3. An N-channel MOSFET
4. A DC gear motor
5. A pull-down resistor for the MOSFET

![MOSFET circuit](/img/mosfet-controller.jpg)

### 7. H-bridge circuit analysis, part 1 (Oct. 4)

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


### 7. H-bridge circuit analysis, part 2 (Oct. 4)

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

### 8. Measure a DC gearmotor (Power In) (Oct. 6)

Here are a few basic measurements you can make to understand your DC gearmotor better. The overall goal is to determine the efficiency of the motor by comparing the electrical power that goes into it ("power in") with the mechanical power it delivers ("power out"). 

We'll start with determing the minimum and maximum current that the motor draws.

1. When your motor is stalled (like if you're trying to lift something too heavy with it), it behaves like a resistor. This is when your motor draws maximum current, so checking the resistance is a good way to estimate the maximum current for whatever drive voltage you choose. Using the resistance-measuring setting of your multimeter (the omega symbol, Ω, represents ohms), measure the resistance of the coils of your motor.
2. Make your DC gearmotor spin by connecting your motor directly to your 12 V DC power supply using alligator clips. Then, measure the current the motor draws with no load attached by putting your multimeter in series with the motor. You should switch your multimeter to the A setting (for Amps), and move the red lead to the port on the left side of the meter that is labeled "A". The black lead stays in the black port labeled "COM".

With measurement #1 above (the resistance of the coils), you can estimate the **maximum current** the motor will draw at any voltage. With measurement #2, you can find the **minimum current at 12 V**. 

When you know the current and the voltage, you can multiply them to find the electrical power going into the motor.

If you can estimate how much power a task will require, you can start to figure out what voltage this motor would need to deliver that power (assuming perfect efficiency, for now). That's the first step toward deciding whether this is the right motor for whatever you're building.

### 9. Measure a DC gearmotor (Power Out) (Oct. 6)

The next step is to determine how much mechanical power the motor actually delivers ("power out"). One way to do this is to measure the time it takes to perform a certain amount of work (i.e., to add energy to a system).

1. Use tape and string to hang a water bottle from your motor shaft.
2. Measure the time it takes your motor to lift around 0.5 kg of water 0.5 m. Compute the amount of work done in lifting the water. With these two values, you can find "power out."
3. Compare "power in" and "power out" to estimate the motor's efficiency.
