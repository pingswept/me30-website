---
title: "Projects"
draft: false
---

## Project 1: 
**Build a breadboard power supply**

The first project is to build a power supply that meets the following requirements:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for Printed Circuit Board submission): Friday, September 27, 6:00PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time. If this cost is a hardship, please email your KiCad files to Brandon or Kristen, and we will order it for you.

### More details for Project 1

First of all, we're not trying to build anything revolutionary in this project. None of you have ever made a PCB before, so the point is to make something fairly simple to get comfortable with the process. If you search Amazon for "breadboard power supply", you'll see that you can buy various versions of things like this, though none with a 12 V passthrough, so far as we're aware.

Here's what a typical one of these things looks like.

![breadboard power supply](/img/breadboard-power-supply-from-amazon.jpg)

The image below shows the mechanical constraints for the PCB. You can make a board of whatever dimensions you want, but it needs to plug into the breadboard, so you probably want to make sure that the pins line up with the holes in the breadboard, as shown below. You can get by with 4 pins, but 8 will make the board stay in place a little more securely. Regardless of how many pins you use, make sure that each rail has only matching pins, i. e. don't accidentally connect 5 V to GND.

The dimension between the outer pins is estimated at 1.9 inches. It would be a really good idea to verify that dimension on your breadboard. Sometimes the breadboards are a little wider or narrower.

You can rely on the rest of the dimensions being quite accurate.

![](/img/breadboard-supply-mechanical-design.png)

In your project kit, you'll find all the components you'll need to build a prototype of your power supply on a breadboard. You build the prototype and make sure that you've got the wiring right. Then, make the PCB with the same connections. Finally, when your PCB arrives in the mail, you can reuse the prototype components on your PCB.

{{< hint danger >}}
**Important note: the pins on the 5V and 3.3V regulators are not in the same order!**
{{< /hint >}}

Check the datasheets for the components to see which pin is the input pin, which is the output pin, and which should connect to ground.

If you feel like you understand this project pretty well, or if you've made a basic circuitboard before, you could try adding additional features. Look at the open source [Ant breadboard power supply](https://www.crowdsupply.com/digital-cool/ant-bbps) for inspiration. The [schematics are available](https://gitlab.com/DigitalUncool/ant/-/blob/main/Hardware) if you're curious about the details.

![Project 1 main steps](/img/P1_flowchart.jpg)

### P1 prototype: what you should do before class #5 (before Wed., 9/18)

1. Read and try to make sense of the website notes on [voltage regulation](http://andnowforelectronics.com/notes/voltage-regulation/). Pay special attention to the circuit diagram showing the L7805C voltage regulator.
2. Try your best to make a breadboard circuit so that 12 V goes into your circuit and 5 V and 3.3 V come out. To get started, see the [schematic on the Voltage Regulators web page](http://andnowforelectronics.com/notes/voltage-regulation/). You'll need to use your [5V and 3.3V voltage regulator components](http://andnowforelectronics.com/notes/datasheets/#voltage-regulators).
3. Install Kicad, [version 7.0.11](https://www.kicad.org/blog/2024/02/KiCad-7.0.11-Release/) for the most bug-free experience.
4. Watch Brandon and Kristen's Kicad [demo videos](http://andnowforelectronics.com/notes/demo-videos/#kicad-for-project-1) 
5. Read as much of chapter 2 from the Practical Electronics textbook as you can.


## Project 0: 
**Create a secure motor attachment**

Later this semester, Projects 2 and 4 will require using a motor to actuate some part of an interactive game, and Projects 5 and 6 will involve motor-driven wheels. So in Project 0, you’ll building some knowledge about how to attach a part securely to a motor.

Your task in Project 0 is to design and build a motor hub that meets the following requirements:

*	  It fits on and attaches to your DC motor shaft
*	  It includes a 3 mm hole located 15 mm from the central axis of your DC motor shaft (you’ll insert a paper clip with a weighted string into this hole)
*	  It stays attached securely enough to handle the amount of torque (load applied to hub) that stalls the motor when it is operating at 12 V

Your motor hub can be shaped like a spool, lever arm, or anything; the details are up to you.

![](/img/motor-hub-diagram.jpg)

Submit to Canvas (1) a photo of your motor hub and (2) a brief video (max 90 seconds) demonstrating that your motor hub meets the requirements above.

Bring your hub to lab on your designated due date. We hope to compile everyone’s results into a histogram showing the range of torques applied before the hubs either (a) slip on their motor shaft or (b) successfully stall the motor.

Due dates are staggered for Project 0 to spread out the demand on fabrication tools at Nolop and Bray. Your hub is due at the start of lab time on the date listed for your weekly lab day.

| Your Weekly Lab Day |  Your Project 0 Due Date | 
|---------------------|-------------------------|
| Monday         |  Mon., Oct. 7      | 
| Tuesday        |  Tues., Oct. 1      | 
| Wednesday      |  Wed., Sep. 25      | 
| Thursday       |  Thurs., Sep. 19    | 


{{< expand "Click for info on preparing to use the Bray Shop 3D printers, laser cutter, or lathe" "..." >}}
All students must complete the Bray [safety quiz](https://sites.tufts.edu/brayprivate/safety-quiz-complete-to-access-shop-spaces/) prior to their first visit to Bray. Completing the quiz will give you access to the Bray user site where you can submit appointment requests for training and fabrication time. 

Use of the Bray lathe requires lathe-specific training in the red zone, which must be booked by appointment.

ME and HFE students can use the Bray 3D printers anytime using their Bray building access. 

Students can book an appointment to use the laser cutter or just walk in to use it during shop open hours as long as it is not reserved or in use by someone else.
{{< /expand >}}


{{< expand "Click for info on preparing to use the Nolop 3D printers or laser cutter" "..." >}}
For more information about the Nolop 3D printers, review the training guide [here](https://nolop.org/3dprint/).

Tutorials on using the Nolop laser cutter are available on the Nolop website [here](https://nolop.org/laser/).
{{< /expand >}}

{{< expand "Click to see procedure for motor hub testing" "..." >}}
Work with your entire lab section. Using water bottles and a scale, create a set of 8 different weights ranging from the weight of an empty bottle to the weight of a full bottle. (Yes, each group of 8 will have a different set of 8 weights, but as long as you have a range, your group will be able to do this activity.)

For each motor hub, begin with the lowest weight and attach it to the hub with a paper clip (through the hole placed ~15 mm from the shaft axis) and a length of string. Supply 12 V to the motor and see if it can lift the weight without slipping of the hub. If it succeeds, move on to the next highest weight. Repeat until you get to a weight that either stalls the motor or makes the hub slip around the motor shaft.  Record this as your "slip/stall weight." 

Multiply your hub's "slip/stall weight" by the distance between your shaft axis and your paper clip attachment point (it should be 15 mm, but measure just to be sure).  The result is your "slip/stall torque."

Submit to Canvas a photo of your motor hub attachment and a video of it lifting weights. Compare its performance to this class histogram created in a previous semester: 
https://docs.google.com/spreadsheets/d/1Y_V_8rgQhnSgg5z3wRCmGc2mLD-aFtRIoKs-uJ67k6A/edit?usp=sharing
{{< /expand >}}

![](/img/motor-hub-examples.png)

Prior Student Examples

![motor hub collage](/img/MotorHubCollage.jpg)
