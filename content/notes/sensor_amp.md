---
title: "Class 22: Sensor amplification"
draft: true
---

## Strain gauges

Strain gauges tell you how much a material is deforming by changing their resistance when bent. The strain gauge we'll use to explore sensor amplification is made up of tiny wire laid down like a zig-zag so there is a change in its resistance when it is stretched or compressed - that is, when strain occurs. This type of strain gauge usually has a baseline resistance of something like 120Ω or 350Ω.

![diagram and photo of a strain gauge]

A strain gauge's "GF," or gauge factor, is the ratio of fractional change in electrical resistance to the fractional change in length (strain). A GF of 2 is typical for strain gauges made of tiny metal wire, like ours.

## Using voltage measurements to determine resistance: the Wheatstone bridge

When a strain gauge is stretched or compressed, its resistance changes. If we could measure the resistance change directly, using the gauge factor, we could easily compute the value of the strain on one gauge.  However, for a sensor circuit to be "read" by a microcontroller (like an Arduino or KB2040), the sensor's output needs to be a voltage value, not a resistance. How can we convert a resistance change into a voltage measurement?

The solution is called a Wheatstone bridge. It's a network of four resistors - at least one of which which has an unknown resistance value, which you want to know.

In the diagram below of a Wheatstone bridge, Rx represents the strain gauge. We choose R1, R2, and R3 so that they are the same as the gauge's baseline resistance (its resistance when it's not strained). When all the resistance values are the same, VL is equal to VR, and the voltage difference across the "bridge" is 0. However, when the gauge is strained, Rx changes, and VL and VR differ from each other. That means the "bridge voltage" will be nonzero. 

How does that bridge voltage relate to Rx? We can use the voltage divider equation to find out.

By voltage divider principles:

![equations for VL and VR]

So the voltage across the bridge, or VL - VR, is:

![equation for Vbridge]

Solving for Rx in terms of Vbridge, we can get:

![solution for Rx]

And if the three known resistances are the same, things simplify greatly:

![solution for Rx with 3 equal resistors]

## The need for amplification

Strain usually occurs in quantities of millistrain or microstrain, something like 0.0005ε, which is 0.5 millistrain(mε) or 500 microstrain (µε).

Let's take a piece of metal that experiences a strain of 500µε, or 0.0005ε. With a gauge factor of 2, the change in resistance will be only twice that, or 0.001. 

That's only a 0.1% change in resistance!  

If the baseline resistance of the gauge is 120Ω, its resistance change at 500µε would be only 0.12Ω. The bridge voltage produced by that resistance would not be detected accurately by our multimeters or microcontrollers.  That means we need a device that can take a very small bridge voltage and amplify it into a voltage we can measure accurately.

Enter: the op amp.

## Using op amps to amplify the difference between two voltage points

