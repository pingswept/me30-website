---
title: "Projects"
draft: false
---
# Projects

## Project #3: Build an electromechanical game

Your task is to build a game with the following characteristics:

*   It is controlled by a Feather microcontroller.
*   It has at least one electromechanical element that moves, like a motor or a solenoid.
*   It has some kind of user input, like buttons, knobs, joysticks, sensors, or the like (no need to spend your own $ - see note below about the ME 30 Nolop tab).
*   It is at least sort of fun to play. A blinking LED is not a game.
*   It is NOT exactly like a game that already exists, like skee-ball or checkers. It can be kinda similar to existing games, but you must use your creativity here.
*   (It does not need to have a custom PCB, but it can if you want. If it has a custom PCB, you must make a working prototype first.)

Where to get materials for your game:

* Feel free to use anything from your ME 30 kit.
* Nolop has buttons, potentiometers, LEDs, and materials for laser cutting. You do not need to pay personally for these items. You can use Nolop   materials for your projects by "charging" it to the ME 30 tab located on a clipboard on the Nolop front table. (That involves writing down the item and your name.)
* Bray also has materials for fabrication.
* If you need something not available at Nolop or Bray, please talk to Brandon or Kristen.

**Midway milestone: Bring a prototype to class and submit some photo or video documentation of it to Canvas: Tuesday, Nov. 1**

**Final demo in class and submit video of it in operation and your code to Canvas: Thursday, Nov. 10**

Class on November 10th will consist entirely of us playing each other's games.

### Project 3 Resources

* Wiring a stepper motor to two H-bridges: https://lastminuteengineers.com/stepper-motor-l298n-arduino-tutorial/
* CircuitPython code for stepper motors: link to py file
* How to download CircuitPython libraries onto your Feather: https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries
* The Adafruit CircuitPython Library Bundle: https://circuitpython.org/libraries

NOTE: I recommend downloading the entire bundle to your **laptop,** and then transferring ONLY the libraries you need for your game to your Feather. Transferring the entire bundle to your Feather will take quite a long time.


## Project #2.5: Create a secure motor attachment

Because the third major project will require using a motor to actuate some part of an interactive game, in Project 2.5, you’ll building some knowledge about how to attach a part securely to a motor.

Your task in Project 2.5 is to design and build a motor hub that meets the following specifications:

-	Provides a 3 mm hole 15 mm from the shaft axis (you’ll insert a paper clip with a weighted string into this hole) 
-	Fits on and attaches to your motor shaft
-	Stays attached securely enough to handle the amount of torque that stalls the motor when it is operating at 12 V
-	Shaped like a spool or lever arm (i.e., shape is up to you)

![](/img/74AC7980-A949-4450-BDC3-5F5F44BE69AC.jpeg)

Submit to Canvas a Solidworks or Onshape rendering of your design, and bring your hub to class. In class on the P2.5 due date, we will compile everyone’s results into histogram showing the range of torques applied before the hubs either (a) slip on their motor shaft or (b) successfully stall the motor.

**Due date: Tuesday, 10/25, at noon (in class)**


## Project #2: Build an H-bridge motor controller

The second project is to build a motor controller with the following characteristics:

*   It consists of a PCB with connectors for a motor, plus power and control lines.
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It has a power LED that lights up when motor power is available.
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting.
*   It can be controlled by logic signals from a Feather (but later, not as part of what you submit for P2).  

Here is a graphical version of those first two bullet points about connectors.

![P2 connectors](/img/P2-connectors.jpg)


<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_708qmkve&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_mtijm1x6" width="400" height="285" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>  

**Due date for prototype: Thursday, October 6, 11:59 PM**

To get started building your prototype H-bridge, review the [Low Power/high power](http://andnowforelectronics.com/notes/low-power-high-power/) and the H-bridge(http://andnowforelectronics.com/notes/h-bridges/) pages, including their mini-lecture videos on BJT and MOSFET transistors. After that, if you're stuck, consult the [H-bridge testing](http://andnowforelectronics.com/notes/demo-videos/#testing-an-h-bridge) demo video.  Note that this video is not intended to give you step-by-step building or testing instructions, but rather to give you a feel for the kind of approach you might take to building and testing this circuit. If your H-bridge prototype isn't working by the deadline for this prototype, don't worry!  Just submit to Canvas a photo of what you have, working or not.  

**Due date for PCB submission: Thursday, October 13, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. (If this cost is a hardship, please let Kristen or Brandon know, and we will help, no questions asked.) After you submit it, take a screenshot of your order confirmation and upload it to the Project 2 PCB assignment on Canvas (proof that you submitted your project on time). Also, take a screenshot of your PCB design in KiCad and upload that as well (it would be a good idea to save this screenshot for your portfolio). 

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

If you feel like you understand this project pretty well, or if you've made a basic circuitboard before, you could try adding additional features. Look at the open source [Ant breadboard power supply](https://www.crowdsupply.com/digital-cool/ant-bbps) for inspiration. The [schematics are available](https://gitlab.com/DigitalUncool/ant/-/blob/main/Hardware) if you're curious about the details.

### P1 prototype: what you should do before class #3 (before Tues., 9/13)

1. Read and try to make sense of the website notes on [voltage regulation](http://andnowforelectronics.com/notes/voltage-regulation/). Pay special attention to the circuit diagram showing the L7805C voltage regulator.
2. Try your best to make a breadboard circuit so that 12 V goes into your circuit and 5 V comes out, as shown on the [website diagram](http://andnowforelectronics.com/notes/voltage-regulation/). You'll need to use your [5V voltage regulator component](http://andnowforelectronics.com/notes/datasheets/#voltage-regulators).
3. Install Kicad.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.

## Project #0: Power an LED with "wall" power through our DC power supply. Control it with a push button.

The getting-started "project" is really more of a warm-up activity, and we'll do it together in class. The goal is to create a circuit on your breadboard that powers an LED with power from the wall, directed through your kit's DC power supply.  This circuit should have the following characteristics:

*   It is implemented on a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It turns on an LED when a push button is pressed.

**Due date (for submitting a photo of your circuit to Canvas): Thursday, September 8, 11:59 PM**

