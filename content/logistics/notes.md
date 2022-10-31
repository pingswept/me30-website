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

## Class 14: PWM

Pulse Width Modulation to control speed of motors. Begin with exercise that shows two square waves one with 75% duty cycle and one with 25% duty cycle, and ask for student initial ideas on how the motor would behave in each case (not yet using the term "duty cycle").

## Class 13: Feather challenges

Start Feather challenges

## Class 12: Intro to microcontrollers 

Feather set-up

Pins on Feather can be switched high or low. Each pin controls one MOSFET or could use one pin for two MOSFETs in an H-bridge. 

Importance of connecting Feather GND to ground loop. 



## Class 11: PCB 1 Test and PCB Fabrication

### PCB 1 test:

Students solder their components onto their P1 PCBs before class. In class, gather in groups of 4. Connect some resistors to your P1 boards and determine how much current your pins can supply before the regulation drops out (for each of the two regulators).

### PCB fabrication

Discuss PCB layers and manufacturing process

## Class 10: Hidden Challenges of Project 2 & Motor Measurements

### Hidden challenges

Challenge 1: Ampacity. What size traces to use and how to find out? 

Challenge 2: Making sure you have connectors on PCB to connect motor and Arduino to PCB (screw terminals, pin headers, wire loops, etc)

Review of KiCAD footprints and how to find appropriate footprints if there isn't a matching option.

Conventions for making circuit schematics
		
Look at the PCB design take-aways they generated after P1
		
Have them individually sketch out a P2 PCB layout design (on paper or whiteboard, etc.), while looking at the list of P2 requirements
		
Share and improve their sketches in groups

Things to go over:
	•	planning PCB connectors. They can merge the P-channel and N-channel connections for each diagonal pair.
	•	Reminder that they need common ground between motor supply and control supply.
	•	The P-channels can handle 27 A. Not sure about screw terminals. But for 27 A, you’d need somewhere around a 20-40 mil trace width, assuming an external trace with normal 1 oz copper.

### Motor measurements

Description of how a DC motor works.

Demo of DC motor working, using rotor from sander and magnet.

Exercise: measure time to lift around 0.5 kg of water 0.5 m. Measure current and voltage. Estimate power in, power out, and efficiency. (Turns out efficiency is only 10% or so. I guess gearbox friction is terrible, and effiency is generally bad at low speeds.)

Exercise: Measure the resistance of your DC gearmotor's coils. Then, hook it up to 12 V with alligator clips and measure its no-load current. (The current will be relatively high, around 100-150 mA, because the gearbox friction is already loading your motor.)

Intro Project 2.5: Design and build a hub, spool, or lever arm that attaches to your motor shaft and provides a hole (where you can attach a paper clip) 1.5cm from the shaft axis. Your hub must be able to handle enough torque to stall the motor when it is operating at 12 V.  Submit your Solidworks rendering of your design and bring your hub to class.  (In class on the P2.5 due date, we will make a histogram showing range of torque applied before either slipping or stalling.)


## Class 9: Soldering demo and H-bridge details

Soldering demo so students are prepared for the arrival of P1 PCBs and the in-class test of the P1 PCBs (in a couple weeks)

Revisit how to test one corner of an H-bridge (focus on top left P channel)

Introduce BJT as better method of switching P channels (still focus on top left P channel)

H-bridge circuit analysis worksheet

Exercise: Build H-bridges with BJTs. Your goal: get your H-bridge circuit working, and then help your neighbor get theirs working, too. Why help your neighbor? Because the process of helping will help you understand it better.

H-bridge debugging. Testing individual MOSFETs. Using multimeter to check voltage at various points. 


## Class 8: Spinning in both directions: the H-bridge


High-side vs. low-side drive. NPN and PNP. N-channel and P-channel.

H-bridge architecture.

Pull-down and pull-up resistors.

If time, NPN used to turn on P-channels.

## Class 7: MOSFETs 

### Control a motor with a MOSFET



## Class 6:

### Intro to transistors

### Low power and high power: BJTs
### The geography of electronics

We use small, low power chunks of silicon to control transistors, which control large flows of current. This is the structure of all modern electronics.

### Transistors as switches

All about BJTs

Exercise #5: Build a BJT circuit to control a motor. First hook up a motor without a BJT so you know you have your 12 V wired correctly. Also set up your 5 V regulator. Then, add the BJT with a base resistor.


## Class 5: 

### Kicad practice, Kicad Q&A

More Kicad practice with an in-class exercise to make the layout for a push-button motor supply PCB that would work in tandem with the Project 1 PCB (on the same breadboard). See Exercise #4.

Kicad Q & A session using shared doc to crowd-source answers


## Class 4: Kicad

You’ve got some basic circuit knowledge. You’re gonna build lots more circuit knowledge, but we’ve got to get some manufacturing underway. While it would be ideal to wait til a bit later to add this complexity, PCB manufacturing isn’t instantaneous so need to start now, so you have the PCB in hand when needed.

### Kicad workflow

schematic -> netlist export -> assign footprints -> netlist import -> lay out PCB

Important maxim: if a footprint has the right size holes in the right location, it is the right footprint. You can also care about the part outline and labels, but the holes are what matter the most.

How PCBs are made, briefly. Copper-clad fiberglass is drilled, exposed to light, etched with acid, and covered in soldermask and silkscreen. Multilayer PCBs contain power planes and rectilinear spaghetti.

## Class 3: Catch-up mini-lecture

Ohm's law and i-v curves

Using a multimeter - 3 ways

Big picture view of Project 1

Q & A about Project 1 breadboard prototypes


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

How the barrel jack works. See that pin 3 is not involved, and then use your multimeter to check polarity on pins 1 and 2. All of our power supplies are center-positive, but center-negative power supplies exist in the world. (In our supplies, postive is the center metal lining, which goes to pin 1, at closed end of barrel. Ground/negative is the outer metal shell, which goes to pin 2, closer to open end.)

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

V - V_f = V_r.  V_r = iR.   R = V_r / i.  Aim for current of 0.001 A and assume V_f of 3V.


### Extension/challenge: Re-arrange your circuit so you have one LED that stays on permanently and another that is powered by the switch

