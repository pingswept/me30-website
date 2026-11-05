---
title: "Class 16: Sensors"
draft: true
---
If we're thinking about electricity like it's water flowing in a pipe, then a resistor is like a narrow restriction in a pipe that limits the amount of current that can flow through.

Here's what resistors actually look like in the real world.

![Different kinds of resistors](/img/resistors.jpg)

At the top left, we have 1/4 W, 10k carbon film through-hole resistors. They're probably the most common resistors in the world.

At top right, we have a big spool of 1/10 W, 1k surface-mount resistors. They might rival the carbon film resistors at left for the popularity title.

The big blocky brass thing in the middle is a current shunt, that is, a resistor that has a very low resistance that is precisely calibrated. You run a large current through the rod in the middle, and then you measure the voltage drop with the two wires on either side. If you look carefully at the right hand side of the shunt, you can seea legend stamped into the metal that reads, "50 A 60 mV." This means that when you measure a 60 mV drop across the shunt, 50 A is flowing through it. (Thus, its resistance is 0.060/50 = 0.0012 ohms, or 1.2 milliohms.)

In the lower left, we have a power resistor. This is just a resistor encased in a big block of metal so you can run a lot of current through it without melting it. The last line of the legend printed on it says, "50W 0.15Ω," which means that the resistor can dissipate 50 W without burning up. Knowing its power limit and resistance, you can calculate its current and voltage limits: sqrt(50/0.15) = 18 A, and sqrt(50 * 0.15) = 2.7 V.
