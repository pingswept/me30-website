---
title: "Exercises"
draft: false
---
## In-class exercises

### 1: Build a voltage regulation circuit

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors

### 2. Control an LED with a transistor

Making an LED light up is pretty simple: put a resistor in series with it and apply a voltage. If you sized the resistor right and didn't put the LED in backwards, you're done. When we want to control things like LEDs electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off an LED.

You need 4 things:

1. A 5 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. An LED
4. Two appropriately-sized current-limiting resistors: one for the LED, one for the BJT

The picture below shows the concept of what you're building. In place of the motor, we'll use an LED.

![Typical BJT circuit](/img/typical-bjt-circuit.png)
