---
title: "Low power/high power"
draft: false
---

## Controlling high power with low power

## Electromechanical relays

Before transistors, and still in some cases today, we used electromechanical relays to control large currents. The basic idea of a relay is that you've got a little coil of wire in a tiny box. You run a small current through the wire, which makes a magnetic field, which pulls a little metal lever, closing a circuit that can handle a lot of current.

![An electromechanical relay](/img/relay.png)

Relays have a few major advantages.
* You can hear and see them open and close. (Usually, they're in a clear plastic box.)
* They are simple to understand.
* They can provide isolation between a high voltage circuit and a low voltage circuit. (A relay used for this purpose, like in a golf cart, is called a contactor.)

Everything else about them is terrible.

* They're slow.
* They're relatively unreliable.
* They're expensive to make.
* They're big.
* They require a relatively large current to operate.
* If you badly overload them, they weld shut.

In general, you probably shouldn't use relays unless you need a safety circuit that pops open when the power fails, like in a table saw, or somebody gives you a pile of relays.

## The new hotness: transistors

There's a huge amount to learn about transistors; the topic can be overwhelming. First, let's narrow things down to just two common varieties of transistor and explain two ways each can be used.

## Bipolar junction transistor (BJT)

If someone just says "transistor" to you, they probably mean a bipolar junction transistor, or BJT. If someone mentions an NPN or PNP transistor, they are also talking about BJT's.

The fundamental characteristic of a BJT is that it is a **current-controlled device**: putting a small amount of current through one leg of the device allows a larger current to flow through another leg of the device.

## Metal oxide semiconductor field effect transistor (MOSFET)

MOSFETs are a newer variety of transistor than BJTs. If someone mentions an N-channel or P-channel device, they're usually talking about a MOSFET.

The fundamental characteristic of a MOSFET is that it's a **voltage-controlled device**: raising the voltage on one leg of the device (the gate) reduces the resistance between two other legs of the device (the drain and source).

## Two ways to use a transistor

There are two major ways that a transistor can be used: as an **amplifier** or a **switch**. In digital electronics, which has largely superseded analog electronics over the last few decades, we largely use transistors as switches rather than amplifiers.

(It should be noted here that because physical phenomena are, in reality, analog in nature, at the lowest levels, electronics will always be analog. But, for everyday engineering tasks, you will largely encounter digital devices. If the analog stuff is interesting to you, dive into it; a deeper understanding of analog stuff can only benefit you.)
