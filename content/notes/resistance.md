---
title: "Resistance"
draft: false
---
If we're thinking about electricity like it's water flowing in a pipe, then a resistor is like a narrow restriction in a pipe that limits the amount of current that can flow through.

Here's what resistors actually look like in the real world.

![Different kinds of resistors](/img/resistors.jpg)

## Resistors are linear

When we say something behaves linearly, we just mean that if you double the input, the output also doubles. If you triple the input, the output triples. With a resistor, if you double the voltage pushing electrons through the resistor, the current through the resistor will double.

In reality, resistors aren't exactly linear, but they're close enough. The most common deviation that you'll run into is that as you run more current through a carbon film resistor, it heats up. As it heats up, the resistance drops slightly, so if you double the voltage, you actually get slightly more than double the current. (But that's just carbon film resistors. The resistance of copper wires increases slightly with temperature.)

## We measure resistance in ohms

We measure resistance in ohms ({{< katex >}}\Omega{{< /katex >}}), a measure of how many amps the resistor lets through per volt applied to it. A 1 ohm resistor lets through 1 amp per volt.

This brings us to Ohm's Law, which is really just the definition of resistance as the ratio of voltage applied to current passed. You could write it as

{{< katex >}}V / I = R{{< /katex >}}

but it's more commonly written as

{{< katex >}}V = IR{{< /katex >}}

## Power rating

One other matter to worry about is what happens if you run a lot of current through a resistor. Raise the current enough, and the resistor will eventually burn out.

We can calculate power by multiplying voltage and current. Think this through with the meaning of the units: volts are joules per coulomb, and amps are coulombs per second. In the product of the two, the coulombs cancel, so we get joules per second, as we would expect for power, a measure of the rate of energy flow.

Typical carbon film resistors are rated for 1/4 W.

Typical 0805 surface mount resistors are rated for 1/8 W.

## Tolerance

When resistors are manufactured, there is some variation in their resistance. Typical cheap carbon film resistors are specified to be accurate within 5% of their nominal value, but they are usually closer than 1%. This is different than capacitors, which are specified to be within 10% or 20% of their rated value, and often push those limits, especially across signals of different frequencies.