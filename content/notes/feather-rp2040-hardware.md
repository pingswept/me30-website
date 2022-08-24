---
title: "Feather RP2040"
draft: false
---

![Top view of Adafruit Feather RP2040](/img/feather-rp2040-top-view.jpg)

## Reference documents

[Adafruit Feather RP2040 schematic](/pdf/schematic-feather-rp2040.pdf)

[Adafruit Feather RP2040 pinout](/pdf/pinout-feather-rp2040.pdf)

[Adafruit Feather RP2040 complete guide](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-rp2040-pico.pdf)

## Adafruit Feather RP2040 hardware overview

Looking at the picture above, you can see 2 large chips, some connectors, and a lot of tiny resistors and capacitors. 

The chip just to the right of center is the microcontroller that acts as the brain of the board. It's an [RP2040 chip] (https://www.raspberrypi.com/products/rp2040/), which has dual ARM Cortex M0+ cores running at 133 MHz. The 20/43 code on the chip means that this particular chip it was manufactured in week 43 of 2020. The RP means that it is made by Raspberry Pi.

The square chip closer to the upper right corner of the board is the Flash memory chip for storing files and code.

Adafruit provides a handy overview of [all the Feather RP2040 components and pins] (https://learn.adafruit.com/adafruit-feather-rp2040-pico/pinouts).

## Connectors

The board has three different connectors. On the left of the board is a USB-C connector used for power and data. You'll connect to your computer through USB-C to install CircuitPython on your Feather and to edit code. The black connector on the top left of the board is a JST connector for a 4.2/3.7V lithium polymer (LiPo) or lithium ion (LiIon) battery. If your Feather is powered by USB and has a battery attached to this port, it will re-charge the battery. On the right edge of the board is a STEMMA QT connector, which allows you to connect I2C sensors and breakout boards to the Feather.

## Buttons

You'll notice two small black buttons encased in silver boxes. The BOOTSEL button is used when you install or update CircuitPython on your Feather (press and hold BOOTSEL while plugging the board into USB or pressing RESET). The RESET button resets the board without disconnecting it from power.

## LEDs

The Feather has three built-in LEDs. On the left edge of the board, above and below the USB-C connector, are two small LEDs. 

The one labeled 13 is a red LED connected to pin D13. You can easily turn it on and off in CircuitPython code using the variable board.LED. It also indicates bootloader mode by pulsing. 

The LED labled CHG indicates the charge status of a connected battery. If no battery is in place, this LED might flicker as the charge circuitry tries to detect whether there is a batter or not.

The NeoPixel LED indicates the runtime status of CircuitPython code. It can also be programmed to glow in difference colors using the variable board.NEOPIXEL and the code in the NeoPixel library.

## Quirks

### To be added as we encounter them (e.g., current limits per pin; serial port delay)


## Learning to program your Feather

Adafruit's [CircuitPython Tutorials](https://learn.adafruit.com/welcome-to-circuitpython) are a great resource for Feather newcomers.
