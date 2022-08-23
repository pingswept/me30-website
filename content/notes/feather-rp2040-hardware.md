---
title: "Feather RP2040"
draft: false
---

## KRISTEN TO EDIT THIS PAGE TO APPLY TO FEATHER INSTEAD OF ARDUINO


![Top view of Adafruit Feather RP2040](/img/feather-rp2040-top-view.jpg)

## Reference documents

[Adafruit Feather RP2040 schematic](/pdf/schematic-feather-rp2040.pdf)

[Adafruit Feather RP2040 pinout](/pdf/pinout-feather-rp2040.pdf)

## Adafruit Feather RP2040 hardware overview

### UPDATE FOR FEATHER! 

Looking at the picture above, you can see X large chips, some connectors, and a lot of tiny resistors and capacitors. Right in the middle is the microcontroller that acts as the brain of the board. 

It's an Atmel [ATSAMD21G18A-U](https://www.microchip.com/wwwproducts/en/ATsamd21g18), which is an ARM Cortex M0+ running at 48 MHz. The 1827 code on the chip means that this particular chip it was manufactured in week 27 of 2018.

At the left edge of the board, you can see the uBlox NINA W102 module, which is what provides the wifi and Bluetooth connections to the board. This is an Espressif ESP32 microcontroller inside a metal box with a small wifi antenna next to it. Its main advantage is that the module has passed FCC 47 CFR 15 certification, so the Arduino folks can add it to their board without having to go through the tedious and expensive certification process required of everything with a radio transmitter.

At the right edge of the board is the Texas Instruments BQ24195L battery management chip. It watches the USB and battery connectors for power sources and, when both are connected, passes current from the USB port to the battery at the right voltage to charge the battery. The L at the end of the part number indicates that it's a low-current part that can supply only 1.0 A from the battery back to the USB port, rather than the 2.1 A available with the plain BQ24195.

There's one mysterious chip on the board, just to the left of the microcontroller. It has 8 pins and is labeled TW 833 GD3. According to the schematic, the board has an ATECC508 crypto chip on it. Curiously, the ATECC508 datasheet says that, "As part of Microchip’s overall security features, the part mark for all crypto devices is intentionally vague.The marking on the top of the package does not provide any information as to the actual device type orthe manufacturer of the device."

However, the first Google image search result for "TW 833 chip" is an Adafruit board that mentions an ATECC508 device. Hmmm.

## Connectors

The right end of the board has three different connectors. The white, 2-pin connector at the top, right next to the battery chip, is a JST connector for a 1-cell lithium ion battery. The silver connector on the short side of the board is a micro USB connector for communication with a host computer. The white, 5-pin connector at the bottom of the board connects to the I<sup>2</sup>C bus of the M0+, as well as an extra digital pin, power, and ground.

## Wifi

To use the uBlox NINA W102 wifi module on the board, you'll need to install the library called WiFiNINA using `Tools > Manage Libraries` in the Arduino IDE.

A good first step once you've done that is to run the network scanning tool under `File > Examples > WiFiNINA > ScanNetworks`.

You'll see results like this:

```
Please upgrade the firmware
MAC: 24:62:AB:B3:8B:9C
Scanning available networks...
** Scan Networks **
number of available networks:5
0) slownet	Signal: -50 dBm	Encryption: WPA2
1) LinksysSetupE48	Signal: -77 dBm	Encryption: WPA2
2) ARRIS-DFDB	Signal: -80 dBm	Encryption: WPA2
3) Braendle-Net	Signal: -87 dBm	Encryption: WPA2
4) foxyguest	Signal: -89 dBm	Encryption: WPA2
```
Notice that this also tells you the MAC address, which you need if you want to connect to Tufts_Wireless rather than Tufts_Secure.

## Quirks

### 2 mA current limit per pin

The Arduino website claims that the digital I/O pins on the MKR Wifi 1010 can supply 7 mA, but as of October 2020, this not true without enabling a special setting.

It turns out that the pins on the ATSAMD21 processor on the MKR 1010 can run in two modes. In high drive strength mode, they can supply 7 mA. In low drive strength mode, they can supply only 2 mA. The low current mode is the default.

To switch to high drive strength mode, you need to set the high drive strength mode for each pin from which you need more than 2 mA. Here's a function that does that:

```
bool setHighStrengthOutputPinMode( uint32_t ulPin)
{
// Thanks to Fabien, https://github.com/fab672000, for this code.
// Handle the case the pin isn't usable as PIO
if ( g_APinDescription[ulPin].ulPinType == PIO_NOT_A_PIN ) return false;
  EPortType port = g_APinDescription[ulPin].ulPort;
uint32_t pin = g_APinDescription[ulPin].ulPin;
uint32_t pinMask = (1ul << pin);
// enable input, to support reading back values, with pullups disabled and DRVSTR set
  PORT->Group[port].PINCFG[pin].reg=(uint8_t)(PORT_PINCFG_INEN | PORT_PINCFG_DRVSTR) ;
// Set pin to output mode
  PORT->Group[port].DIRSET.reg = pinMask;
return true;
}
```

Full example of usage here: https://gist.github.com/pingswept/c4a8e9aae4df17f11bd23ed20d30f7c3

This issue was reported to the Arduino folks in 2016, but it's still occurring in October 2020: https://github.com/arduino/ArduinoCore-samd/issues/158

### Serial port setup delay

Here's a fun fact I discovered about the Arduino MKR Wifi 1010 today (October 2020): it takes around 1.7 seconds for it to initialize its serial port. If you're finding that the first `Serial.println()`'s that you issue in `setup()` or `loop()` are getting dropped, this is probably why.

Try adding `delay(2000);` after `Serial.begin(9600);`, and I bet it will fix your problems.

## Learning to program your Feather

Adafruit's [CircuitPython Tutorials](https://learn.adafruit.com/welcome-to-circuitpython) are a great resource for Feather newcomers.
