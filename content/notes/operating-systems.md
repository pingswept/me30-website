---
title: "Operating systems"
draft: false
---

So far, we've been programming the Feather microcontroller, which comes with some software on it, but not an operating system. We're now starting with the Raspberry Pi, which runs the operating system called Linux. You'll be familiar with a few other operating systems: Windows and macOS for laptops and iOS and Android for phones.

## On the Feather microcontroller

When you take the Feather out of the box, it has a small chunk of code on it that makes it appear like a USB drive when you plug it in. All it does is listen for USB traffic and return a list of the files stored on the Feather. It can also return the contents of those files and receive new files for storage. That's it.

When we want the Feather to run Python, we give it a chunk of code called something like `circuitpython-7.3.3.uf2`. Then, when the Feather is powered up, that code runs. By default, it looks for a file called `code.py` and then runs that code through the CircuitPython interpreter, which is also contained in the UF2 file.

## On the Raspberry Pi

When you power up the Raspberry Pi, it runs a small chunk of code that looks at its microSD card for more code to execute. Typically, the microSD card contains a large program called the Linux kernel, plus a pile of other programs and libraries.

The main job of the operating system is to do all the boring stuff that computers do in the background, so every programmer doesn't have to write the same code over and over again.

The main jobs that an operating system does are:

* Run a file system. Store files efficiently. Keep track of their names, who is allowed to access them, and when they were last modified.
* Talk to the internet. Connect to a wifi access point and get an IP address. Resolve domain names.
* Run a process scheduler. This is a program that switches back and forth between different programs really fast, so that it seems like they are running at the same time. 
