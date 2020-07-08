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

## Kirchhoff's Current and Voltage Laws

There are two rules that can be useful in thinking about electricity flowing in circuits. When mathematicians and similar notation enthusiasts describe Kirchhoff's current law, they do it like this:
{{< katex display >}}
\sum_{k=1}^{n} I_k = 0
{{< /katex >}}
The letter {{< katex >}}I{{< /katex >}} refers to current, because, [according to Wikipedia](https://en.wikipedia.org/wiki/Electric_current#Symbol), it was long ago an abbreviation for *intensité du courant*. So the idea is that if you add up all the currents going in or out of any point in an electrical circuit, the currents will always add up to zero. But that's a weird way of saying something that you all already understand in a different context, which is that all the water that goes into a network of pipes also comes out of that network of pipes.

For example, take a pipe with 7 liters/minute flowing into it, which splits into two pipes. One of the pipes has 4 liters/minute coming out of it. **How many liters per minute are coming out of the other pipe?**

{{< expand "See the answer" "..." >}}
That's right, it's 3 liters/minute, because {{< katex >}}7 - 4 = 3{{< /katex >}}, or, as the mathematicians would say, {{< katex >}}7 - 4 - 3 = 0{{< /katex >}}.
{{< /expand >}}

{{< katex display >}}
\sum_{k=1}^{n} V_k = 0
{{< /katex >}}
