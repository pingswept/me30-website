---
title: "H-bridge motor driver"
date: 2020-06-28T16:58:30-04:00
draft: false
---
# The H-bridge motor driver

## What is an H-bridge and why would I want one?

An H-bridge is a simple, commonly used circuit that can make motors spin in both directions. When you draw a schematic of the circuit, it looks kind of like the letter H, with the motor bridging the two sides of the circuit.

Conceptually, the circuit consists of 4 switches. When they're all off, the motor is stopped. When you turn on the upper left and lower right, current flows one way, and the motor spins. When you turn on the upper right and lower left, current flows the other way, so the motor reverses.

![H-bridge concept](/img/bjt-h-bridge.jpg)

For small, low-power motors, you can get chips that contain all 4 switches in a single package. As motors get bigger, we start using 4 separate MOSFETs for the 4 switches.

## What kind of MOSFETs do we use?

Typically, the lower two MOSFETs in the circuit are N-channel MOSFETs, while the upper two are P-channel. (If the upper ones were N-channel, you would need a higher gate voltage to turn them on, which is inconvenient.) A good starting point would be the IRLB8721 MOSFET for the N-channels and the FQP27P06 MOSFET for the P-channels. Both MOSFETs are cheap (around $0.80 from a US distributor) and widely available. They can handle 25-30 A when on and withstand 60 V when off.

![H-bridge with MOSFETs](/img/mosfet-h-bridge.jpg)

## Don't I still need high voltage to turn off the P-channels?

Yes, you do. The trick that people use is to a low power NPN bipolar junction transistor, like the 2N3904, to turn on the P-channels, and then a pull-up resistor to turn them off. Then you can control the P-channels through the BJT's using 3.3 V or 5 V logic signals from a microcontroller.

![Left half of an H-bridge with MOSFETs and a BJT](/img/half-h-bridge.jpg)

## But if we have to use a BJT, why not use that instead of the MOSFET? Why both?

The 2N3904 costs around $0.01, i.e. it is approximately free, but it can only handle around 0.5 A. You could instead get a larger power transistor. In some circumstances, people do that, but H-bridges tend to be pulsed on and off very quickly (hundreds or thousands of times per second) for speed control. MOSFETs require much less energy to turn on and off than BJTs, so the MOSFETs make the circuit more efficient. At really high currents (hundreds of amps, say for an electric car), people switch from MOSFETs to a weird hybrid of the two called an insulated gate bipolar transistor. IGBT's are cool, but they're also more expensive. Stick with the MOSFETs for now.
