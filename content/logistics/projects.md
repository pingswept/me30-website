---
title: "Projects"
draft: false
---
## Project 3: Build an H-bridge motor controller

The third project is to build a motor controller with the following characteristics:

*   It consists of a PCB with connectors for a motor, plus power and control lines.
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It has a power LED that lights up when motor power is available.
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting.
*   It can be controlled by logic signals from a KB2040.  

Here is a graphical version of those first two bullet points about connectors.

![P2 connectors](/img/P2-connectors.jpg)


<!-- <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_708qmkve&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_mtijm1x6" width="400" height="285" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>  -->

**Due date for prototype: Monday, October 23, 11:59 PM**

To get started building your prototype H-bridge, review the [Low Power/high power](http://andnowforelectronics.com/notes/low-power-high-power/) and the H-bridge(http://andnowforelectronics.com/notes/h-bridges/) pages, including their mini-lecture videos on BJT and MOSFET transistors. After that, if you're stuck, consult the [H-bridge testing](http://andnowforelectronics.com/notes/demo-videos/#testing-an-h-bridge) demo video.  Note that this video is not intended to give you step-by-step building or testing instructions, but rather to give you a feel for the kind of approach you might take to building and testing this circuit. If your H-bridge prototype isn't working by the deadline for this prototype, don't worry!  Just submit to Canvas a photo of what you have, working or not.  

**Due date for PCB submission: Monday, October 30, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. (If this cost is a hardship, please let Kristen or Brandon know, and we will cover the cost by ordering it for you, no questions asked.) After you submit it, take a screenshot of your order confirmation and upload it to the Project 3 PCB assignment on Canvas (proof that you submitted your project on time). Also, take a screenshot of your PCB design in KiCad and upload that as well (it would be a good idea to save this screenshot for your portfolio). 




## Project 2:
**Build a lame game**

The next project is to use the basic electrical components we've covered in class with some mechanical fabrication to make a game that is at least mildly entertaining. The point here is *NOT* making the best game ever, but to set some goals for testing out your electromechanical skills.

This is a solo project, but we'll be brainstorming in groups.

You should bring your game to class on Monday, October 16th to share with your brainstorming group. 

**Due date (for game documentation submission): Monday, October 16, 11:59PM**

To keep things simple, there are a few required constraints.

Your game should:

* Use the DC gearmotor in your kit
* Require user interaction of some sort (e.g., pushing a button, pressing a key, interacting with a physical component)
* Fit inside a cube 20 cm on a side
* Be fabricated without 3D printing, except for a motor hub if needed (talk to an instructor if you have a particular reason you need to violate this constraint.)

The point of the constraints is to keep your game simple enough that you can complete it in 2 weeks.

In addition to planning to meet these constraints, you should also pick one learning goal for yourself for this project. Open-ended projects offer you an opportunity to bend the curriculum into the direction of your interests or to explore a potential new area of interest. 

Here are some example learning goals:

  * Get more comfortable with cordless drills and at least one other hand tool.
  * Test my system to failure, then rebuild it stronger.
  * Use only recycled/found materials.
  * Complete my project 24 hours early.
  * Model, predict and subsequently measure at least one mechanical property of my project.
  * Complete the project in less than 6 hours of focused effort.
  * Use the laser cutter (which I have never used before).
  * Make at least one part out of steel.
  * Turn a part on a lathe at Bray.
  * Spend at least 1/3 of my effort on the aesthetics of the project.
  * Make my most refined 3D print ever.


## Project 1: 
**Build a breadboard power supply**

The first project is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for Printed Circuit Board submission): Thursday, September 28, 11:59PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time. If this cost is a hardship, please email your KiCad files to Brandon or Kristen, and we will order it for you.

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

![Project 1 main steps](/img/P1_flowchart.jpg)

### P1 prototype: what you should do before class #5 (before Wed., 9/20)

