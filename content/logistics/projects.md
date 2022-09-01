---
title: "Projects"
draft: false
---
# Projects


## Project #1: Build a breadboard power supply

The first project is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for PCB submission): Thursday, September 22, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time.

### More details for project #1

First of all, we're not trying to build anything revolutionary in this project. None of you have ever made a PCB before, so the point is to make something fairly simple to get comfortable with the process. If you search Amazon for "breadboard power supply", you'll see that you can buy various versions of things like this, though none with a 12 V passthrough, so far as we're aware.

Here's what a typical one of these things looks like.

![breadboard power supply](/img/breadboard-power-supply-from-amazon.jpg)

The image below shows the rough mechanical constraints for the PCB. You can make a board of whatever dimensions you want, but it needs to plug into the breadboard, so you probably want to follow the pin location dimensions shown below. You don't have to have pins where all of the 8 red dots are-- you could get by with just 4, but 8 will make the board stay in place a little more securely.

![](/img/breadboard-supply-mechanical-design.png)

In your project kit, you'll find all the components you'll need to build a prototype of your power supply on a breadboard. You build the prototype and make sure that you've got the wiring right. Then, make the PCB with the same connections. Finally, when your PCB arrives in the mail, you can reuse the prototype components on your PCB.

{{< hint danger >}}
**Important note: the pins on the two regulators are not in the same order!**
{{< /hint >}}

Check the datasheets for the components to see which pin is the input pin, which is the output pin, and which should connect to ground.


### P1 prototype: what you should do before class #3

1. Make it so that 12 V goes into your circuit and 5 V comes out.
2. Install Kicad.
3. Try to replicate in Kicad the schematic of the circuit that you started building in the first class.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. Read and try to make sense of the web pages listed under ["What to study" on the calendar](http://andnowforelectronics.com/logistics/calendar/)
6. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.

## Project #0: Power an LED with "wall" power through our DC power supply. Control it with a push button.

The getting-started "project" is really more of a warm-up activity, and we'll do it together in class. The goal is to create a circuit on your breadboard that powers an LED with power from the wall, directed through your kit's DC power supply.  This circuit should have the following characteristics:

*   It is implemented on a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It turns on an LED when a push button is pressed.

**Due date (for submitting a photo of your circuit to Canvas): Thursday, September 8, 11:59 PM**

