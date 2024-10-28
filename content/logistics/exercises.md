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

Learn to program your KB2040 board by working through the first 6 of these 12 challenges: http://andnowforelectronics.com/notes/kb2040-challenges/

You'll want to consult the [KB2040 programming](http://andnowforelectronics.com/notes/kb2040-programming/) resources.

For Kristen's 1-page summary of the most important Circuit Python commands for your KB2040, click [here](https://tufts.box.com/s/lczswqulqewphbxyku1zpvazp73govzi).

## 12. Project 2 takeaways reflection (Oct. 9)

(a) What are some problems you encountered along the way of working on your game for Project 2, and what did you learn from them? Let's collectively document those [here](https://docs.google.com/document/d/1yKv0bKWhP53wHEWxWcOBskjrUdKzZLRV_DfW0eVWal0/edit?usp=sharing).

(b) Take a moment to fill out the [self-assessment for Project 2](https://tufts.qualtrics.com/jfe/form/SV_7PAFa4Tk6kXRZ1s), if you have not done so already.

## 13. Mechanically controlled two-way motor circuit (Oct. 9)

With a partner or two, build a circuit that will allow you to use pushbutton switches to toggle a 12-V DC motor between the states of (a) OFF (b) ON counterclockwise, and (c) ON clockwise. That means your motor needs to be able to draw current in either direction (only one direction at a time). Your circuit should NOT use transistors. It should include (a) 12 V adapter and barrel jack, (b) DC gearmotor, (c) assorted wires, (d) as many pushbutton switches as you want.

As you work on this challenge, **be careful not to create a situation where you are sending 12 V to ground only through wires.** That's a short circuit and will cause heat and smoke!

![Motor with question marks](/img/Exercise_2waymotor.jpg)

## 14. Recognizing common errors in KB2040 Challenge #6 (Oct. 16)

Challenge #6 asks you to control a motor's on/off state with a KB2040 output pin. Below are two approaches to setting up the circuitry. Each has problems that will prevent it from working correctly. What do you think those problems are?

![Microcontroller problems](/img/Micro_with_transistors_flawed.jpg)

*What are the problems with approach #1?*

{{< expand "See the answer" "..." >}}
(a) The KB2040 GND pin is not tied to the same ground as the motor circuitry.

(b) There is no current-limiting resistor between the KB2040 output and the BJT base. We want to keep the current through the base-emitter diode to about 10% of the collector-to-emitter current. If the motor is drawing 150 mA, then we want the base-emitter current to be about 15 mA. And we know that when the BJT is on, its base voltage is 0.6 V. Since the KB2040 output supplies 3.3 V, we need a resistor to drop the voltage by 2.7 V and limit the current to something closer to 15 mA. A resistor somewhere between 100 and 1000 ohms should do it.

![Fixed circuit](/img/Micro_BJT_Fixed.jpg)
{{< /expand >}}

*What are the problems with approach #2?*

{{< expand "See the answer" "..." >}}
(a) The motor is "below" the N-channel MOSFET. When the gate is supplied with voltage, **for a very brief moment** the gate voltage will be higher than the source voltage, and current will flow from drain to source and therefore through the motor.  But once current starts to be drawn through the motor, the voltage at the source will rise to somewhere near 12 V. At this point, the gate voltage of 3.3 V will be less than the source voltage, and the MOSFET will no longer allow current flow to the motor.

(b) The MOSFET gate does not have a pull-down resistor to ground.

(c) The KB2040 GND pin is not tied to the same ground as the motor circuitry.

![Fixed circuit](/img/Micro_MOSFET_Fixed.jpg)
{{< /expand >}}

## 15. H-bridge circuit analysis  (Oct. 16)

You've just wired up the top left corner of an H-bridge circuit using a P-channel MOSFET. You connect the other motor lead to ground so that you can test this corner before wiring up the transistors at any other corners.  If this corner is wired correctly, 

1. What should happen to the motor when the MOSFET gate is connected:

- to 12 V?  
- to ground?  

2. Sketch the current path for each of those gate states.

![Top left corner of an H-bridge](/img/Hbridge-corner.png)

Now you add a BJT as a different method for switching on the P-channel MOSFET. Again, you want to test this corner before moving on to other sections of the H-bridge. If the BJT and P-channel MOSFET in this corner are wired correctly, 

1. What should happen to the motor when the BJT base is:

- at 3.3 V?  
- at ground?  

2. Sketch the current path for each of those base states.
3. What is the voltage at G for each of those base states?

![add BJT to corner of an H-bridge](/img/Hbridge-corner-BJT.jpg)

## 16. H-bridge circuit analysis, part 2 (Oct. 21)

**This H-bridge circuit has four inputs, shown at locations 1, 2, 3, and 4. Each input turns a transistor on or off.**

*If all four switches were connected to 3.3 V (as shown below), what would happen and why?*  

![H-bridge inputs all at 3.3 V](/img/Hbridge_all3v.jpeg)

{{< expand "See the answer" "..." >}}
**Don't do this -  it will short the circuit!!** In this H-bridge, setting a corner input to 3.3 V turns that corner's MOSFET "on," allowing current to across the source-drain pathway. If all 4 MOSFETs are allowing current to flow, then this circuit's easiest path to ground will be down the two sides of the "H."  No current will flow through the highly resistive motor. The motor will not spin, and the rest of the circuit will get very hot.
{{< /expand >}}

## 17a. Measure a DC gearmotor (Power In) (Oct. 21)

Here are a few basic measurements you can make to understand your DC gearmotor better. The overall goal is to determine the efficiency of the motor by comparing the electrical power that goes into it ("power in") with the mechanical power it delivers ("power out"). 

We'll start with determing the minimum and maximum current that the motor draws.

1. When your motor is stalled (like if you're trying to lift something too heavy with it), it behaves like a resistor. This is when your motor draws maximum current, so checking the resistance is a good way to estimate the maximum current for whatever drive voltage you choose. Using the resistance-measuring setting of your multimeter (the omega symbol, Ω, represents ohms), measure the resistance of the coils of your motor.
2. Make your DC gearmotor spin by connecting your motor directly to your 12 V DC power supply using alligator clips. Then, measure the current the motor draws with no load attached by putting your multimeter in series with the motor. You should switch your multimeter to the A setting (for Amps), and move the red lead to the port on the left side of the meter that is labeled "A". The black lead stays in the black port labeled "COM".

With measurement #1 above (the resistance of the coils), you can estimate the **maximum current** the motor will draw at any voltage. With measurement #2, you can find the **minimum current at 12 V**. 

When you know the current and the voltage, you can multiply them to find the electrical power going into the motor.

If you can estimate how much power a task will require, you can start to figure out what voltage this motor would need to deliver that power (assuming perfect efficiency, for now). That's the first step toward deciding whether this is the right motor for whatever you're building.

## 17b. Measure a DC gearmotor (Power Out) (Oct. 23)

The next step is to determine how much mechanical power the motor actually delivers ("power out"). One way to do this is to measure the time it takes to perform a certain amount of work (i.e., to add energy to a system).

1. Use tape and string to hang a water bottle from your motor shaft.
2. Measure the time it takes your motor to lift a known weight a specific distance (you could try something like 0.5 kg of water, lifted up 1 m). Compute the amount of work done in lifting the water. With these two values (work and time), you can find "power out."
3. Compare "power in" and "power out" to estimate the motor's efficiency. You may want to measure "power in" at this motor operating point by measuring current while the water is being lifted.

## 18. Test the current limit of your P1 PCB (Oct. 23)

The voltage regulators on your P1 PCB are specified (on their data sheets) to be able to handle current at the level of 1.5 A (the 5V regulator) and 0.8 A (the 3.3 V regulator). But the question is - **once soldered into your P1 PCB, can they still perform up to their specified max current limit?**  

**Test your P1 PCB by determining how much current your regulators can actually send out to loads at your output pins before going into thermal shutdown.**

General procedure (details left to your group):
- Determine the resistance (it will be a low value!) you should attach to your 3.3 V and 5 V output so that something close to the specified max current is drawn (0.8 A or 1.5 A, respectively)
- Attach those low-ohm resistors to the output. These resistors stand in for a motor or other load to which you would want to supply 3.3 V or 5 V
- Monitor the voltage drop across that resistive load - that is, the voltage drop between the output of the regulator and ground
- Once that voltage drop begins to decrease lower than 3.3 V or 5 V, your regulator has gone into thermal shutdown (you may feel the regulators getting very hot before this happens)

Use this [shared doc](https://tinyurl.com/ME30questiondoc) to post questions about the P1 PCB test and about P3 circuit board design.

## 17. Motor speed-torque curve (Oct. 28)

Fill in values in the boxes to complete the motor speed-torque curve for the DC gearmotor in your ME 30 kit.

![speed torque curve](/img/speed-torque.jpg)

## 18. Motor selection cases (Oct. 28)

For each of these potential motorized game designs, determine whether the mechanical power and torque needs are within the capabilities of the DC gearmotor in your ME 30 kit.
- Can your motor handle these designs with a direct-drive approach (i.e., no gear trains or pulleys)? Why or why not?
- If your motor can't handle the design via direct-drive, can it do the job with a gear train or pulley transmission? Why or why not?
  
Work in a small group and post your answers to this google doc:
https://docs.google.com/spreadsheets/d/18il0YS9v-0mt79J7DdHGnpuPw71HNZ7vh3b1nPuhzdM/edit?usp=sharing

<! -- ![motor case 1](/img/motorcase1.jpg) -->

<! -- ![motor case 2](/img/motorcase2.jpg) -->

<! -- ![motor case 3](/img/motorcase3.jpg) -->

