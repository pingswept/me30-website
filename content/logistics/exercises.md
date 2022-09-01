---
title: "Exercises"
draft: false
---
## In-class exercises

### 1: Project #0: Power an LED with "wall" power

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


### 2: Build a voltage regulation circuit

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors

### 3. Build voltage dividers

![Voltage dividers](/img/voltage-dividers.png)

### 4. Control an LED with a transistor

Making an LED light up is pretty simple: put a resistor in series with it and apply a voltage. If you sized the resistor right and didn't put the LED in backwards, you're done. When we want to control things like LEDs electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off an LED.

You need 4 things:

1. A 5 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. An LED
4. Two appropriately-sized current-limiting resistors: one for the LED, one for the BJT

The picture below shows the concept of what you're building. In place of the motor, we'll use an LED.

![Typical BJT circuit](/img/typical-bjt-circuit.png)

### 5. Measure a DC gearmotor (part 1)

Here are a few basic measurements you can make to understand your DC gearmotor better. We'll start with current measurement.

1. When your motor is stalled (like if you're trying to lift something too heavy with it), it behaves like a resistor. This is when your motor draws maximum current, so checking the resistance is a good way to estimate the maximum current for whatever drive voltage you choose. Using the resistance-measuring setting of your multimeter (the omega symbol, Ω, represents ohms), measure the resistance of the coils of your motor.
2. Make your DC gearmotor spin by connecting your motor directly to your 12 V DC power supply using alligator clips. Then, measure the current the motor draws with no load attached by putting your multimeter in series with the motor. You should switch your multimeter to the A setting (for Amps), and move the red lead to the port on the left side of the meter that is labeled "A". The black lead stays in the black port labeled "COM".

With these measurements, you can estimate the maximum current the motor will draw at any voltage, and the minimum current at 12 V. If you can estimate how much power a task will require, you can start to figure out what voltage this motor would need to deliver that power (assuming perfect efficiency, for now). That's the first step toward deciding whether this is the right motor for whatever you're building.
