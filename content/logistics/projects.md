---
title: "Projects"
draft: false
---

# Projects 5 and 6: Build an intrepid robot

Projects 5 and 6 are, in a sense, one mega-project. In the first part, P5, you and your team build a robot. In the second part, P6, you and your team modify the robot to deliver a payload under specific diabolical constraints.

## Requirements for project 6
### Modify your intrepid robots to roll a tube up a ramp in pairs

**Due during your final exam block, SEC Atrium**

Final demo sessions are on Tuesday, 12/17 (3:30pm) or Wednesday, 12/18 (2:00 or 3:30pm). These are the university-scheduled times scheduled for ME 30 finals.

All teams, from all ME 30 sections, are welcome at any of these demo sessions. However, if you finish P6 earlier and you can find another team to demo with you, you can come to Nolop for an early demo on Friday, 12/13, 3pm or Monday, 12/16, 3pm.

### The challenge ###

Your final challenge is to modify your robot's hardware and software so that it can collaborate with another robot to roll a tube (plastic, diameter of 3 in) up the pair of ramps as quickly as possible without the tube falling off either ramp. It is the shared responsibility of both robots to control their speed and the tube angle to shepherd the tube to the top of the ramp.

You will know the IP address of the robot you are collaborating with, but your robot should attempt to work with any one of the 40 other robots in the class. On the day of the trials, you can try to work with multiple different robots. The most successful robot is the robot that can work with the largest variety of peers.

