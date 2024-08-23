---
title: "Projects Archive"
draft: true
---
# Projects Assigned in Fall 2023

# Projects 5 and 6: Build an intrepid robot

Projects 5 and 6 are, in a sense, one mega-project. In the first part, P5, you and your team build a robot. In the second part, P6, you and your team modify the robot to deliver a payload under specific diabolical constraints.

## Requirements for project 6
### Modify your intrepid robots to roll a tube up a ramp in pairs

**Due Monday, December 18, 3:30 PM, SEC Atrium**

Your final challenge is to modify your robot's hardware and software so that it can collaborate with another robot to roll a tube (cardboard, diameter of 3 in) up the pair of ramps as quickly as possible without the tube falling off either ramp. It is the shared responsibility of both robots to control their speed and the tube angle to shepherd the tube to the top of the ramp.

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

**BONUS: To make sure that friction is not an insurmountable obstacle, the driving surface of the ramps will be covered in grip tape.**

If it's useful, we have several bins of ball bearings in Nolop that you could use to make some kind of tube roller for the front of your robot. Ball bearings may turn out to be unnecessary, but they're available if you need them.

![P6 ramps diagram](/img/ramps-with-tube.png)

### Recommended work plan ###

Project 6 is challenging. We suggest that you **break it down into the following sequence of more manageable tasks.** Each task involves adding a new capability to your robot until it can achieve all of the project requirements.

