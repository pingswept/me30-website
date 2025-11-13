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

In the load cell we are using in Fall 2025 in ME 30, there are two strain gauges and two resistors arranged in a Wheatstone bridge.

The diagram below shows a Wheatstone bridge with four strain gauges. Assume that two of them are placed on the bottom of a beam, and two are placed on the top of the same beam. Each resistor shown in the Wheatsone bridge is one of these strain gauges. They all have the same baseline resistance, R (resistance when not strained). When all the resistance values are the same, VL is equal to VR, and the voltage difference across the "bridge" is 0. However, when the beam is bent, all the gauges are strained. The gauges on the top of the beam increase in resistance by delta. The gauges on the bottom decrease in resistance by delta. Now VL and VR differ from each other. That means the "bridge voltage," V_L - V_R, will be nonzero. 

four_gauge_wheatstone.jpg

How does that bridge voltage relate to the change in resistance (delta) caused by the strain?

We can use the voltage divider principle to find out:

four_gauge_math.jpg

## The need for amplification

Strain usually occurs in quantities of millistrain or microstrain, something like 0.0005ε, which is 0.5 millistrain(mε) or 500 microstrain (µε).

Let's take a piece of metal that experiences a strain of 500µε, or 0.0005ε. With a gauge factor of 2, the change in resistance will be only twice that, or 0.001. 

That's only a 0.1% change in resistance!  

If the baseline resistance of the gauge is 120Ω, its resistance change at 500µε would be only 0.12Ω. The bridge voltage produced by that resistance change would not be detected accurately by our multimeters or microcontrollers.  That means we need a device that can take a very small bridge voltage and amplify it into a voltage we can measure accurately.

Enter: the op amp.

## Using op amps to amplify the difference between two voltage points


op_amp_difference_amp.jpg

op_amp_math.jpg
