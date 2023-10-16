---
title: "KB2040 hardware"
draft: false
---

![Top view of Adafruit KB2040](/img/KB2040_top.jpeg)

## Reference documents

[Adafruit KB2040 pinout](/img/KB2040_Pinout.pdf)

[Adafruit KB2040 schematic](/img/KB2040_Schematic.png)

[Adafruit KB2040 complete guide](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-kb2040.pdf)

## Adafruit KB2040 hardware overview

Looking at the picture above, you can see 2 large chips, some connectors, and a lot of tiny resistors and capacitors. 

The chip just to the right of center is the microcontroller that acts as the brain of the board. It's an [RP2040 chip](https://www.raspberrypi.com/products/rp2040/), which has dual ARM Cortex M0+ cores running at 133 MHz. The 21/19 code on the chip means that this particular chip was manufactured in week 19 of 2021. The RP means that it is made by Raspberry Pi.

The square chip closer to the lower left corner of the board is the Flash memory chip for storing files and code.

Adafruit provides a handy [overview](https://learn.adafruit.com/adafruit-kb2040/pinouts) of all the KB2040 components and pins.

## Why are there no header pins?

The KB2040 is shipped without header pins to keep costs low and to give users options for how they attach sensors and actuators to it. Users can decide whether and which header pins to solder to the  PCB. 

In ME 30, you'll want to be able to plug your KB2040 into a breadboard for stability and wiring. Find the header pins in the ziploc bag in your ME 30 box, and solder them onto the KB2040 PCB. Before you do this, check out [Adafruit's soldering tutorial](https://learn.adafruit.com/how-to-solder-headers/male-headers).


## Connectors

The board has two different connectors. On the left of the board is a USB-C connector used for power and/or data. You'll connect to your computer through USB-C to install CircuitPython on your KB2040 and to edit code. On the right edge of the board is a STEMMA QT connector, which allows you to connect I2C sensors and breakout boards to the KB2040.

## Buttons

You'll notice two small black buttons encased in silver boxes. The **RST (reset) button** resets the board without disconnecting it from power. The **BOOT (boot select) button** is used when you install or update CircuitPython on your KB2040 (press and hold BOOTSEL while plugging the board into USB or pressing RESET). This button is also usable as an input in CircuitPython code, on pin <<board.BUTTON>>. 

## LEDs

The KB2040 has two built-in LEDs. 

The one above the USB-C connector is the **green power LED** that indicates whether the board is receiving adequate power.
- green blink = code finished; no error
- red blink = code ended due to Python error
- yellow blink = safe mode; no user code run; check serial monitor

The **NeoPixel LED** to the left of the RESET (RST) button can be programmed to glow in different colors using the variable board.NEOPIXEL and the code in the NeoPixel library.

## Quirks

### To be added as we encounter them (e.g., current limits per pin; serial port delay)


## Learning to program your KB2040

In ME 30 you'll install CircuitPython on your KB2040 so that it can run Python programs. We'll use these [CircuitPython set-up instructions provided by Adafruit](https://learn.adafruit.com/adafruit-kb2040/circuitpython).

Adafruit's more general [CircuitPython Tutorials](https://learn.adafruit.com/welcome-to-circuitpython) are a great resource for newcomers to the world of microcontrollers.
