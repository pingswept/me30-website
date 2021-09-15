---
title: "Rough notes"
draft: false
---
## Rough notes for class meetings

This page is more like the show notes for a podcast (links to stuff mentioned in class, reminders) than a coherent description of electronics.

## Class 2: More voltage regulation and Kicad

### Intro stuff

LA office hours

Notice that we are offering a few different modes of learning. Check which one works for you and go deep on that.

### More voltage regulation

Develop your breadboard circuit a little more fully to meet the P1 requirements.

12 V in, leading to 3 outputs: 12 V passing through on a screw terminal, 5 V from an L7805CV, and 3.3 V from an LM1117.

There are at least two possible topologies: cascade the 3.3 V regulator off the 5 V output, or feed both regulators directly from 12 V. Cascading the two regulators is less efficient. Also, we have to worry about dropout voltage. If you feed the L7805CV less than 7 V, its output will sag. At 6 V input, its output will be around 4 V, and the regulation will be terrible.

### Kicad workflow

schematic -> netlist export -> assign footprints -> netlist import -> lay out PCB

Important maxim: if a footprint has the right size holes in the right location, it is the right footprint. You can also care about the part outline and labels, but the holes are what matter the most.

How PCBs are made, briefly. Copper-clad fiberglass is drilled, exposed to light, etched with acid, and covered in soldermask and silkscreen. Multilayer PCBs contain power planes and rectilinear spaghetti.

### Introductions

## Class 1: Intro and build a voltage regulation circuit

### Introductions

Briana Bouchard, Brandon Stafford, and 8 LA's

[andnowforelectronics.com](http://andnowforelectronics.com)

Room assignments, how class works: three classrooms, short lectures, then build

Office hours

Join [the ME 30 Slack channel](https://tufts-me30.slack.com/)

Failure is success. But aim high and try hard!

Grading is on project completion, not any performance threshold.

### Voltage and current

AC voltage comes from the big gas turbine in Everett. Burn the gas, spin the magnets past coils of wire. You get sinusoidal voltage out.

Sidebar: voltage vs. current. Current is like water flowing in a hose. Voltage is like the pressure of the water in the hose.

Our DC power supply converts high (110 V) AC voltage to low (12 V) DC voltage.

### Voltage regulation

We need 4 components: two capacitors, one regulator, and one power jack, plus various wires and a breadboard.

Find those components in your kits.

Use the multimeter on the DC voltage setting to measure voltage.

### Your homework for Tuesday

1. Make it so that 12 V goes into your circuit and 5 V comes out.
2. Install Kicad.
3. Try to replicate the schematic.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. Read and try to absorb the web pages listed under ["What to study" on the calendar](http://andnowforelectronics.com/logistics/calendar/)
6. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.
