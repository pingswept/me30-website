---
title: "Projects"
draft: false
---

# Project 1: Build a breadboard power supply

The first project is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for Printed Circuit Board submission): Wednesday, September 27, 10:30AM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time.

### More details for project 1

First of all, we're not trying to build anything revolutionary in this project. None of you have ever made a PCB before, so the point is to make something fairly simple to get comfortable with the process. If you search Amazon for "breadboard power supply", you'll see that you can buy various versions of things like this, though none with a 12 V passthrough, so far as we're aware.

Here's what a typical one of these things looks like.

![breadboard power supply](/img/breadboard-power-supply-from-amazon.jpg)

The image below shows the rough mechanical constraints for the PCB. You can make a board of whatever dimensions you want, but it needs to plug into the breadboard, so you probably want to follow the pin location dimensions shown below. You don't have to have pins where all of the 8 red dots are-- you could get by with just 4, but 8 will make the board stay in place a little more securely.

![](/img/breadboard-supply-mechanical-design.png)

In your project kit, you'll find all the components you'll need to build a prototype of your power supply on a breadboard. You build the prototype and make sure that you've got the wiring right. Then, make the PCB with the same connections. Finally, when your PCB arrives in the mail, you can reuse the prototype components on your PCB.

{{< hint danger >}}
**Important note: the pins on the 5V and 3.3V regulators are not in the same order!**
{{< /hint >}}

Check the datasheets for the components to see which pin is the input pin, which is the output pin, and which should connect to ground.

If you feel like you understand this project pretty well, or if you've made a basic circuitboard before, you could try adding additional features. Look at the open source [Ant breadboard power supply](https://www.crowdsupply.com/digital-cool/ant-bbps) for inspiration. The [schematics are available](https://gitlab.com/DigitalUncool/ant/-/blob/main/Hardware) if you're curious about the details.

### P1 prototype: what you should do before class #4 (before Mon., 9/18)

1. Read and try to make sense of the website notes on [voltage regulation](http://andnowforelectronics.com/notes/voltage-regulation/). Pay special attention to the circuit diagram showing the L7805C voltage regulator.
2. Try your best to make a breadboard circuit so that 12 V goes into your circuit and 5 V comes out, as shown on the [website diagram](http://andnowforelectronics.com/notes/voltage-regulation/). You'll need to use your [5V voltage regulator component](http://andnowforelectronics.com/notes/datasheets/#voltage-regulators).
3. Install Kicad.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.


# Project 0: Create a secure motor attachment

Later this semester, Projects 2 and 4 will require using a motor to actuate some part of an interactive game, and Projects 5 and 6 will involve motor-driven wheels. So in Project 0, you’ll building some knowledge about how to attach a part securely to a motor.

Your task in Project 0 is to design and build a motor hub that meets the following specifications:

-	Fits on and attaches to your DC motor shaft
-	Stays attached securely enough to handle the amount of torque that stalls the motor when it is operating at 12 V
-	Provides a 3 mm hole 15 mm from the central axis of your DC motor shaft (you’ll insert a paper clip with a weighted string into this hole) 
-	Shaped like a spool or lever arm or anything (i.e., shape is up to you)

![](/img/motor-hub-diagram.jpg)

Submit to Canvas both (1) a CAD rendering of your hub design and (2) a photo your actual hub, and bring it to lab on your designated due date. We will compile everyone’s results into histogram showing the range of torques applied before the hubs either (a) slip on their motor shaft or (b) successfully stall the motor.

Due dates are staggered for Project 0 to spread out the demand on fabrication tools at Nolop and Bray. Your hub is due at the start of lab time on the date listed for your weekly lab day.

| Your Weekly Lab Day |  You Project 0 Due Date | 
|---------------------|-------------------------|
| Sunday         |  Sun., Sep. 24      | 
| Monday         |  Mon., Sep. 25      | 
| Tuesday        |  Tues., Oct. 1      | 
| Wednesday      |  Oct. 11            | 
| Thursday       |  Thurs., Sep. 14    | 
| Friday         |  Fru., Sep. 15      | 
