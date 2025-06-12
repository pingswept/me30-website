---
title: "Class 22: Sensor amplification"
draft: false
---
## Sensor amplification

Sensors produce real small voltages, so we need to amplify them.

## Strain gauges ##

A strain gauge is a small wire that changes resistance when it is stretched. The strain gauges we'll use in ME 30 are made of constantan, an alloy of copper and nickel. The constantan is attached in a serpentine shape to a polyimide film. The 14 sections in the serpentine shape means that the wire behaves like 14 resistors in series, each of which increases in resistance when it's stretched. When the strain gauge is not stretched, it has a resistance of 120 ohms. When stretched, it increases to 121 or 122 ohms.

If we put the strain gauge in series with a normal 120 ohm resistor to make a voltage divider supplied with 3.3 V, the voltage between the two resistors will be around 1.65 V. The voltage will go up and down in proportion to strain, but the voltage change is so small that it will be hard to detect.

## Amplification ##

To make the signal bigger, we'll use an amplifier. You can buy a strain gauge amplifier like the HX711, but we're going to build one using a chip called an operational amplifier, or op-amp. We're also going to deploy a technique that will make the sensor more accurate.

The technique we'll use is called a Wheatstone bridge (invented in 1833 by Samuel H. Christie; Wheatstone just blathered on about it). The idea is to add a second pair of resistors in parallel with the original voltage divider and then measure the voltage difference between the two central nodes. It's like our voltage is a bridge across the middle of the circuit.

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
