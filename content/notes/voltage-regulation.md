---
title: "Voltage regulation"
draft: false
---

## Why do we need voltage regulators?

(Make sure you understand the difference between [voltage and current](/notes/voltage-and-current/), or this won't make any sense. Also, remember that power = voltage * current.)

Suppose, as an example, you want to make your own toaster oven. You've done some heat transfer calculations, and you think you want the electric heaters in your oven to deliver around 1500 W.

Here are two ways you could do it.

You could get a 150 V power supply that can supply at least 10 A and connect it to a heater with a resistance of 15 ohms. 150/15 = 10, so 10 A would flow. 150 * 10 = 1500, so you would be delivering 1500 W.

You could also get a 15 V power supply that can supply at least 100 A and connect it to a heater with a resistance of 0.15 ohms. 15/0.15 = 100, so 100 A would flow. 15 * 100 = 1500, so once again you would be delivering 1500 W.

So, is there any difference?

It turns out that there's actually a major difference. Suppose you connected the two ends of your heater to your power supply with two wires like the ones in your project kit, but each 5 feet long. That's 10 feet of 22 gauge wire in total, which has a resistance of around 0.16 ohms. **In the high current case, that's roughly the same resistance as your heater.**

That means that while you thought that you would get 100 A flowing, but you'll really only get around half as much. What's worse, half of the heat will be delivered to the wires, which are presumably outside of the toaster oven, so you actually only get 1/4 of the power you thought delivered to the oven itself. But it gets even worse-- the 1500/4 = 375 W delivered to the wires is enough to melt the insulation off and possibly start a fire. Oops.

A key figure to remember here is described by the phrase, "ohmic losses." The power dissipated in a resistive element like a wire is {{< katex >}}P = VI{{< /katex >}}, which is the same as {{< katex >}}P = (IR) * I{{< /katex >}} or {{< katex >}}P = I^2R {{< /katex >}}. The implication of this is that generally, when we're building electronics, if we have a choice between high voltage and high current, we choose high voltage, especially when we're trying to push a lot of energy across a long distance, as in [overhead power lines](https://en.wikipedia.org/wiki/Overhead_power_line).

{{< hint danger >}}
**Safety note**

At voltages of 30 V or higher, you need to start being careful about not getting hurt. We will not be doing anything with voltages above 12 V in this class, but it's still good to remember that your body is kind of like a 70k resistor, and 10 mA through your heart can kill you.
{{< /hint >}}

## Voltage regulation

Okay, so we have high voltages because we want to avoid losing all of our energy in the wires leading to our devices. How do we lower the voltage from a high voltage down to the one we want?

The easiest solution is to use a chip called a linear voltage regulator, along with two capacitors. A typical circuit shown below.

![voltage regulator circuit](/img/voltage-regulator-circuit.png)
