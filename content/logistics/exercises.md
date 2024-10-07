---
title: "Exercises"
draft: false
---
# In-class exercises for Fall 2024

## 1: Power an LED with "wall" power (Sep. 4)

For a warm-up activity, let's power an LED with "wall" power and control it with a push button. 

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

In the cross-section view of a barrel plug inserted into the jack, you can see how the outer sheath of the plug makes contact with pin 2 and also how the plug breaks the continuity between pin 3 and pin 2.  

![barrel jack cross section](/img/BarrelJackMultipleViews.jpg)

Image credit: E. Schlaepfer and W. Oskay, 2023, Open Circuits, opencircuitsbook.com
{{< /hint >}}

*For an extension to this exercise, re-arrange your circuit so you have one LED that stays on permanently and another that is powered by the button.*


## 2. Build voltage dividers (Sep. 9)

We've used resistors to limit *current* flow through an LED.  

Let's see how we can also use them to reduce a *voltage* so we can supply a specific lower voltage to a device. For example, we might be using a 12 V power supply but want to supply only 5 V to an Arduino or other microcontroller. 

Read more [here](http://andnowforelectronics.com/notes/resistors/#typical-application-current-limiter) about using resistors as current limiters and voltage dividers.

For each of the set-ups below, provide 12 V as V_in, and predict the output voltage V_out. 

After you've written down your predictions for V_out, build the circuits and use your multimeter to measure V_out. If your predictions were off, try to figure out why.

![Voltage dividers](/img/voltage-dividers-2022.png)

## 3: Build a voltage regulation circuit (Sep. 9 & 11)

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors

## 4: Matching schematics to breadboards (Sep. 16)

Which of these breadboards has the same circuit as the one represented in the schematic?

![Schematic and breadboards](/img/Breadboard_schematic_matching.jpg)

## 5: Review of voltage and current (Sep. 16)

For the circuit below, analyze the following first for when the switch is open, and then for when the switch is closed:
1. Find sets of labeled points on the circuit where the **current** is the **same**.
2. Identify any points on the circuit where **no** current is flowing.
3. List the points in order from **highest current flow to least current flow**.
4. Find sets of points where the **voltage** is the **same**.
5. At what points should the voltage be near 0 V (e.g., ground)?
6. Order the points from highest to lowest voltage.
  
![Circuits to analyze](/img/Voltage_current_review.jpg)

## 6: Safety check (Sep. 16)

If you feel a circuit component getting hot or starting to smoke, what should you do first?
a. call over an LA
b. take the component out of the breadboard
c. unplug the power supply (e.g., barrel jack) from the breadboard
d. use your multimeter to measure the voltage across the component


What is a possible result if your multimeter dial is turned to the “mA” symbol and you put your multimeter probes between a high and low voltage location on a circuit? 
a. you’ll get zero current reading on your multimeter and prevent your circuit from working
b. you’ll let too much current go through your multimeter and blow its fuse
c. you’ll hear a beeping sound warning you that you should use the “A” symbol and port

## 7. Control a motor with a BJT (Sep. 25)

Making a motor spin is pretty simple: apply sufficient voltage across its leads. When we want to control things like motors (or LEDs, buzzers, etc.) electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off a motor.

You need 5 things in addition to the usual 12 V power supply and barrel jack:

1. A 3.3 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. A DC gear motor
4. An appropriately-sized current-limiting resistor for the BJT

The picture below shows the concept of what you're building. 

![Typical BJT circuit](/img/typical-bjt-circuit.jpg)

**Extension:** Add a potentiometer (a variable resistor) in series with the base and use it to vary the current flowing from base to emitter. Notice how this works as a crude motor speed controller, but also notice (carefully!) how the BJT heats up as more current is drawn through it.

![BJT circuit with potentiometer](/img/bjt-potentiometer.jpg)

## 8. Determine pin voltages and ideal resistor value for a BJT circuit (Sep. 25 & Sep. 30)

1. For the circuit shown in Exercise #7, fill in the table below to indicate the voltage at E, B, and C when the base resistor is connected to (a) 0 V and (b) 3.3 V.
2. To run your kit's gear motor, what is an ideal value for the resistor between 3.3 V and the base of the transistor?


|  | V_E  | V_B   | V_C |
|:----:|:-----:|:----:|:----:|
|  Input at O V   |    |   |     |
|  Input at 3.3 V   |    |   |     |

## 9. Control a motor with a MOSFET (Sep. 30)

You've used a bipolar junction transistor to control a motor. Now try using the other main class of transistor: a metal oxide semiconductor field effect transistor, or MOSFET.  The main difference between the [two types of transistors](http://andnowforelectronics.com/notes/low-power-high-power/) is that BJTs are current-controlled, and MOSFETs are voltage-controlled.

You need 5 things:

1. 3.3 V voltage source, which you can make using the 3.3V regulator in your kit
2. 12 V voltage source
3. An N-channel MOSFET
4. A DC gear motor
5. A pull-down resistor for the MOSFET

![MOSFET circuit](/img/mosfet-controller.jpg)

## 10. De-bugging challenges set 1 (Oct. 7)

Images of circuits: https://tufts.box.com/s/8al3jwc3l81ewtb16ridfo2ewqbjtc3v

Your Circuit 1 responses - https://tufts.qualtrics.com/jfe/form/SV_bdOn4VWl8YvNoQm

Your Circuit 2 responses - https://tufts.qualtrics.com/jfe/form/SV_3WAXKdT2tT7u0rc

Your Circuit 3 responses- https://tufts.qualtrics.com/jfe/form/SV_3t9Kl4NmGOak5JY

Your Circuit 4 responses- https://tufts.qualtrics.com/jfe/form/SV_3sFQF0NE8VbxI58

## 11. KB2040 microcontroller challenges set 1 (Oct. 7 and labs)

Learn to program your KB2040 board by working through the first 6 of these 12 challenges. You'll want to consult the [KB2040 programming](http://andnowforelectronics.com/notes/kb2040-programming/) resources.

http://andnowforelectronics.com/notes/KB2040-challenges/