* Your robot should still comply with all the constraints from P5.
* Your robot should receive only one signal from a human: the click of a button to begin operation. After starting, your robot should operate autonomously.
* Your robot should respond to two URLs: `/start/<delay>` and `/target/<speed>`. (See [URL details](/logistics/projects/#url-details) below.)
* Your robot should only make requests where `delay` is an integer in the range 1-10 seconds, and `speed` is an integer in the range 1-1000 mm/second.
* Your robot should never send HTTP requests at a rate of more than 10 Hz, i.e. wait at least 100 ms between requests.

### URL details ###

For `/start/<delay>`, your robot should respond `ok` or `no`. After responding `ok`, it should start driving in `delay` seconds. If your robot is not ready, or it has already agreed to a start time, or it is driving, it should respond `no`.

For `/target/<speed>`, your robot should respond `ok` or `no`. After responding `ok`, it should try to ascend the ramp at a rate of `speed` mm/s.

As your robot ascends the ramp, if your robot detects that the tube is tilting or sliding off, your robot can suggest that its partner speed up or slow down by requesting new target speeds. Your robot should listen for new target speeds from its partner and should respond in a way to increase the chances of getting the tube up the ramp quickly. Note that the robot is required to operate autonomously after the start; you cannot have a human in the feedback loop, mashing buttons in desperation.


![P6 ramps diagram](/img/ramps-with-tube.png)

### Recommended work plan ###

Project 6 is challenging. We suggest that you **break it down into the following sequence of more manageable tasks.** Each task involves adding a new capability to your robot until it can achieve all of the project requirements.

1. Get your robot to drive up a ramp autonomously. Make sure it can handle the weight of the tube while driving. For this task, be sure to consider mechanical solutions. You might add guards or guides to your robot that keep it from veering off the edges of the ramp; you might swap out a swervy caster wheel for a wheel-and-axle assembly that tracks straighter; or something else like that. 
2. Make decisions about driving speed. Figure out how commands (voltage or PWM) to your robot's motors translate into its linear speed up the ramp (in mm/sec). Also, what is the min/max driving speed for your robot? What kind of start delay works for your robot?
3. Get your robot to run Flask and start at a target `speed` (in mm/sec) after a specific `delay` (in seconds) based on receiving those values in HTTP requests (i.e., focus on running a server.py script in Flask with @app.route to functions).
4. Get your robot to send `delay` and `speed` requests to a partner (i.e., add code that now also can send HTTP requests). Info on how to send an HTTP request from within a Python script is [here](http://andnowforelectronics.com/notes/pi-programming/#how-do-i-send-a-get-http-request-from-within-a-python-script).
5. Decide how to run both of these simultaneously (see [Software Architecture](/logistics/projects/#software-architecture) details below.)
6. Get your robot to be able to check if the tube is stable (i.e., not sliding off at an angle), perhaps with buttons or other sensors. Understand how the speeds of your robot and your partner's robot should change based on information about the tube. (e.g., If you sense the tube tilting toward your partner, do you send a target speed request to your partner to speed up or slow down? Do you change your own speed? What if you're alread driving at min or max speed?)
7. Get your robot to be able to receive target `speed` and `delay` requests while driving.

The key to this method is to focus on one new "robot superpower" at a time. Don't try to add them all at once because each capability influences the others. 

### Minimum viable product ###

If you're overwhelmed by the details, start by aiming to:
* Get your robot to drive up a ramp autonomously.
* Have your robot be able to sense the tube and adjust its speed as needed to get the tube up the ramp.
      

### Software architecture ###

Assuming your intrepid robot can drive up the ramp with enough force left to roll the tube, you should figure out how to set up your Pi so that it can collaborate effectively with the robot on the other ramp. The major challenge is that a Python program can only do one thing at a time, so if your Flask server is listening to or responding to a request from another robot, it can't do anything else. The exciting thing is that we have an operating system running on the Pi that allows you to run multiple processes simultaneously.

Before we get into that slightly complicated arrangement, there is a simpler approach that might work, and it will probably be useful for testing.

### The simpler approach ###

Add two routes to Flask that look something like this.

```python
import requests # a Python library that lets us make HTTP requests of another host
import time

@app.route('/do-once')
def do_once():
    # (This is pseudo code)
    speed = negotiate_target_speed_with_partner()   # pseduo code;  you would need to fill in the details here
    delay = negotiate_start_delay_with_partner()     # pseduo code;  you would need to fill in the details here
    time.sleep(delay)
    set_motors_to_target(speed)    # pseudo code; fill in the details here

@app.route('/control-loop')
def control_loop():
    # (This is pseudo code)
    read_sensors()        # pseudo code; fill in the details here
    change_PWM_based_on_sensor_data()   # pseudo code; fill in the details here
    maybe_suggest_different_target_speed_to_partner()   # pseudo code; fill in the details here
```

If you have those two routes, you could make a webpage served from your Flask templates folder that has 2 buttons: `run_do_once` and `run_control_loop`. Then, to start, you click the `run_do_once` button, which runs the `do_once` function on your Pi. If it works, your robot starts driving.

Then, you mash the `run_control_loop` button repeatedly as fast as you can. This runs the `control_loop` function on your Pi a few times a second.

"BUT WAIT!" you cry in dismay, "That violates the 'only one signal from a human' requirement!" Yes, it does. The next thing to do is to modify your webpage so that it mashes the button for you repeatedly. You can ask ChatGPT about this, and it will explain about the `setInterval` method in Javascript.

### A more advanced approach

The simpler approach described above has the strength that it is uses the same tools we used for robot control in P5 (a single Python process running Flask, a web page sending commands to the Flask server). It has the weakness that it relies on a wifi connection for everything. If the wifi gets laggy, which is likely, your control loop won't execute reliably.

The good news is that instead of triggering the `control_loop` function repeatedly through the internet, you can run it locally on your Pi, as long as you run it in a separate Python process. There are a few different ways you could do this. Here are a few.

1. It's a bit hacky, but you could log in to your Pi twice in two different SSH sessions. Start Flask in one window and run something like `python3 control-loop.py` in the other. The big challenge here is figuring out how to share information, like the target speed, between the control loop and Flask server. A decent solution would be to have the server write the target speed to a file and then have the control loop read it. ChatGPT can tell you how to read and write from a file in Python. Alternatively, you could also implement a route like `@app.route('/get-target-speed')` which just retrieves the target speed from a global variable held by the Flask server.

2. If you want something less brittle than 2 SSH sessions, you could [run the Flask server using Supervisor](/notes/pi-programming/#thats-cool-but-how-do-i-get-flask-to-start-itself-when-the-pi-boots). For a fully autonomous robot, you could also run your control loop using Supervisor.

3. Debugging errors while starting and stopping Supervisor can be cumbersome, so while you're testing, you could also run your control loop on your laptop, as long as you communicate with the Flask process entirely via HTTP rather than files.

4. There are lots of other ways to talk between Python processes, like the [Python multiprocessing module](https://docs.python.org/3/library/multiprocessing.html), [RPyC](https://rpyc.readthedocs.io/en/latest/), or [ZeroMQ](https://zeromq.org/languages/python/).

### Project 6 FAQs

{{< expand "0. Where do we start?" "..." >}}
See notes above on [Recommended work plan](/logistics/projects/#recommended-work-plan).
{{< /expand >}}

{{< expand "1. How big is the tube?" "..." >}}
3 inches in diameter, around 52 inches long
{{< /expand >}}

{{< expand "2. Will we know our partner robot ahead of time?" "..." >}}
No. On the day of the showcase we'll make random pairings and ask you to try rolling the tube up the ramp together. If it doesn't go well, you can try again with other partners. However, the most successful robot is the one that can collaborate with the most other robots.
{{< /expand >}}

{{< expand "3. Can we make physical modifications to our partner robot?" "..." >}}
No. 
{{< /expand >}}

{{< expand "4. Is there a way to get our Pi to run two Python scripts at the same time?" "..." >}}
Yes. One way to do this is to log in to your Pi twice in two different SSH sessions. You can type different commands into the two the different sessions.

See [A more advanced approach](/logistics/projects/#a-more-advanced-approach) above for other ideas.
{{< /expand >}}

{{< expand "5. How do you send an HTTP request (like for a target speed) from within a Python script?" "..." >}}
Let's say you want to use an HTTP request to send a target speed value to another Pi, at IP address 10.123.12.12.  For this example, let's say the target speed value is 50.
```python
import requests

desired_speed = 50
partner_url = "http://10.123.12.12:5000/"

r = requests.get(partner_url + "/target/" + str(desired_speed))  #this sends out "http://10.123.12.12:5000/target/50"

# another way to make that same request is r = requests.get(10.123.12.12:5000/target/50)

print(r.text)   # prints whatever response you get from the server (the Pi at 10.123.12.12)
                # the variable 'r' stores all the information related to the HTTP request that you made
                # r.text is the content of the response from the server
```
Then you could do something like `if r.text == 'ok'` or `if r.text != 'ok'` to compare the server's response to the string 'ok.'

See more info on the Python requests library [here](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request).
{{< /expand >}}

{{< expand "6. What happens if two Pis make requests of each other at the same time?" "..." >}}
In reality, one of those requests will be received a tiny fraction of a second before the other one. You should think about what you want your robot to do if it receives a request from a partner robot just after it has sent out its own request. Is there a way to make your robot respond differently if it "knows" it is still waiting for a response itself? 
{{< /expand >}}

{{< expand "7. Do we need advanced sensors for this project?" "..." >}}
No, you don't. You probably need at least some buttons or switches cleverly located, but you can be successful without cameras, distance sensors, or the like.
{{< /expand >}}

{{< expand "8. When can we get help?" "..." >}}
Regular labs have ended, but there will be office hours in Nolop:

* Mon., 12/9, 6-9pm (LAs)
* Mon., 12/9, 4-5pm (Kristen)
* Tue., 12/10, 6-9pm (LAs)
* Wed., 12/11, 11am-1pm (Kristen)
* Fri., 12/13, 2:30-4:30pm (Kristen)

<!--* Mon., 12/11 - Gabe 1:30-2:30pm, Zosia 5-7pm, Theresa 7-8pm
* Tue., 12/12 - Anna 12:30-2:30pm, Theresa 3:30-4:30pm, Zosia 5-7pm
* Wed., 12/13 - Zosia 1-2:30pm
* Thu., 12/14 - Alexa 10:30-11:30am, Anna 2:30-4:30pm, Antonio 5-7pm
* Fri. 12/15 - Rose 12-2pm, Kristen 2-5pm-->

{{< /expand >}}

## Requirements for project 5
### Build an intrepid robot that travels up a ramp

**Due date: Wednesday, December 4, 9:00/10:30/3:00**

This is a relatively constrained project compared to the vast open field of P4. Your task is to build a robot that can travel up a ramp, controlled remotely by you.

* Your robot should fit in a circle 18 inches in diameter.
* Your robot should be less than 12 inches tall.
* Your robot should be able to ascend the ramp without falling off the side.
* You should not touch your robot during its adventures. This probably means that your robot should be remote controlled.
* You should not use an RC car controller. This probably means that your robot should be controlled through wifi from a laptop or phone.
* Your robot cannot fly. (We don't have the space to test drones safely, unfortunately.)
* Unlike previous years, your robot does NOT need to turn in arbitrary directions. It should be optimized for straight ramp ascension.
* Note: It would be a good idea to focus on making your robot drive effectively before you worry about any higher level mechanics or control through the internet.

In class on the due date, we will test drive the robots through a basic course-- a 18 inch wide, 12 inch tall doorway and a ramp. If your robot meets the requirements above, it will do fine. The rough specifications of the ramp are shown in the picture below. The ramp is available in Nolop for testing.

![P5 ramp diagram](/img/ramp.png)

**Project planning resource:** We suggest discussing this [list of P5 planning questions](https://tufts.box.com/s/hs2supj34cp4mar33w4fsitflc4m4o6c) with your team. 

### **Batteries for projects 5 and 6**

For portable power, Nolop has 5 V batteries (for the Raspberry Pis) and 9 V and 11 V batteries (for motors).

![battery safety](/img/11volt_battery_safety.jpg)

### **H-bridges for projects 5 and 6**

The goal is for you to use your Project 3 H-bridge PCBs for your robot motor control. However, as a last resort, if no one on your team can get their P3 PCBs to work, you can find a dual-H-bridge PCB (called an L298 motor driver) in the Nolop store.

Please see the sketch below for details on how to wire the L298 dual H-bridge board.

![L298 wiring](/img/L298_Wiring.jpg)


### **More details for projects 5 and 6**

* See the [Raspberry Pi setup](http://andnowforelectronics.com/notes/pi-setup/) page to learn how to control your Pi via serial cable and the Internet.
* See the [Raspberry Pi programming](http://andnowforelectronics.com/notes/pi-programming/) page for snippets of Python code to control the pins on your Pi. 
* See the [servers and clients](http://andnowforelectronics.com/notes/servers/) page to learn how to coax your Pi into sending and receiving data through the Internet.
* See the [client and server setup](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup) demo video that walks through the code for Raspberry Pis as clients and servers (it also shows Arduino code from previous semesters, but you should ignore that)
* See the [Internet](http://andnowforelectronics.com/notes/internet/) page to find out how IP addresses work.

### Team options for projects 5 and 6

Option 1 – Work in a team of 2 or 3 chosen by you

Option 2 – Work in a team of 2 or 3 assigned to you by Kristen and Brandon
We’ll pool all the people who would like to be assigned a partner and team you up. We might need to make a team of 3 depending on who is available. 

Use [this survey](https://tufts.qualtrics.com/jfe/form/SV_0cAixyzuN8ok4br) to indicate your chosen teaming option (list your teammates or indicate you'd like to be placed on a team).

## Project 4: Build an electromechanical game

Your task is to build a game with the following characteristics:

*   It is controlled by a KB2040 microcontroller.
*   It uses your H-bridge prototype to drive a motor in at least one direction. (If you need a second H-bridge, you can make another one or use any motor driver that will work.) 
*   It has some kind of user input, like a button, knob, joystick, sensor, or the like, that talks to the KB2040 microcontroller. (Read the note below about the ME 30 Nolop tab).
*   It has at least one part that moves, driven by one of the motors in your kit. (You can use both motors if you want. Servo motors are prohibited.)
*   It is at least sort of fun to play. A blinking LED is not a game.
*   It includes no 3D printed components whose STL files were downloaded from the internet.
*   Its major structural components are NOT 3D printed.

For 1 of the 7 project points you will also need to respond to the project reflection questions linked from Canvas.

### Personal learning goals ###

As soon as you can manage it, you should formulate and submit to Canvas one or more personal learning goals for the project. Building games is cool, but the real point here is for you to gain skills and experience that help you grow as an engineer. That works best when your heart is in it; this is your chance to follow where your heart leads. (Okay, that's a bit cheesy, but also true.)

**By Tuesday, October 29, 11:59 PM, please describe your learning goal on Canvas.**

At the end of the project, one of the reflection questions will ask you whether you met your learning goal.

### Where to get materials for your game ###

To build the game, you can use anything from your ME 30 kit, as well as anything else you can lay your hands on. Additionally, Nolop has buttons, potentiometers, LEDs, and other electronic components, as well as materials for laser cutting. You can use Nolop materials for your projects by recording them on the ME 30 tab located on a clipboard on top of the Nolop store. (At the end of the semester, the ME department pays Nolop back for all the parts we use.)

Bray also has materials for fabrication, leaning more toward the metal/nuts/bolts end of the spectrum.

If you need something not available at Nolop or Bray, please talk to Brandon or Kristen as soon as you can.

**Due date for game: Monday, November 18, IN CLASS**

Documentation due on Canvas by Monday, November 18, 11:59 PM

On November 18th, class will consist of us playing each other's games, marveling at our collective ingenuity and resourcefulness, and introducing Project 5. 

## Project 3: H-bridge
**Build an H-bridge motor controller**

The third project is to build a motor controller to meet the following requirements:

*   It consists of a PCB with connectors for a motor, plus power and control lines.
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It has a power LED that lights up when motor power is available.
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting (see notes on PCB [ampacity](http://andnowforelectronics.com/notes/ampacity/))
*   It can be controlled by logic signals from a KB2040.  

Here is a graphical version of those first two bullet points about connectors.

![P2 connectors](/img/P3-connectors.jpg)


<!-- <iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_708qmkve&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_mtijm1x6" width="400" height="285" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>  -->

**Due date for prototype: Monday, October 21, 11:59 PM**

To get started building your prototype H-bridge, review the [Low Power/high power](http://andnowforelectronics.com/notes/low-power-high-power/) and the H-bridge(http://andnowforelectronics.com/notes/h-bridges/) pages, including their mini-lecture videos on BJT and MOSFET transistors. After that, if you're stuck, consult the [H-bridge testing](http://andnowforelectronics.com/notes/demo-videos/#testing-an-h-bridge) demo video.  Note that this video is not intended to give you step-by-step building or testing instructions, but rather to give you a feel for the kind of approach you might take to building and testing this circuit. If your H-bridge prototype isn't working by the deadline for this prototype, don't worry!  Just submit to Canvas a photo of what you have, working or not.  

**Due date for functional breadboard H-bridge and PCB submission: Monday, October 28, 11:59 PM**

When your PCB design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. (If this cost is a hardship, please let Kristen or Brandon know, and we will cover the cost by ordering it for you, no questions asked.) After you submit it, take a screenshot of your order confirmation and upload it to the Project 3 PCB assignment on Canvas (proof that you submitted your project on time). Also, take a screenshot of your PCB design in KiCad and upload that as well (it would be a good idea to save this screenshot for your portfolio). 

For this final submission to Canvas, you will also need to submit evidence that your H-bridge circuit is functional. So, once you do get your breadboard H-bridge working, take a video that shows it making the motor spin in both directions, controlled by a KB2040. You'll need that video for your P3 final Canvas submission.




## Project 2: Simple game
**Build a simple game**

The next project is to use the basic electrical components we've covered in class with some mechanical fabrication to make a game that is at least mildly entertaining. The point here is NOT making the best game ever, but to set some goals for testing out your electromechanical skills. For your circuit for this project, use your breadboard. No PCBs needed.

This is a solo project, but we'll be brainstorming in groups.

You should bring your game to class on Wednesday, October 9th to share with your brainstorming group.

Due date (for game documentation submission): Wednesday, October 9th, 11:59PM

To keep things simple, there are a few required constraints.
Your game should:
* Use the DC gearmotor in your kit
* Use at least one transistor 
* Require user interaction of some sort (e.g., pushing a button, pressing a key, interacting with a physical component)
* Fit inside a cube 20 cm on a side
* Be fabricated without 3D printing, except for a motor hub if needed (talk to an instructor if you have a particular reason you need to violate this constraint.)

The point of the constraints is to keep your game simple enough that you can complete it in 1.5 weeks.

In addition to planning to meet these constraints, you should also pick one learning goal for yourself for this project. Open-ended projects offer you an opportunity to bend the curriculum into the direction of your interests or to explore a potential new area of interest.

Here are some example learning goals:
* Get more comfortable with cordless drills and at least one other hand tool.
* Test my system to failure, then rebuild it stronger.
* Use only recycled/found materials.
* Complete my project 24 hours early.
* Model, predict and subsequently measure at least one mechanical property of my project.
* Use the laser cutter (which I have never used before).
* Make at least one part out of steel.
* Turn a part on a lathe at Bray.
* Spend at least 1/3 of my effort on the aesthetics of the project.

## Project 1: Power supply
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


## Project 0: Motor hub
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
