---
title: "Analog vs. digital"
draft: false
---
## Analog vs digital

When you first start learning about electronics, we talk a lot about voltage and current. You do a bunch of calculations about resistance using Ohm's law. Then, as soon as you get into microcontrollers, it's just **voltage, voltage, voltage**. We stop talking about current almost completely. This might seem mysterious, but it's just because you're studying electronics after the victory of digital communication.

When we say "analog," we mean a signal that varies smoothly in time-- it doesn't jump around discontinuously. An analog signal could be either a voltage or a current, the value of which represents a sensor reading, like temperature.

When we say "digital," we mean a signal that bounces back and forth between full-on and full-off (commonly 3.3 V and 0 V). The pattern or timing of the jumps encodes a sensor reading, like temperature. (In truth, even digital signals are analog, as no voltage can change truly instantaneously.)

## The past

In the past, we largely used analog signals to communicate between systems. A pressure sensor would put out a signal that ranged from 0-10 V, proportional to the pressure of the tank it was stuck in. We also had current loop sensors, where a flow sensor would send a current that ranged from 4-20 mA through a loop that was proportional to the flow rate of the fluid in the pipe it was measuring.

Those analog systems worked effectively for decades. They were simpler to understand and maintain than our modern digital systems. In large industrial processes, like mixing vats of chemicals, 4-20 mA sensors are still widely used. (Why not 0-20 mA? Making 4 mA the bottom end of the range means that you can tell the difference between your lowest sensor reading (4 mA) and a broken sensor (0 mA), which is cool.)

We also still use analog signals for radio transmission of many kinds, and lots of sensors rely on analog phenomena, which are quickly converted to digital signals for transmission, but are still analog at their core.

## Now: the victory of digital

But, analog systems have some major disadvantages: noise susceptibility and power consumption.

Electrical noise is everywhere. If you are using an analog sensor, and someone turns on a microwave oven that is leaking 2.450 GHz noise all over the place, your analog sensor readings may get corrupted. Once the noise gets into your system, you can't tell whether the real reading should be, for example, 1.2 V or 1.3 V.

With digital systems, you categorize the bits that are transmitted as either 0 or 1, so the noise has to be pretty bad before corruption occurs. Even after that, you can do error correction. For example, after every 8 bits, you could send a bit that corresponds to whether the last 8 bits should have contained an odd or even number of 1's. (This is called a parity bit; it used to be popular. Now we use more complicated error correction schemes, but you get the idea.)

Another weakness of analog systems is power consumption. A typical 4-20 mA sensor running at 24 V might consume an average of 300 mW. For comparison, a 3.3 V digital signal running into an microcontroller input with leakage of 15 nA is consuming 50 nW, or 6 million times less power.

So now, most sensors have digital outputs, and most chips communicate with each other through digital signals like I2C or SPI.
