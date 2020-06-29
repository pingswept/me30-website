---
title: "Projects"
date: 2020-06-29T15:59:30-04:00
draft: false
---
# Projects

## Project #3: Build a useful, electronic thing

Your task is to build something electronic with the following characteristics:

*   It has electronics in it. (A microcontroller is not absolutely required.)
*   It has at least one sensor, i.e something that measures something in the world and makes the device behave differently as a result.
*   It has some kind of output: either a physical actuator or a display. The display can be a remote device, like the screen of your phone. (This might seem easier, but it is not.)
*   It is something you genuinely think will be useful to you (or people you have talked to about the idea) now and 1 year from now.
*   (It does not need to have a custom PCB, but it can if you want. If it has a custom PCB, you must make a working prototype first.)

**Milestone 1: Tell me your plan: Thursday, April 4, 12:00 PM (noon (start of class))**

**Milestone 2: Build a prototype: Tuesday, April 16, 12:00 PM (noon (start of class))**

**Final due date: Thursday, April 25, 12:00 PM (noon (start of class))**

Bring your useful thing to class on April 25; we will all marvel at our devices' utility. You will find it thrilling.

### More details for project #4

If you need parts (like a sensor or a certain kind of motor), I'm happy to order them for you.

## Project #3: Build an electromechanical game

Your task is to build a game with the following characteristics:

*   It is controlled by a microcontroller like an Arduino or Raspberry Pi. (Choose the Arduino unless you're a Pi zealot.)
*   It has at least one electromechanical element that moves, like a motor or a solenoid.
*   It has some kind of user input, like buttons, knobs, joysticks, sensors, or the like.
*   It is at least sort of fun to play. A blinking LED is not a game.
*   (It does not need to have a custom PCB, but it can if you want. If it has a custom PCB, you must make a working prototype first.)

**Milestone 1: Tell me your plan: Tuesday, March 5, 12:00 PM (noon (start of class))**

**Milestone 2: Build a prototype: Thursday, March 14, 12:00 PM (noon (start of class))**

**Final due date: Thursday, March 28, 12:00 PM (noon (start of class))**

Bring your playable game to class on March 28; we will all play each other's games. You will enjoy it.

### More details for project #3

If you need parts (like a sensor or a certain kind of motor), I'm happy to order them for you.

## Project #2: Build an H-bridge motor controller

The second project is to build a motor controller with the following characteristics:

*   It consists of a PCB with screw terminals for power and control lines
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter
*   It has a power LED that lights up when motor power is available
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting.
*   It can be controlled by logic signals from an Arduino.

**Due date (for PCB submission): Tuesday, February 19, 12:00 PM (noon (start of class))**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, forward your order confirmation to brandon.stafford@tufts.edu. That will serve as proof that you submitted your project on time.

### More details for project #2

(I'll add more details here if they're needed.)

## Project #1: Build a breadboard power supply

The first project, as described in some detail in the first class, is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly in a breadboard
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for PCB submission): Thursday, January 31, 12:00 PM (noon (start of class))**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, forward your order confirmation to brandon.stafford@tufts.edu. That will serve as proof that you submitted your project on time.

### More details for project #1

First of all, we're not trying to build anything revolutionary in this project. None of you have ever made a PCB before, so the point is to make something fairly simple to get comfortable with the process. (If you search Amazon for "breadboard power supply", you'll see that you can buy various versions of things like this, though none with the 12 V passthrough, so far as I'm aware.)

The image below shows the rough mechanical constraints for the PCB. You can make a board of whatever dimensions you want, but it needs to plug into the breadboard, hence the pin location dimensions.

![](img/breadboard-supply-mechanical-design.png)

In the first class, I'll hand out all the [components](components.html) you'll need to build a prototype of your power supply on a breadboard. You build the prototype and make sure that you've got the wiring right. Then, make the PCB with the same connections. Finally, when your PCB arrives in the mail, you can reuse the prototype components on your PCB.

To improve heat dissipation, you will want to use your PCB as a heatsink for the regulators. The TA from 2018, Dominic Guri, has made a [KiCAD PCB footprint for the TO-220 package](to-220-horizontal-footprint.kicad_mod) to help with that. You should put it into a folder called `volt-reg.pretty`, or something like that. (The ending `.pretty` is what matters to KiCAD.)

Put that folder in C:\Program Files\KiCad\share\kicad\modules on Windows or /Library/Application Support/kicad/modules on MacOS. Then, you can add that library to Kicad using Preferences > Footprint Libraries in the footprint association window.

**Note that the pins on the two regulators are not in the same order!**
