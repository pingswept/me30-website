---
title: "LEDs"
draft: false
---

## Light-emitting diodes (LEDs)

A diode is a piece of semiconductor, usually silicon or germanium, that blocks current flow in one direction. Light-emitting diodes have the exciting property that when current flows in the other direction, light comes out. I could try to write something hand-wavy about bandgaps here to explain how they work, but the truth is that they're like magic to me.

LEDs have the irritating property that they respond nonlinearly to voltage. If you were to hook an LED up to an adjustable voltage source and then slowly raise the voltage, at first, no light would come out. Then, suddenly, around 2 or 3 volts, the LED would start emitting light. Shortly after that, it would overheat and burn out.

The voltage at which the LED emits light is called the forward voltage. When you include an LED in a circuit, typically you'll want to include a [resistor to limit the current](/notes/resistors/#typical-application-current-limiter) drawn by the LED. With a properly-sized resistor, this allows the LED to conduct at its forward voltage, while the resistor prevents it from burning out.

Oddly, the forward voltage of an LED varies with its color.

![5 mm LED innards](/img/led-5mm-green.svg)