1. Read and try to make sense of the website notes on [voltage regulation](http://andnowforelectronics.com/notes/voltage-regulation/). Pay special attention to the circuit diagram showing the L7805C voltage regulator.
2. Try your best to make a breadboard circuit so that 12 V goes into your circuit and 5 V comes out, as shown on the [website diagram](http://andnowforelectronics.com/notes/voltage-regulation/). You'll need to use your [5V voltage regulator component](http://andnowforelectronics.com/notes/datasheets/#voltage-regulators).
3. Install Kicad.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.


## Project 0: 
**Create a secure motor attachment**

Later this semester, Projects 2 and 4 will require using a motor to actuate some part of an interactive game, and Projects 5 and 6 will involve motor-driven wheels. So in Project 0, you’ll building some knowledge about how to attach a part securely to a motor.

Your task in Project 0 is to design and build a motor hub that meets the following specifications:

-	Fits on and attaches to your DC motor shaft
-	Includes a 3 mm hole located 15 mm from the central axis of your DC motor shaft (you’ll insert a paper clip with a weighted string into this hole) 
-	Stays attached securely enough to handle the amount of torque (load applied to hub) that stalls the motor when it is operating at 12 V
-	Shaped like a spool or lever arm or anything (i.e., shape is up to you)

![](/img/motor-hub-diagram.jpg)

Submit to Canvas both (1) a CAD rendering of your hub design and (2) a photo your actual hub, and bring it to lab on your designated due date. We will compile everyone’s results into histogram showing the range of torques applied before the hubs either (a) slip on their motor shaft or (b) successfully stall the motor.

Due dates are staggered for Project 0 to spread out the demand on fabrication tools at Nolop and Bray. Your hub is due at the start of lab time on the date listed for your weekly lab day.

| Your Weekly Lab Day |  Your Project 0 Due Date | 
|---------------------|-------------------------|
| Sunday         |  Sun., Sep. 17      | 
| Monday         |  Mon., Sep. 25      | 
| Tuesday        |  Tues., Oct. 3      | 
| Wednesday      |  Wed., Oct. 11      | 
| Thursday       |  Thurs., Sep. 21    | 
| Friday         |  Fri., Sep. 29      | 


{{< expand "Click for info on preparing to use the Bray Shop 3D printer, laser cutter, or lathe" "..." >}}
All students must complete the Bray [safety quiz](https://sites.tufts.edu/brayprivate/safety-quiz-complete-to-access-shop-spaces/) prior to their first visit to Bray. Completing the quiz will give you access to the Bray user site where you can submit appointment requests for training and fabrication time. 

Use of the Bray lathe requires lathe-specific training in the red zone, which must be booked by appointment.

Students trained on the 3D printers can access them in Bray Room 109 anytime. 

Students can book an appointment to use the laser cutter or just walk in to use it during shop open hours as long as it is not reserved or in use by someone else.
{{< /expand >}}


{{< expand "Click for info on preparing to use the Nolop 3D printers or laser cutter" "..." >}}
For more information about the Nolop 3D printers, review the training guide [here](https://nolop.org/3dprint/).

Tutorials on using the Nolop laser cutter are available on the Nolop website [here](https://nolop.org/laser/).
{{< /expand >}}

{{< expand "Click to see procedure for motor hub testing" "..." >}}
Work with your entire lab section. Using water bottles and a scale, create a set of 8 different weights ranging from the weight of an empty bottle to the weight of a full bottle. (Yes, each group of 8 will have a different set of 8 weights, but as long as you have a range, your group will be able to do this activity.)

For each motor hub, begin with the lowest weight and attach it to the hub with a paper clip (through the hole placed ~15 mm from the shaft axis) and a length of string. Supply 12 V to the motor and see if it can lift the weight without slipping of the hub. If it succeeds, move on to the next highest weight. Repeat until you get to a weight that either stalls the motor or makes the hub slip around the motor shaft.  Record this as your "slip/stall weight." 

Multiply your hub's "slip/stall weight" by the distance between your shaft axis and your paper clip attachment point (it should be 15 mm, but measure just to be sure).  The results is your "slip/stall torque."

Take a photo of your motor hub attachment. Compare it to the class histogram created in Fall 2022. How are Fall 2023 students doing?
https://docs.google.com/spreadsheets/d/1Y_V_8rgQhnSgg5z3wRCmGc2mLD-aFtRIoKs-uJ67k6A/edit?usp=sharing
{{< /expand >}}

![](/img/motor-hub-examples.png)

