---
title: "Operating systems"
draft: false
---

So far, we've been programming the Feather microcontroller, which comes with some software on it, but not an operating system. We're now starting with the Raspberry Pi, which runs the operating system called Linux. You'll be familiar with a few other operating systems: Windows and macOS for laptops and iOS and Android for phones.

## On the Feather microcontroller

When you take the Feather out of the box, it has a small chunk of code on it that makes it appear like a USB drive when you plug it in. All it does is listen for USB traffic and return a list of the files stored on the Feather. It can also return the contents of those files and receive new files for storage. That's it.

When we want the Feather to run Python, we give it a chunk of code called something like `circuitpython-7.3.3.uf2`. Then, when the Feather is powered up, that code runs. By default, it looks for a file called `code.py` and then runs that code through the CircuitPython interpreter, which is also contained in the UF2 file.

## On the Raspberry Pi