1. Get your robot to drive up a ramp autonomously. Make sure it can handle the weight of the tube while driving. For this task, be sure to consider mechanical solutions. You might add guards or guides to your robot that keep it from veering off the edges of the ramp; you might swap out a swervy caster wheel for a wheel-and-axle assembly that tracks straighter; or something else like that. 
2. Make decisions about driving speed. Figure out how commands (voltage or PWM) to your robot's motors translate into its linear speed up the ramp (in mm/sec). Also, what is the min/max driving speed for your robot? What kind of start delay works for your robot?
3. Get your robot to run Flask and start at a target `speed` (in mm/sec) after a specific `delay` (in seconds) based on receiving those values in HTTP requests (i.e., focus on running a server.py script in Flask with @app.route to functions).
4. Get your robot to send `delay` and `speed` requests to a partner (i.e., add code that now also can send HTTP requests).
5. Decide how to run both of these simultaneously (see [Software Architecture](/logistics/projects/#software-architecture) details below.)
6. Get your robot to be able to check if the tube is stable (i.e., not sliding off at an angle), perhaps with buttons or other sensors. Understand how the speeds of your robot and your partner's robot should change based on information about the tube. (e.g., If you sense the tube tilting toward your partner, do you send a target speed request to your partner to speed up or slow down? Do you change your own speed? What if you're alread driving at min or max speed?)
7. Get your robot to be able to receive target `speed` and `delay` requests while driving.

The key to this method is to focus on one new "robot superpower" at a time. Don't try to add them all at once because each capability influences the others. 

### Minimum viable product ###

If you're overwhelmed by the details, start by aiming to:
* Get your robot to drive up a ramp autonomously.
* Decide the best speed for your robot.
* Tell your partner what speed and start delay you need.
* On the count of three, start your robot.            

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
    speed = negotiate_target_speed_with_partner()
    delay = negotiate_start_delay_with_partner()
    time.sleep(delay)
    set_motors_to_target(speed)

@app.route('/control-loop')
def control_loop():
    # (This is pseudo code)
    read_sensors()
    change_PWM_based_on_sensor_data()
    maybe_suggest_different_target_speed_to_partner()
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
3 inches in diameter, 52 inches long
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

{{< expand "5. What happens if two Pis make requests of each other at the same time?" "..." >}}
In reality, one of those requests will be received a tiny fraction of a second before the other one. You should think about what you want your robot to do if it receives a request from a partner robot just after it has sent out its own request. Is there a way to make your robot respond differently if it "knows" it is still waiting for a response itself? 
{{< /expand >}}

{{< expand "6. Do we need advanced sensors for this project?" "..." >}}
No, you don't. You probably need at least some buttons or switches cleverly located, but you can be successful without cameras, distance sensors, or the like.
{{< /expand >}}

{{< expand "7. When can we get help?" "..." >}}
Regular lab times have ended, but there are extra office hours in Nolop the week of Dec. 12:

* Mon., 12/11 - Gabe 1:30-2:30pm, Zosia 5-7pm, Theresa 7-8pm
* Tue., 12/12 - Anna 12:30-2:30pm, Theresa 3:30-4:30pm, Zosia 5-7pm
* Wed., 12/13 - Zosia 1-2:30pm
* Thu., 12/14 - Alexa 10:30-11:30am, Anna 2:30-4:30pm, Antonio 5-7pm
* Fri. 12/15 - Rose 12-2pm, Kristen 2-5pm

As always, please reach out to an instructor if you want to make a separate appointment for help.
{{< /expand >}}

## Requirements for project 5
### Build an intrepid robot that travels up a ramp

**Due date: Wednesday, December 6, 10:30 AM**

This is a relatively constrained project compared to the vast open field of P4. Your task is to build a robot that can travel up a ramp, controlled remotely by you.

* Your robot should fit in a circle 45 cm in diameter.
* Your robot should be less than 30 cm tall.
* Your robot should be able to ascend the ramp without falling off the side.
* You should not touch your robot during its adventures. This probably means that your robot should be remote controlled.
* You should not use an RC car controller. This probably means that your robot should be controlled through wifi from a laptop or phone.
* Your robot cannot fly. (We don't have the space to test drones safely, unfortunately.)
* Unlike previous years, your robot does NOT need to turn in arbitrary directions. It should be optimized for straight ramp ascension.
* Note: It would be a good idea to focus on making your robot drive effectively before you worry about any higher level mechanics or control through the internet.

In class on December 6, we will test drive the robots through a basic course-- a 45 cm wide, 30 cm tall doorway and a ramp. If your robot meets the requirements above, it will do fine. The rough specifications of the ramp are shown in the picture below. Two identical ramps will be available in Nolop for testing by December 1.

![P5 ramp diagram](/img/ramp.png)

**Project planning resource:** We suggest discussing this [list of P5 planning questions](https://docs.google.com/document/d/1ulQfKKEcXGVL5VZVITyimeE2d2Y40JnkMOGGLtVdCfo/edit?usp=sharing) with your team. 

### Team options for projects 5 and 6

**Option 1 – Work in a team of 2 or 3 chosen by you**

**Option 2 – Work in a team of 2 or 3 assigned to you by Kristen and Brandon**
We’ll pool all the people who would like to be assigned a partner and team you up. We might need to make a team of 3 depending on who is available. 

By Sunday, Nov. 26, use [this survey](https://tufts.qualtrics.com/jfe/form/SV_0cAixyzuN8ok4br) to indicate your chosen teaming option (list your teammates or indicate you'd like to be placed on a team).

### More details for projects 5 and 6

* For portable power, Nolop has 5 V batteries (for the Raspberry Pis) and 9 V and 11 V batteries (for motors).
* See the [Raspberry Pi setup](http://andnowforelectronics.com/notes/pi-setup/) page to learn how to control your Pi via serial cable and the Internet.  
* See the [servers and clients](http://andnowforelectronics.com/notes/servers/) page to learn how to coax your Pi into sending and receiving data through the Internet.
* See the [client and server setup](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup) demo video that walks through the code for Raspberry Pis and Arduinos as clients and servers
* See the [Internet](http://andnowforelectronics.com/notes/internet/) page to find out how IP addresses work.

## Project 4: Build an electromechanical game

Your task is to build a game with the following characteristics:

*   It is controlled by a KB2040 microcontroller.
*   It has some kind of user input, like a button, knob, joystick, sensor, or the like, that talks to the microcontroller. (Read the note below about the ME 30 Nolop tab).
*   It has at least one part that moves, driven by one of the motors in your kit. (You can use both motors if you want. Servo motors are prohibited.)
*   It is at least sort of fun to play. A blinking LED is not a game.
*   (It does not need to have a custom PCB, but it can if you want. If you aim to make a custom PCB, you must make a working prototype first.)

### Personal learning goals ###

As soon as you can manage it, you should formulate and write down one or more personal learning goals for the project. Building games is cool, but the real point here is for you to gain skills and experience that help you grow as an engineer. That works best when your heart is in it; this is your chance to follow where your heart leads. (Okay, that's a bit cheesy, but also true.)

**By Wednesday, November 1, 11:59 PM, please complete the learning goal assignment on Canvas.**

At the end of the project, when you submit your documentation, we'll ask you whether you met your learning goal.

### Where to get materials for your game ###

To build the game, you can use anything from your ME 30 kit, as well as anything else you can lay your hands on. Additionally, Nolop has buttons, potentiometers, LEDs, and other electronic components, as well as materials for laser cutting. You can use Nolop materials for your projects by recording them on the ME 30 tab located on a clipboard on top of the Nolop store. (At the end of the semester, the ME department pays Nolop back for all the parts we use.)

Bray also has materials for fabrication, leaning more toward the metal/nuts/bolts end of the spectrum.

If you need something not available at Nolop or Bray, please talk to Brandon or Kristen as soon as you can.

**Due date for game: Wednesday, November 15, 10:30 AM (IN CLASS)**

Documentation due on Canvas by Wednesday, November 15, 11:59 PM

On November 15th, class for both sections of ME 30 will take place in the SEC atrium. The class will consist entirely of us playing each other's games, and marveling at our collective ingenuity and resourcefulness. (Set-up 10:30 to 11:00; sharing starts at 11:00.)

## Project 3: Build an H-bridge motor controller

The third project is to build a motor controller with the following characteristics:

*   It consists of a PCB with connectors for a motor, plus power and control lines.
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It has a power LED that lights up when motor power is available.
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting (see notes on PCB [ampacity](http://andnowforelectronics.com/notes/ampacity/))
*   It can be controlled by logic signals from a KB2040.  

Here is a graphical version of those first two bullet points about connectors.

![P2 connectors](/img/P3-connectors.jpg)


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

    





# Projects Assigned in Fall 2022

# Projects 4 and 5
### Build an intrepid robot that traverses an obstacle course and delivers freight

Projects 4 and 5 are, in a sense, one mega-project. In the first part, P4, you and your team build a robot. In the second part, P5, you and your team modify it to traverse an obstacle course and deliver a payload.

### Requirements for project 5
### Build something that traverses or climbs over the maze by Thursday, December 15, high noon

Your robot, which you have constructed for P4, must complete two tasks:

 1. It must EITHER travel through the maze (shown below) or scale the ramp, cross the roof of the maze, and drive down the ramp on the far side.
 2. After completing the first challenge, your robot must visit the freight terminal, where it will be given a payload. Your robot will then deliver the payload to the drop zone. Once one of your team members has received the payload in the drop zone, your team has completed the challenge.

### Characteristics of the maze

If your robot traversed the hallway and doorway of P4, it will fit through the maze. However, the maze has a roof on it, and you can't see inside. 
To spice things up a little, the maze has two movable walls. One of the walls will be at location A or B. The other wall will be at location C or D. You will not know which location the movable walls are in. This means you will need to add some kind of sensor system to your robot. You might consider using ultrasonic distance sensors, optical sensors, pushbuttons bumpers, or a webcam to navigate the maze.

If sensors are not that interesting to you, you can instead choose to drive over the maze. This will likely require that you upgrade your robot to be able to drive up and down ramps, which is a non-trivial challenge.

### Characteristics of the freight terminal and drop zone

Okay, to be honest, we were considering having a freight terminal where you have to pick up a payload with a forklift (or something like that), but it seemed too difficult. So, all you have to do is have your robot drive up to a table to receive freight. When your robot arrives, one of the LA's will put a payload (a mass weighing less than 1 kg and less than 10 cm in diameter) on your robot. If your robot can drive to the nearby drop zone (an area marked by tape on the floor), you're victorious!

![](/img/maze-top-view.jpg)

![](/img/maze-isometric-view.jpg)

The length of the ramp surface is 122 cm, and its height is 41 cm. 

### Requirements for project 4
### Build something that travels by Tuesday, December 6, high noon

This is a relatively constrained project compared to the vast open field of P3. Your task is to build a robot that can travel across the floor, controlled remotely by you.

* Your robot should fit in a circle 30 cm in diameter.
* Your robot should be less than 30 cm tall.
* The top of your robot should be a freight platform that can support a load, up to 10 cm in diameter that weighs up to 1 kg.
* Your robot should be stable, so that as it travels, laden with freight, it does not tilt its load more than 3 degrees in any direction from the horizontal plane. 
* You should not touch your robot during its adventures. This probably means that your robot should be remote controlled.
* You should not use an RC car controller. This probably means that your robot should be controlled through wifi from a laptop or phone.
* Your robot cannot fly. (We don't have the space to test drones safely, unfortunately.)
* You should submit video documentation to Canvas and bring your something-that-drives to class.
* Note: It would be a good idea to focus on making your robot drive effectively before you worry about any higher level mechanics or control through the internet.

**Due date: Tuesday, December 6, high noon**

In class on December 6, we will test drive the robots through a basic course-- basically a U-shaped hallway with a 30 cm doorway. If your robot can navigate and meets the requirements above, it will do fine. 

**Project grading:** As with all projects in ME 30, if your robot demonstrates an attempt at meeting all requirements, you receive full points for the project.

**Project planning resource:** We suggest discussing this [list of P4 planning questions](https://docs.google.com/document/d/1ulQfKKEcXGVL5VZVITyimeE2d2Y40JnkMOGGLtVdCfo/edit?usp=sharing) with your team. 

### Team options for projects 4 and 5

**Option 1 – Work in a team of 2 or 3 chosen by you**
If there are 1 or 2 other people in the class you would like to work with, send Kristen and Brandon an email listing the names of the people on your team.

**Option 2 – Work in a team of 2 or 3 assigned to you by Kristen and Brandon**
We’ll pool all the people who would like to be assigned a partner and try to team you up. We might need to make a team of 4 depending on who is available. If you'd prefer this option, no need to do anything; we'll team up everyone not already on a team.

### More details for projects 4 and 5

* If you need parts (like a sensor or a certain kind of motor), we're happy to order them for you.  
* See the [Raspberry Pi setup](http://andnowforelectronics.com/notes/pi-setup/) page to learn how to control your Pi via serial cable and the Internet.  
* See the [servers and clients](http://andnowforelectronics.com/notes/servers/) page to learn how to coax your Pi into sending and receiving data through the Internet.
* See the [client and server setup](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup) demo video that walks through the code for Raspberry Pis and Arduinos as clients and servers
* See the [Internet](http://andnowforelectronics.com/notes/internet/) page to find out how IP addresses work.

# Project #3: Build an electromechanical game

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

## Project 3 FAQs / Resources

- State machine code shown in class: https://gist.github.com/pingswept/1d37a74943f73a6266688db44f3e382d
- Downloading CircuitPython libraries onto your Feather: https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries
- Full bundle of CircuitPython libraries for the Feather: https://circuitpython.org/libraries

NOTE: I recommend downloading the entire bundle to your **laptop,** and then transferring ONLY the libraries you need for your game to your Feather. Transferring the entire bundle to your Feather will take quite a long time.

- Stepper motors - how to wire: https://lastminuteengineers.com/stepper-motor-l298n-arduino-tutorial/
- Stepper motors - how to code:

{{< expand "Click to see stepper motor code" "..." >}}
<pre class="code">
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Use this example for digital pin control of an H-bridge driver
# like a DRV8833, TB6612 or L298N.

import time
import board
import digitalio
from adafruit_motor import stepper

# Set DELAY as the length of time that the motor runs for each step. Adafruit suggests 0.01, but ME 30 folks have found this delay value needs to be much shorter. If 0.01 doesn't work, try something as short as 0.005.

DELAY = 0.01

# Set the number of steps for one rotation of the motor. For the stepper motor in the ME 30 kit, one rotation takes 200 steps.

STEPS = 200

# You can use any available GPIO pin on a microcontroller.
# The following pins are simply a suggestion. If you use different pins, 
# update the following code to use your chosen pins.

coils = (
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
    
# The next line is essential. It creates an 
# object, 'motor' (you can name it anything)
# to hold the details about your stepper motor wiring. 
# It uses the stepper command from the adafruit_motor library.

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

# The for loop below represents just one approach to taking a step. 
# For more info on the arguments for the 'onestep' command, see 
# the "Stepper Motors" section of this page: 
# https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing/circuitpython

for step in range(STEPS):
    motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
    time.sleep(DELAY)

motor.release()

</pre>
{{< /expand >}}



# Project 2.5: Create a secure motor attachment

Because the third major project will require using a motor to actuate some part of an interactive game, in Project 2.5, you’ll building some knowledge about how to attach a part securely to a motor.

Your task in Project 2.5 is to design and build a motor hub that meets the following specifications:

-	Provides a 3 mm hole 15 mm from the shaft axis (you’ll insert a paper clip with a weighted string into this hole) 
-	Fits on and attaches to your motor shaft
-	Stays attached securely enough to handle the amount of torque that stalls the motor when it is operating at 12 V
-	Shaped like a spool or lever arm (i.e., shape is up to you)

![](/img/motor-hub-diagram.jpg)

Submit to Canvas a Solidworks or Onshape rendering of your design, and bring your hub to class. In class on the P2.5 due date, we will compile everyone’s results into histogram showing the range of torques applied before the hubs either (a) slip on their motor shaft or (b) successfully stall the motor.

**Due date: Tuesday, 10/25, at noon (in class)**

# Project #2: Build an H-bridge motor controller

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

# Project 1: Build a breadboard power supply

The first project is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for PCB submission): Thursday, September 22, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time.

### More details for project 1

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

# Project 0: Power an LED with "wall" power through our DC power supply. Control it with a push button.

The getting-started "project" is really more of a warm-up activity, and we'll do it together in class. The goal is to create a circuit on your breadboard that powers an LED with power from the wall, directed through your kit's DC power supply.  This circuit should have the following characteristics:

*   It is implemented on a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It turns on an LED when a push button is pressed.

**Due date (for submitting a photo of your circuit to Canvas): Thursday, September 8, 11:59 PM**




# Projects Assigned in Fall 2021

## Project #4: Build a whimsical, sort-of-public art installation

### System requirements

* It should consist of at least one sensor and at least one actuator that are not attached to each other.
* The sensor and actuator should communicate with each other through the internet.
* The system should do something beautiful, intriguing, or both, without physical intervention or control signals from you.
* The system should be enclosed and repel a [test finger probe](https://www.amazon.com/Articulated-Finger-accessibility-electrical-standards/dp/B0716YYXN2), like that used in UL/IEC 60950-1. The idea here is that you should try to give your system a finished appearance, with no holes where people can stick their fingers in.
* To the extent that this is possible, the system should be installed in public location, because the world needs more joy in the dark winter coming up. If you live by yourself on a dead-end street with no foot traffic, "public" to your cat is okay.

### Sensor requirements

* It should sense something. It should not be a simple binary sensor, i.e. not just a pushbutton.
* The sensor hardware should filter the raw sensor data so the readings reported to the actuator are smooth.
* It should run without a connection to a laptop. Batteries or a wall plug are okay.

### Actuator requirements

* It should physically move in response to your sensor.
* Including LEDs, displays, or sound is also good, but not required.
* It should query your sensor via HTTP.
* It should run without a connection to a laptop. Batteries or a wall plug are okay.

If you are working in a team, while it is probably wise to have one of you manage the sensor and one of you manage the actuator, you are both responsible for the entire system. Saying, "Well, my side works; it's his side that doesn't work," is the same as saying, "I have failed to get half of the project working." Both sides are your sides.

**Milestone 1: Build a mock-up: Wednesday, November 18, 11:59 PM**

**Final due date: Wednesday, December 2, 11:59 PM**

### More details for project #4

* If you need parts (like a sensor or a certain kind of motor), we're happy to order them for you.  
* See the [Raspberry Pi setup](http://andnowforelectronics.com/notes/rpi-setup/) page to learn how to control your Pi via serial cable and the Internet.  
* See the [Servers and Clients](http://andnowforelectronics.com/notes/series-vs-parallel/) page for resources on coding your Pi and Arduino to send and receive data through the Internet.  
* See the [client and server setup](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup) demo video that walks through the code for Raspberry Pis and Arduinos as clients and servers
* See the [Internet](http://andnowforelectronics.com/notes/internet/) page to find out how IP addresses work.  

### Teaming options for project #4

Project 4 requires an internet-connected sensor that can send data in response to a request from an internet-connected actuator. Due to internet firewalls, this communication is only possible when either (1) both the sensor and actuator are on the same wireless network (i.e., Tufts_Wireless, or the same home wireless router), or (2) the sensor operator has access to change the firewall settings of their wireless router (specifically, the port forwarding settings). You may have heard of people doing this to run an Xbox; it's the same situation, but just one port.

**Option 1 – Work by yourself**
You’ll need to use both your Raspberry Pi and your Arduino, both connected to the same wireless network. With this approach, an individual student can satisfy the project requirement to include a sensor and an actuator that are not physically connected to each other and that communicate through the internet.

**Option 2 – Work with a partner of your choice**
For this set-up to be successful, one of the following statements should be true:
* Both partners can access the Tufts campus network when testing and running your system, OR
* at least one partner (who operates the sensor node) has access to change the firewall (port forwarding) settings on their home wireless router, OR
* both partners are willing to work patiently with the ME 30 team on creating an encrypted tunnel through your firewall.

Be sure to ask any potential partners about their wireless situation both before and after Thanksgiving. The project is due on Dec. 1.

**Option 3 – Work with a partner assigned to you by Kristen and Brandon**
We’ll pool all the people who would like to be assigned a partner, and make optimal pairs based on your responses to the following questions about wireless network access.  
1)	Will you have access to the Tufts campus wireless network both before and after Thanksgiving?
2)	Do you have access to change the firewall (port forwarding) settings of your home wireless router?

-->
## Project #4: Build an intrepid robot that traverses the SEC

### System requirements

* On December 14th at 10:30 AM, your robot will be placed on the floor in the atrium near Blake.
* Your robot must do three things in order in less than 15 minutes:
  * High five an LA (target hand height 105.5-107 cm), seated conveniently nearby in the atrium
  * Travel to Jason Rife's office.
  * High five Jason Rife (target hand height 105.5-107 cm).
* Your robot should not be tethered to a wall outlet (batteries will be available in Nolop).

### Restrictions

* You should not touch your robot during its adventures. This probably means that your robot should be remote controlled.
* You should not use an RC car controller. This probably means that your robot should be controlled through wifi from a laptop or phone.
* Your robot cannot fly. (We don't have the space to test drones safely, unfortunately.)
* You cannot clear a path for the robot. This would include moving chairs, opening doors and the like. 

### Safe assumptions

* The doors at the top of the stairs that lead to the ME department hallway will be propped open.
* The atrium and hallways will be clear of chairs and similar obstacles. You will still need to traverse a variety of different surfaces.

**Milestone 1: Build something that drives: Tuesday, December 7, 10:30 AM**

* You should submit video documentation to Canvas and bring your something-that-drives to class. 
* Note: It would be a good idea to focus on making your robot drive effectively before you worry about any higher level mechanics or control through the internet.

**Final due date: Thursday, December 14, 10:30 AM (last class)**

* You should submit video documentation and code to Canvas and bring your robot to the atrium. 

### More details for project #4

* If you need parts (like a sensor or a certain kind of motor), we're happy to order them for you.  
* See the [Raspberry Pi setup](http://andnowforelectronics.com/notes/pi-setup/) page to learn how to control your Pi via serial cable and the Internet.  
* See the [Servers and Clients](http://andnowforelectronics.com/notes/servers-and-clients/) page for resources on coding your Pi and Arduino to send and receive data through the Internet.  
* See the [client and server setup](http://andnowforelectronics.com/notes/demo-videos/#client-and-server-setup) demo video that walks through the code for Raspberry Pis and Arduinos as clients and servers
* See the [Internet](http://andnowforelectronics.com/notes/internet/) page to find out how IP addresses work.  

## Project #3: Build an electromechanical game

Your task is to build a game with the following characteristics:

*   It is controlled by a microcontroller like an Arduino or Raspberry Pi. (Choose the Arduino unless you're a Pi zealot.)
*   It has at least one electromechanical element that moves, like a motor or a solenoid.
*   It has some kind of user input, like buttons, knobs, joysticks, sensors, or the like.
*   It is at least sort of fun to play. A blinking LED is not a game.
*   It is NOT a game that already exists, like skee-ball or checkers. It can be kinda similar to existing games, but you must use your creativity here.
*   (It does not need to have a custom PCB, but it can if you want. If it has a custom PCB, you must make a working prototype first.)

**Midway milestone: Bring a prototype to class and submit some photo or video documentation of it to Canvas: Tuesday, November 2nd (7 points)**

**Final demo in class and submit video of it in operation and your code to Canvas: Tuesday, November 16 (14 points)**

Class on November 16th will consist entirely of us playing each other's games.

### More details for project #3

If you need parts (like a sensor or a certain kind of motor), we're happy to order them for you. Keep in mind that it takes a few days for stuff to arrive through the mail.

It is a good plan to work hard on this project at the beginning, until you have some idea what stuff you might need, then build/buy/borrow what you need, then put it all together. (Then realize that despite your best efforts, not everything works the first time; scramble to recover.)

## Project #2.5: Build something to couple a winch to a motor shaft

This mini-project is to build an attachment to a motor shaft - torque contest

## Project #2: Build an H-bridge motor controller

The second project is to build a motor controller with the following characteristics:

*   It consists of a PCB with connectors for a motor, plus power and control lines.
*   It also accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It has a power LED that lights up when motor power is available.
*   It can make a DC motor spin in both directions.
*   The motor current traces can handle 12 V and 5 A continuously without melting.
*   It can be controlled by logic signals from an Arduino (but later, not as part of what you submit for P2).  


<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_708qmkve&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_mtijm1x6" width="400" height="285" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>  

**Due date for prototype: Tuesday, October 5, 11:59 PM**

To get started building your prototype H-bridge, review the [Low Power/high power](http://andnowforelectronics.com/notes/low-power-high-power/) and the H-bridge(http://andnowforelectronics.com/notes/h-bridges/) pages, including their mini-lecture videos on BJT and MOSFET transistors. After that, if you're stuck, consult the [H-bridge testing](http://andnowforelectronics.com/notes/demo-videos/) demo video.  Note that this video is not intended to give you step-by-step building or testing instructions, but rather to give you a feel for the kind of approach you might take to building and testing this circuit. If your H-bridge prototype isn't working by the deadline for this prototype, don't worry!  Just submit to Canvas a photo of what you have, working or not.  

**Due date for PCB submission: Tuesday, October 12, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 2 PCB assignment on Canvas. Also, take a screenshot of your PCB design in KiCad and upload that as well (it would be a good idea to save this screenshot for your portfolio). That will serve as proof that you submitted your project on time.

## Project #1: Build a breadboard power supply

The first project is to build a power supply with the following characteristics:

*   It consists of a PCB that plugs directly into a breadboard.
*   It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
*   It emits 12 V, 5 V, and 3.3 V (at the same time).

**Due date (for PCB submission): Tuesday, September 21, 11:59 PM**

When your design is ready, you should [submit it to the fabricator](https://oshpark.com/), OSH Park. It will cost you around $10\. After you submit it, take a screenshot of your order confirmation and upload it to the Project 1 PCB assignment on Canvas. That will serve as proof that you submitted your project on time.

### More details for project #1

First of all, we're not trying to build anything revolutionary in this project. None of you have ever made a PCB before, so the point is to make something fairly simple to get comfortable with the process. If you search Amazon for "breadboard power supply", you'll see that you can buy various versions of things like this, though none with a 12 V passthrough, so far as I'm aware.

Here's what a typical one of these things looks like.

![breadboard power supply](/img/breadboard-power-supply-from-amazon.jpg)

The image below shows the rough mechanical constraints for the PCB. You can make a board of whatever dimensions you want, but it needs to plug into the breadboard, so you probably want to follow the pin location dimensions shown below. You don't have to have pins where all of the 8 red dots are-- you could get by with just 4, but 8 will make the board stay in place a little more securely.

![](/img/breadboard-supply-mechanical-design.png)

In your project kit, you'll find all the components you'll need to build a prototype of your power supply on a breadboard. You build the prototype and make sure that you've got the wiring right. Then, make the PCB with the same connections. Finally, when your PCB arrives in the mail, you can reuse the prototype components on your PCB.

{{< hint danger >}}
**Important note #1: the pins on the two regulators are not in the same order!**
{{< /hint >}}

Check the datasheets for the components to see which pin is the input pin, which is the output pin, and which should connect to ground.

{{< hint danger >}}
**Important note #2: the pins on the power jack are weird! More details below.**

There's a cryptic diagram in the datasheet for the PJ-102AH power jack, shown below.

![power jack pinout](/img/power-jack-pinout.jpg)

One part is obvious: the pin in the middle is connected to pin 1.

But what is that little arrow/bump thing with pins 2 and 3?

That's trying to tell you that when the jack is empty (i.e. no plug inserted), pins 2 and 3 are connected together. When you insert the plug, the barrel pushes on the bump at the end of the pin 2 contact, which bends it away from the pin 3 arrow, breaking the connection to pin 3. It's so that you can detect whether there's a plug inserted or not, which can be useful for battery-powered systems. You don't need to implement that feature on your regulator board; you can just use pins 1 and 2.
{{< /hint >}}

### P1 prototype: what you should do before class #2

1. Make it so that 12 V goes into your circuit and 5 V comes out.
2. Install Kicad.
3. Try to replicate in Kicad the schematic of the circuit that you started building in the first class.
4. Watch the Kicad demo videos, a total of 5 minutes, 59 seconds for [the first two demo videos](http://andnowforelectronics.com/notes/demo-videos/)
5. Read and try to absorb the web pages listed under ["What to study" on the calendar](http://andnowforelectronics.com/logistics/calendar/)
6. If you can absorb material from books efficiently, read as much of chapter 2 from the Practical Electronics textbook as you can.
