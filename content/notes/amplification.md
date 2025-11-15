---
title: "Class 22: Sensor amplification"
draft: false
---
## Sensor amplification

Sensors produce real small voltages, so we need to amplify them.

## Strain gauges ##

A strain gauge is a small wire that changes resistance when it is stretched. The strain gauges we'll use in ME 30 are made of constantan, an alloy of copper and nickel. The constantan is attached in a serpentine shape to a polyimide film. The 14 sections in the serpentine shape means that the wire behaves like 14 resistors in series, each of which increases in resistance when it's stretched. When the strain gauge is not stretched, it has a resistance of 120 ohms. When stretched, it increases to 121 or 122 ohms.

If we put the strain gauge in series with a normal 120 ohm resistor to make a voltage divider supplied with 3.3 V, the voltage between the two resistors will be around 1.65 V. The voltage will go up and down in proportion to strain, but the voltage change is so small that it will be hard to detect.


## another attempt below ##

## Strain gauges

Strain gauges tell you how much a material is deforming by changing their resistance when bent. The strain gauge we'll use to explore sensor amplification is made up of tiny wire laid down like a zig-zag so there is a change in its resistance when it is stretched or compressed - that is, when strain occurs. This type of strain gauge usually has a baseline resistance of something like 120Ω or 350Ω.

![diagram and photo of a strain gauge](img/strain_gauge.JPG)

A strain gauge's "GF," or gauge factor, is the ratio of fractional change in electrical resistance to the fractional change in length (strain). A GF of 2 is typical for strain gauges made of tiny metal wire, like ours.

## Using voltage measurements to determine resistance: the Wheatstone bridge

When a strain gauge is stretched or compressed, its resistance changes. If we could measure the resistance change directly, using the gauge factor, we could easily compute the value of the strain on one gauge.  However, for a sensor circuit to be "read" by a microcontroller (like an Arduino or KB2040), the sensor's output needs to be a voltage value, not a resistance. How can we convert a resistance change into a voltage measurement?

The solution is called a Wheatstone bridge. It's a network of four resistors - at least one of which which has an unknown resistance value, which you want to know.  

In the load cell we are using in Fall 2025 in ME 30, there are four strain gauges arranged in a Wheatstone bridge. Two of the resistors are placed on the bottom of a short beam, called a load cell, and two are placed on the top of the same beam. 

The diagram below shows a Wheatstone bridge with four strain gauges -- four variable resistors. They all have the same baseline resistance, R (their resistance when not strained). When all the resistance values are the same, VL is equal to VR, and the voltage difference across the "bridge" is 0. However, when the beam is bent, all the gauges are strained. The gauges on the top of the beam increase in resistance by delta. The gauges on the bottom decrease in resistance by delta. Now VL and VR differ from each other. That means the "bridge voltage," V_L - V_R, will be nonzero. 

{{< katex display >}}
\begin{aligned}
V_{source} &= \text{source voltage (12 V for our circuit)}\\
R &= \text{baseline resistance of strain gauge}\\
\Delta &= \text{change in resistance of gauge due to strain}\\
V_{L} &= \text{voltage relative to ground on the left side of the bridge}\\
V_{R} &= \text{voltage relative to ground on the right side of the bridge}\\
V_{bridge} &= \text{voltage across the outputs of the bridge}\\
\end{aligned}
{{< /katex >}}

{{< katex display >}}
\begin{aligned}
V_{L} &= \frac{R + \Delta}{(R + \Delta) + (R - \Delta)} * V_{source}\\
V_{R} &= \frac{R - \Delta}{(R - \Delta) + (R + \Delta)} * V_{source}\\

V_{L} &= \frac{R + \Delta}{2R} * V_{source}\\
V_{R} &= \frac{R - \Delta}{2R} * V_{source}\\

V_{bridge} &= V_{L} - V_{R} = \frac{(R + \Delta) - (R - \Delta)}{2R} * V_{source}\\
V_{bridge} &= \frac{2\Delta}{2R} * V_{source}\\
\frac{V_{bridge}}{V_{source}} &= \frac{\Delta}{R}\\
\end{aligned}
{{< /katex >}}

![four_gauge_wheatstone.jpg](/img/four_gauge_wheatstone.JPG)

How does that bridge voltage relate to the change in resistance (delta) caused by the strain?

We can use the voltage divider principle to find out:

![four_gauge_math.jpg](/img/four_gauge_math.JPG)


## The need for amplification

Strain usually occurs in quantities of millistrain or microstrain, something like 0.0005ε, which is 0.5 millistrain(mε) or 500 microstrain (µε).

Let's take a piece of metal that experiences a strain of 500µε, or 0.0005ε. With a gauge factor of 2, the change in resistance will be only twice that, or 0.001. 

That's only a 0.1% change in resistance!  

If the baseline resistance of the gauge is 120Ω, its resistance change at 500µε would be only 0.12Ω. The bridge voltage produced by that resistance change would not be detected accurately by our multimeters or microcontrollers.  That means we need a device that can take a very small bridge voltage and amplify it into a voltage we can measure accurately.

Enter: the op amp.

## Using op amps to amplify the difference between two voltage points


![op amp circuit](/img/difference_op_amp.JPG)

![op amp math](/img/op_amp_math.JPG)



## earlier text below ##
## Amplification ##

To make the signal bigger, we'll use an amplifier. You can buy a strain gauge amplifier like the HX711, but we're going to build one using a chip called an operational amplifier, or op-amp. We're also going to deploy a technique that will make the sensor more accurate.

The technique we'll use is called a Wheatstone bridge (invented in 1833 by Samuel H. Christie; Wheatstone just blathered on about it). The idea is to add a second pair of resistors in parallel with the original voltage divider and then measure the voltage difference between the two central nodes. It's like our voltage is a bridge across the middle of the circuit.

The Wheatstone bridge has two major advantages.

1. Resistors change resistance when they heat up, which means that your sensor signal will slowly drift with the temperature in the room, and it gets worse because the current running through the resistors heats them up even more. When comparing the two sides of the bridge, they are both at roughly the same temperature, so the temperature drift is the same on both sides, which means it cancels out in the difference.

2. It is easier to measure small voltages accurately than large voltages. Every op-amp has the unfortunate property that it responds slightly nonlinearly to input voltage. If we just try to amplify a 1.65 V voltage relative to ground ........ acch, not sure how to explain this well yet. This is called the common-mode rejection ratio, or CMRR. The LM324 opamps that we will be using have a CMRR of around 10,000 (80 dB).

## Circuit explanation ##

{{< katex display >}}
V_{in} = V_{out} * \frac{R_1}{(R_1 + R_2)}
{{< /katex >}}

{{< katex display >}}
\frac{V_{in}}{V_{out}} = \frac{R_1}{(R_1 + R_2)}
{{< /katex >}}

{{< katex display >}}
Gain = \frac{V_{out}}{V_{in}} = \frac{(R_1 + R_2)}{R_1}
{{< /katex >}}

{{< katex display >}}
Gain = 1 + \frac{R_2}{R_1}
{{< /katex >}}
