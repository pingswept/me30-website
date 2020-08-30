---
title: "Voltage and current"
draft: false
---
## What's the difference between voltage and current?

Voltage and current are the two ways we measure electricity, like we use pressure and flow rate to describe water flow in a pipe.

## Current

Current is easier, so let's start with that. Current is a measure of how many electrons are flowing past a point per second. Current is measured in amperes, called amps for short, and abbreviated "A". 1 amp means that 6.24 x 10<sup>18</sup> electrons per second are flowing. That's 6.24 quintillion electrons. Physicists call that number of electrons a coulomb. A chemist might call it around 100 micromoles. A baker might call it 500 quadrillion dozens of electrons. It's a lot of electrons.

To give you an idea of scale, microcontrollers and phones run on currents of 1-100 mA ("mA" is a milliamp). A blender or a vacuum cleaner might pull 1-15 A. (Wall outlets are rated for 15 A before a circuit breaker trips, usually.) Electric cars draw 100-1000 A.

## Voltage

But current doesn't tell the whole story. Voltage tells the rest. Voltage is a measure of potential energy per electron.

**Need more explanation of voltage here**

**Maybe something like this? (from Kristen)**

While current tells us about the rate at which electrons are flowing, and those electrons have some potential to transfer energy, the value of the current doesn’t tell us how MUCH energy the electrons are transferring each second.  To know that, we have to know how much voltage is applied. Voltage - also called potential difference - tells you where energy is converted in a circuit. If there’s a difference in voltage across something, then that thing has transferred electrical energy to some other form.

Voltage has an “energy” definition and a “practical” definition. The energy definition is that 1 volt equals 1 joule per coulomb. In other words, voltage is the energy supplied per unit of charge. If 1 volt is applied, 1 joule of energy will be applied to each unit of charge in a circuit. That’s like giving each charge enough energy to lift 1 Newton 1 meter, it it could convert the energy perfectly. The practical definition of 1 volt is 1 watt per 1 amp. It's the power consumed per unit of current drawn by a device. If 1 volt is applied, 1 watt of power will be consumed for each 1 amp of current.

A lot of us have the equation for Ohm’s law, V = iR, committed to memory. But Ohm's law should not be viewed as a definition of voltage. Instead, it defines resistance, as the ratio of the voltage applied to the resultant current flow. 

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_ok1imbkt&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_xafzjzsr" width="736" height="450 allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_7ke8jg2l&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_rpv1gktr" width="400" height="285" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Kirchhoff's Current Law

There are two rules that can be useful in thinking about electricity flowing in circuits. When mathematicians and similar notation enthusiasts describe Kirchhoff's current law, they do it like this:
{{< katex display >}}
\sum_{k=1}^{n} I_k = 0
{{< /katex >}}
The letter {{< katex >}}I{{< /katex >}} refers to current, because, [according to Wikipedia](https://en.wikipedia.org/wiki/Electric_current#Symbol), it was long ago an abbreviation for *intensité du courant*. So the idea is that if you add up all the currents going in or out of any point in an electrical circuit, the currents will always add up to zero. But that's a weird way of saying something that you all already understand in a different context, which is that all the water that goes into a network of pipes also comes out of that network of pipes.

For example, take a pipe with 7 liters/minute flowing into it, which splits into two pipes. One of the pipes has 4 liters/minute coming out of it.

![Water flowing through pipes](/img/kirchhoff-pipe-example.png)

**How fast is water coming out of the other pipe?**

{{< expand "See the answer" "..." >}}
That's right, it's 3 liters/minute, because {{< katex >}}7 - 4 = 3{{< /katex >}}, or, as the mathematicians would say, {{< katex >}}7 - 4 - 3 = 0{{< /katex >}}.
{{< /expand >}}

Now let's try the same thing with electricity. We have a circuit where 7 mA are flowing into a junction. 4 mA are coming out one wire.

![Electricity flowing through wires](/img/kirchhoff-current-example.png)

**How much current is coming out of the other wire?**

{{< expand "See the answer" "..." >}}
Hey, you did it! 3 mA is right!
{{< /expand >}}

## Kirchhoff's Voltage Law

Unfortunately, there is another law that is also typically taught in an obfuscated way: Kirchhoff's voltage law, which is that the sum of the voltages around any loop is zero.

{{< katex display >}}
\sum_{k=1}^{n} V_k = 0
{{< /katex >}}

But you know how to use a tape measure, right?

![A 6 foot tall man](/img/kirchhoff-height-example.png)

If I am 6 feet tall, and it's 2 feet from the bottom of my feet to my knees, how far is it from my knees to the top of my head?

{{< expand "See the answer" "..." >}}
Yes, 4 feet is correct. Well calculated.
{{< /expand >}}

Voltage works the same way.

![Battery resistor, led loop](/img/kirchhoff-voltage-example.png)

If you have a circuit run by a 6 V battery, and there is a 2 V drop across the LED, how many volts are there across the resistor?

{{< expand "See the answer" "..." >}}
Hey, you did it again! 4 V is right!
{{< /expand >}}
