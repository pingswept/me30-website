---
title: "Rough notes"
draft: false
---
## Rough notes for class meetings

This page is more like the show notes for a podcast (links to stuff mentioned in class, reminders) than a coherent description of electronics.

{{< hint danger >}}
**These notes are really just for the ME 30 instructors. You are probably spending your time frivolously if you are reading them.**

Seriously, go read some of the sensible pages on the site rather than this malformed dreck.
{{< /hint >}}

## Before Project 3:

**Add a software exercise where we practice writing a state machine.**

Make an LED flash twice per second while checking a button:
- the bad way (delay)
- using millis() in a loop
- real state machine and functions

## (2021) Class 9: Arduino Connections & PWM for Motor Control

Pins on Arduino can be switched high or low. Each pin controls one MOSFET or could use one pin for two MOSFETs in an H-bridge. 

Importance of connecting Arduino GND to ground loop. 

Pulse Width Modulation to control speed of motors. Ideally demo this using a signal generator. Digital vs analog signals.

Exercise: Work on KiCAD - revisit this and come up with motor related exercise. 

## (2021) Class 8: Hidden Challenges of Project 2 & H-Bridge Debugging

Challenge 1: Ampacity. What size traces to use and how to find out? 

Challenge 2: Making sure you have connectors on PCB to connect motor and Arduino to PCB (screw terminals, pin headers, wire loops, etc)

Review of KiCAD footprints and how to find appropriate footprints if there isn't a matching option.

H-bridge debugging. Testing individual MOSFETs. Using multimeter to check voltage at various points. 

Exercise: Continue working on H-bridge prototype.

## (2021) Class 7: Spinning in both directions: the H-bridge

High-side vs. low-side drive. NPN and PNP. N-channel and P-channel.

H-bridge architecture.

Pull-down and pull-up resistors.

If time, NPN used to turn on P-channels.

## (2021) Class 6: Motors

Comments on feedback from last class.

Description of how a DC motor works.

Demo of DC motor working, using rotor from sander and magnet.

Exercise: measure time to lift around 0.5 kg of water 0.5 m. Measure current and voltage. Estimate power in, power out, and efficiency. (Turns out efficiency is only 10% or so. I guess gearbox friction is terrible, and effiency is generally bad at low speeds.)

## (2021) Class 5: MOSFETs

### Intro stuff

LA's: set up power strips right away.

### Motor measurements, episode 1

Measure the resistance of your DC gearmotor's coils. Then, hook it up to 12 V with alligator clips and measure its no-load current. (The current will be relatively high, around 100-150 mA, because the gearbox friction is already loading your motor.)

## Class 4: 

### Kicad Q&A, intro to transistors

Kicad Q & A session

### Low power and high power: BJTs
### The geography of electronics

We use small, low power chunks of silicon to control transistors, which control large flows of current. This is the structure of all modern electronics.

### Transistors as switches

All about BJTs

Build a BJT circuit to control an LED. First hook up an LED without a BJT so you know you have your current-limiting resistor right. Then, add the BJT with a base resistor.

## Class 3: Kicad

You’ve got some basic circuit knowledge. You’re gonna build lots more circuit knowledge, but we’ve got to get some manufacturing underway. While it would be ideal to wait til a bit later to add this complexity, PCB manufacturing isn’t instantaneous so need to start now, so you have the PCB in hand when needed.

### Kicad workflow

schematic -> netlist export -> assign footprints -> netlist import -> lay out PCB

Important maxim: if a footprint has the right size holes in the right location, it is the right footprint. You can also care about the part outline and labels, but the holes are what matter the most.

How PCBs are made, briefly. Copper-clad fiberglass is drilled, exposed to light, etched with acid, and covered in soldermask and silkscreen. Multilayer PCBs contain power planes and rectilinear spaghetti.


## Class 2: Build a voltage regulator circuit

### Intro stuff

LA office hours

Notice that we are offering a few different modes of learning. Check which one works for you and go deep on that.

### Re-visit extension/challenge from end of Class 1 (having two LEDs in circuit)

Series vs. Parallel

Resistance increases in series and decreases in parallel

### Frame Project 1
We’ve “powered” on LED with 12V from wall, “controlled” with push button.
By end of semester, you’re going to want to control outputs with portable microcontroller, which handles only 5 V.

So how do we get 5 V from power supply instead of 12?

### Voltage divider as first approach to reducing output voltage

Voltage divider exercises (first two)

Uncover the issue with voltage dividers / need for voltage regulation (see if calculated voltage matches measured voltage.)

Attaching load causes sag in voltage from current pull - not the same as voltage regulators

### Project 1: Voltage regulation

We need 4 components: two capacitors, one regulator, and one power jack, plus various wires and a breadboard.

12 V in, leading to 3 outputs: 12 V passing through on a screw terminal, 5 V from an L7805CV, and 3.3 V from an LM1117.

There are at least two possible topologies: cascade the 3.3 V regulator off the 5 V output, or feed both regulators directly from 12 V. Cascading the two regulators is less efficient. Also, we have to worry about dropout voltage. If you feed the L7805CV less than 7 V, its output will sag. At 6 V input, its output will be around 4 V, and the regulation will be terrible.



## Class 1: Intro and build an LED circuit

### Introductions

Nametags and introductions: Instructors and LA's

[andnowforelectronics.com](http://andnowforelectronics.com)

How class works: short lectures, then build; collaborative community where those with less experience can learn from those with more experience, AND vice versa

Office hours

Join [the ME 30 Slack channel](https://tufts-me30.slack.com/)

Failure is success. But aim high and try hard!

Grading is on project completion, not any performance threshold.

### Voltage and current

AC voltage comes from the big gas turbine in Everett. Burn the gas, spin the magnets past coils of wire. You get sinusoidal voltage out.

Sidebar: voltage vs. current. Current is like water flowing in a hose. Voltage is like the pressure of the water in the hose.

Our DC power supply converts high (110 V) AC voltage to low (12 V) DC voltage.

### Project 0: Power an LED with "wall" power through our DC power supply. Control it with a pushbutton.

Schematic diagram of what we’re going to build
- ground symbol
- note closed loop
- find each component as we discuss: DC power supply, one power (barrel) jack, one LED, one resistor, one pushbutton, plus various wires and a breadboard.

How the barrel jack works

How the LED works

Breadboard connections / pattern layout

### LEDs
Nonlinear I-V curve means they are not resistorsCurrent flowing in one direction will be stopped, but current flowing in the opposite direction will result in LED emitting light.

Forward voltage. Varies by color.

Need for current limiting resistor to prevent burnout.

### Ohm’s Law as definition of resistance
Resistors always have linear I-V curve, otherwise, it’s not a resistor.

Review resistor color codes

Importance of considering how much power resistors are rated for or they will burn out 

Which resistor for your LED circuit, and why?


### Extension/challenge: Re-arrange your circuit so you have one LED that stays on permanently and another that is powered by the switch

