---
title: "Exercises"
draft: false
---
# In-class exercises for Fall 2025

## 1: Power an LED with "wall" power (Class 1)

For a warm-up activity, let's power an LED with "wall" power and control it with a push button. 

Your goal is to create a circuit on your breadboard that lights up an LED with power from the wall, directed through your kit's DC power supply. This circuit should have the following characteristics:

- It is implemented on a breadboard.
- It accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter.
- It turns on an LED when a push button is pressed.

The components are:

1. DC power supply
2. One power (barrel) jack
3. One LED
4. One resistor (What size? See [these notes](http://andnowforelectronics.com/notes/resistors/#typical-application-current-limiter).)
5. One pushbutton
6. Various wires and a breadboard

The image below is a circuit diagram representation of what you're building.

![Wall-powered LED circuit](/img/project0_circuit.png)


**For an extension to this exercise,** re-arrange your circuit so you have one LED that stays on permanently and another that is powered by the button.


{{< hint danger >}}
**Important note: the pins on the power jack are weird! More details below.**

There's a cryptic diagram in the [datasheet](http://andnowforelectronics.com/notes/datasheets/) for the PJ-102AH power jack, shown below.

![power jack pinout](/img/power-jack-pinout.jpg)

One part is obvious: the pin in the middle is connected to pin 1.

But what is that little arrow/bump thing with pins 2 and 3?

That's trying to tell you that when the jack is empty (i.e. no plug inserted), pins 2 and 3 are connected together. When you insert the plug, the barrel pushes on the bump at the end of the pin 2 contact, which bends it away from the pin 3 arrow, breaking the connection to pin 3. It's so that you can detect whether there's a plug inserted or not, which can be useful for battery-powered systems. You don't need to implement that feature on your regulator board; you can just use pins 1 and 2.

In the cross-section view of a barrel plug inserted into the jack, you can see how the outer sheath of the plug makes contact with pin 2 and also how the plug breaks the continuity between pin 3 and pin 2.  

![barrel jack cross section](/img/BarrelJackMultipleViews.jpg)

Image credit: E. Schlaepfer and W. Oskay, 2023, Open Circuits, opencircuitsbook.com
{{< /hint >}}


## 2. LED circuit details (Class 2)

Would the functioning of Circuit A (left) be any different than that of Circuit B (right)? Why or why not? What evidence would prove your answer?

![LEDs with resistors](/img/led-resistor-location-exercise.jpg)

Does it matter if the resistor is "above" or "below" the LED?



## 3. Safety check (Class 2)

1. If you feel a circuit component getting hot or starting to smoke, what should you do first?

      a) Call over an LA
  
      b) Take the component out of the breadboard
  
      c) Unplug the power supply (e.g., barrel jack) from the breadboard
  
      d) Use your multimeter to measure the voltage across the component


2. What is a possible result if your multimeter dial is turned to the “mA” symbol and you put your multimeter probes between a high and low voltage location on a circuit?

      a) You’ll get zero current reading on your multimeter and prevent your circuit from working

      b) You’ll let too much current go through your multimeter and blow its fuse

      c) You’ll hear a beeping sound warning you that you should use the “A” symbol and port

4. Which of these three circuits can you safely build on your breadboard? (hint: the resistor power rating is 0.5W)

![Current Limiting Circuit](/img/Safety_circuits.png)

## 4. Current limiting resistors (Class 2)

Which circuit gives the brightest LED? 
![Current Limiting Circuit](/img/Current_limiting_circuits.png)

## 5. Build voltage dividers (Class 2)

We've used resistors to limit *current* flow through an LED.  

Let's see how we can also use them to reduce a *voltage* so we can supply a specific lower voltage to a device. For example, we might be using a 12 V power supply but want to supply only 5 V to an Arduino or other microcontroller. 

Read more [here](http://andnowforelectronics.com/notes/resistors/#typical-application-current-limiter) about using resistors as current limiters and voltage dividers.

For each of the set-ups below, provide 12 V as V_in, and predict the output voltage V_out. 

After you've written down your predictions for V_out, build the circuits and use your multimeter to measure V_out. If your predictions were off, try to figure out why.

![Voltage dividers](/img/voltage_dividers.jpg)

## 6: Matching schematics to breadboards (Class 3)

Which of these breadboards has the same circuit as the one represented in the schematic?

![Schematic and breadboards](/img/Breadboard_schematic_matching.jpg)

## 7: Build a voltage regulation circuit (Class 3)

This is an introductory exercise designed to help you get familiar with breadboard prototyping while also building a basic circuit that will be useful for later exercises and projects. It forms the basis for Project #1, but you don't need to think about that yet. If this is all new to you, look at the pages on [breadboard prototyping](/notes/prototyping/) and [multimeters](/notes/multimeters/).

Your goal is to put 4 components and some wires on your breadboard to achieve this goal: **12 volts go in; 5 volts come out**.

The 4 components are:

1. One power jack
2. One L7805CV voltage regulator
3. Two capacitors

## 8: Review of voltage and current (Class 3 and 4)

For the circuit below, analyze the following first for when the switch is open, and then for when the switch is closed:
1. Find sets of labeled points on the circuit where the **current** is the **same**.
2. Identify any points on the circuit where **no** current is flowing.
3. List the points in order from **highest current flow to least current flow**.
4. Find sets of points where the **voltage** is the **same**.
5. At what points should the voltage be near 0 V (e.g., ground)?
6. Order the points from highest to lowest voltage.
  
![Circuits to analyze](/img/Voltage_current_review.jpg)

## 9: Discharge a capacitor and observe the RC time constant (Class 4)

![capacitor discharge circuit](/img/capacitor_discharge.jpg)

1. What sequence of button presses makes the LED flash, and then fade out?
2. From the R and C values you can create with your kit, what combination of R and C will produce the slowest rate of fade for the LED (that you can observe)? The fastest rate of fade (still observable)?
3. Try to explain, conceptually, why the rate of fade varies with R*C. (We will look at this mathematically as well.)  

## 10. Control a motor with a BJT (Class 7)

Making a motor spin is pretty simple: apply sufficient voltage across its leads. When we want to control things like motors (or LEDs, buzzers, etc.) electronically, instead of plugging them in to breadboards with our hands, we use transistors. The goal of this exercise is to use a bipolar junction transistor, the 2N3904, to turn on and off a motor.

You need 5 things in addition to the usual 12 V power supply and barrel jack:

1. A 3.3 V voltage source, like the voltage regulation circuit you built previously
2. A 2N3904 transistor (or really any transistor is fine, if you know the pinout)
3. A DC gear motor
4. An appropriately-sized current-limiting resistor for the BJT

The picture below shows the concept of what you're building. 

![Typical BJT circuit](/img/typical-bjt-circuit.jpg)

**Extension:** Add a potentiometer (a variable resistor) in series with the base and use it to vary the current flowing from base to emitter. Notice how this works as a crude motor speed controller, but also notice (carefully!) how the BJT heats up as more current is drawn through it.

![BJT circuit with potentiometer](/img/bjt-potentiometer.jpg)

## 11. Determine pin voltages and ideal resistor value for a BJT circuit (Class 7 and 8)

1. For the circuit shown in Exercise #7, fill in the table below to indicate the voltage at E, B, and C when the base resistor is connected to (a) 0 V and (b) 3.3 V.
2. To run your kit's gear motor, what is an ideal value for the resistor between 3.3 V and the base of the transistor?


|  | V_E  | V_B   | V_C |
|:----:|:-----:|:----:|:----:|
|  Input at O V   |    |   |     |
|  Input at 3.3 V   |    |   |     |

## 12. Control a motor with a MOSFET (Class 8)

You've used a bipolar junction transistor to control a motor. Now try using the other main class of transistor: a metal oxide semiconductor field effect transistor, or MOSFET.  The main difference between the [two types of transistors](http://andnowforelectronics.com/notes/low-power-high-power/) is that BJTs are current-controlled, and MOSFETs are voltage-controlled.

You need 5 things:

1. 3.3 V voltage source, which you can make using the 3.3V regulator in your kit
2. 12 V voltage source
3. An N-channel MOSFET
4. A DC gear motor
5. A pull-down resistor for the MOSFET

![MOSFET circuit](/img/mosfet-controller.jpg)

## 13. De-bugging challenges set 1 (Class 10)

Images of circuits: https://tufts.box.com/s/8al3jwc3l81ewtb16ridfo2ewqbjtc3v

## 14. KB2040 microcontroller challenges set 1 (Class 10 and labs)

Learn to program your KB2040 board by working through the first 6 of these 12 challenges: http://andnowforelectronics.com/notes/kb2040-challenges/

You'll want to consult the [KB2040 programming](http://andnowforelectronics.com/notes/kb2040-programming/) resources.

For Kristen's 1-page summary of the most important Circuit Python commands for your KB2040, click [here](https://tufts.box.com/s/lczswqulqewphbxyku1zpvazp73govzi).

## 15. Project 2 takeaways reflection (Class 11)

(a) What are some problems you encountered along the way of working on your game for Project 2, and what did you learn from them? Let's collectively document those [here](https://docs.google.com/document/d/1yKv0bKWhP53wHEWxWcOBskjrUdKzZLRV_DfW0eVWal0/edit?usp=sharing).

(b) Take a moment to fill out the [self-assessment for Project 2](https://tufts.qualtrics.com/jfe/form/SV_7PAFa4Tk6kXRZ1s), if you have not done so already.

## 16. Recognizing common errors in KB2040 Challenge #6 (Class 11)

Challenge #6 asks you to control a motor's on/off state with a KB2040 output pin. Below are two approaches to setting up the circuitry. Each has problems that will prevent it from working correctly. What do you think those problems are?

![Microcontroller problems](/img/Micro_with_transistors_flawed.jpg)

*What are the problems with approach #1?*

{{< expand "See the answer" "..." >}}
(a) The KB2040 GND pin is not tied to the same ground as the motor circuitry.

(b) There is no current-limiting resistor between the KB2040 output and the BJT base. We want to keep the current through the base-emitter diode to about 10% of the collector-to-emitter current. If the motor is drawing 150 mA, then we want the base-emitter current to be about 15 mA. And we know that when the BJT is on, its base voltage is 0.6 V. Since the KB2040 output supplies 3.3 V, we need a resistor to drop the voltage by 2.7 V and limit the current to something closer to 15 mA. A resistor somewhere between 100 and 1000 ohms should do it.

![Fixed circuit](/img/Micro_BJT_Fixed.jpg)
{{< /expand >}}

*What are the problems with approach #2?*

{{< expand "See the answer" "..." >}}
(a) The motor is "below" the N-channel MOSFET. When the gate is supplied with voltage, **for a very brief moment** the gate voltage will be higher than the source voltage, and current will flow from drain to source and therefore through the motor.  But once current starts to be drawn through the motor, the voltage at the source will rise to somewhere near 12 V. At this point, the gate voltage of 3.3 V will be less than the source voltage, and the MOSFET will no longer allow current flow to the motor.

(b) The MOSFET gate does not have a pull-down resistor to ground.

(c) The KB2040 GND pin is not tied to the same ground as the motor circuitry.

![Fixed circuit](/img/Micro_MOSFET_Fixed.jpg)
{{< /expand >}}

## 17. Mechanically controlled two-way motor circuit (Class 11)

With a partner or two, build a circuit that will allow you to use pushbutton switches to toggle a 12-V DC motor between the states of (a) OFF (b) ON counterclockwise, and (c) ON clockwise. That means your motor needs to be able to draw current in either direction (only one direction at a time). Your circuit should NOT use transistors. It should include (a) 12 V adapter and barrel jack, (b) DC gearmotor, (c) assorted wires, (d) as many pushbutton switches as you want.

As you work on this challenge, **be careful not to create a situation where you are sending 12 V to ground only through wires.** That's a short circuit and will cause heat and smoke!

![Motor with question marks](/img/Exercise_2waymotor.jpg)

## 18. H-bridge circuit analysis  (Class 12)

You've just wired up the top left corner of an H-bridge circuit using a P-channel MOSFET. You connect the other motor lead to ground so that you can test this corner before wiring up the transistors at any other corners.  If this corner is wired correctly, 

1. What should happen to the motor when the MOSFET gate is connected:

- to 12 V?  
- to ground?  

2. Sketch the current path for each of those gate states.

![Top left corner of an H-bridge](/img/Hbridge-corner.png)

Now you add a BJT as a different method for switching on the P-channel MOSFET. Again, you want to test this corner before moving on to other sections of the H-bridge. If the BJT and P-channel MOSFET in this corner are wired correctly, 

1. What should happen to the motor when the BJT base is:

- at 3.3 V?  
- at ground?  

2. Sketch the current path for each of those base states.
3. What is the voltage at G for each of those base states?

![add BJT to corner of an H-bridge](/img/Hbridge-corner-BJT.jpg)

## 19. H-bridge circuit analysis, part 2 (Class 13)

**This H-bridge circuit has four inputs, shown at locations 1, 2, 3, and 4. Each input turns a transistor on or off.**

*If all four switches were connected to 3.3 V (as shown below), what would happen and why?*  

![H-bridge inputs all at 3.3 V](/img/Hbridge_all3v.jpeg)

{{< expand "See the answer" "..." >}}
**Don't do this -  it will short the circuit!!** In this H-bridge, setting a corner input to 3.3 V turns that corner's MOSFET "on," allowing current to across the source-drain pathway. If all 4 MOSFETs are allowing current to flow, then this circuit's easiest path to ground will be down the two sides of the "H."  No current will flow through the highly resistive motor. The motor will not spin, and the rest of the circuit will get very hot.
{{< /expand >}}

## 20. Test the current limit of your P1 PCB (Class 14)

The voltage regulators on your P1 PCB are specified (on their data sheets) to be able to handle current at the level of 1.5 A (the 5V regulator) and 0.8 A (the 3.3 V regulator). But the question is - **once soldered into your P1 PCB, can they still perform up to their specified max current limit?**  

**Test your P1 PCB by determining how much current your regulators can actually send out to loads at your output pins before going into thermal shutdown.**

General procedure (details left to your group):
- Determine the resistance (it will be a low value!) you should attach to your 3.3 V and 5 V output so that something close to the specified max current is drawn (0.8 A or 1.5 A, respectively)
- Attach those low-ohm resistors to the output. These resistors stand in for a motor or other load to which you would want to supply 3.3 V or 5 V
- Monitor the voltage drop across that resistive load - that is, the voltage drop between the output of the regulator and ground
- Once that voltage drop begins to decrease lower than 3.3 V or 5 V, your regulator has gone into thermal shutdown (you may feel the regulators getting very hot before this happens)

Use this [shared doc](https://tinyurl.com/ME30questiondoc) to post questions about the P1 PCB test and about P3 circuit board design.

## 21a. Measure a DC gearmotor (Power In) (Class 14)

Here are a few basic measurements you can make to understand your DC gearmotor better. The overall goal is to determine the efficiency of the motor by comparing the electrical power that goes into it ("power in") with the mechanical power it delivers ("power out"). 

We'll start with determing the minimum and maximum current that the motor draws.

1. When your motor is stalled (like if you're trying to lift something too heavy with it), it behaves like a resistor. This is when your motor draws maximum current, so checking the resistance is a good way to estimate the maximum current for whatever drive voltage you choose. Using the resistance-measuring setting of your multimeter (the omega symbol, Ω, represents ohms), measure the resistance of the coils of your motor.
2. Make your DC gearmotor spin by connecting your motor directly to your 12 V DC power supply using alligator clips. Then, measure the current the motor draws with no load attached by putting your multimeter in series with the motor. You should switch your multimeter to the A setting (for Amps), and move the red lead to the port on the left side of the meter that is labeled "A". The black lead stays in the black port labeled "COM".

With measurement #1 above (the resistance of the coils), you can estimate the **maximum current** the motor will draw at any voltage. With measurement #2, you can find the **minimum current at 12 V**. 

When you know the current and the voltage, you can multiply them to find the electrical power going into the motor.

If you can estimate how much power a task will require, you can start to figure out what voltage this motor would need to deliver that power (assuming perfect efficiency, for now). That's the first step toward deciding whether this is the right motor for whatever you're building.

## 21b. Measure a DC gearmotor (Power Out) (Class 14)

The next step is to determine how much mechanical power the motor actually delivers ("power out"). One way to do this is to measure the time it takes to perform a certain amount of work (i.e., to add energy to a system).

1. Use tape and string to hang a water bottle from your motor shaft.
2. Measure the time it takes your motor to lift a known weight a specific distance (you could try something like 0.5 kg of water, lifted up 1 m). Compute the amount of work done in lifting the water. With these two values (work and time), you can find "power out."
3. Compare "power in" and "power out" to estimate the motor's efficiency. You may want to measure "power in" at this motor operating point by measuring current while the water is being lifted.

## 22. Motor speed-torque curve (Class 15)

Fill in values in the boxes to complete the motor speed-torque curve for the DC gearmotor in your ME 30 kit.

![speed torque curve](/img/speed-torque.jpg)

## 23. Motor selection cases (Class 15)

For each of these potential motorized game designs, determine whether the mechanical power and torque needs are within the capabilities of the DC gearmotor in your ME 30 kit.
- Can your motor handle these designs with a direct-drive approach (i.e., no gear trains or pulleys)? Why or why not?
- If your motor can't handle the design via direct-drive, can it do the job with a gear train or pulley transmission? Why or why not?
  
Work in a small group and post your answers to this google doc:
https://docs.google.com/spreadsheets/d/18il0YS9v-0mt79J7DdHGnpuPw71HNZ7vh3b1nPuhzdM/edit?usp=sharing

![banana launcher case](/img/motorcase1.jpg)
![claw assembly case](/img/motorcase2.jpg)
![popcorn launcher case](/img/motorcase3.jpg)

## 24. Analog and digital sensors (Class 16)

Circuits A and B show different ways to send a varying input to a KB2040 pin. Circuit A uses a photoresistor, a component whose resistance depends on the amount of light shining on it. Circuit B uses a simple pushbutton. 

1. Which of the set-ups below involves *analog* input to the microcontroller, and which involves *digital* input? Why?  What will need to be different about your KB2040 code to measure voltage at A0 (in the photoresistor circuit) versus measuring voltage at D6 (in the push-button circuit)?

Build each of the circuits below and program your KB2040 to measure the input voltage from the point specified in the circuit. Answer the questions below.

2. For Circuit A, vary the light level, and explore the range of voltages that your KB2040 pin receives (at the point specified in the schematic).
3. How does the voltage at A0 relate to the light level (i.e., as the light level increases, does voltage at A0 increase or decrease)?
4. How does the photoresistor's resistance relate to the light level (i.e., as the light level increases, does its resistance increase or decrease)?

![photoresistor and push-button voltage dividers](/img/Sensors_Exercise.jpg)

## 25. More practice with sensors and PWM (Class 16)

Set up KB2040 challenge #10: 

Use a resistor in series with your photoresistor to make a voltage that changes with light exposure. Use that voltage to control the speed of your gearmotor on pin D6. 

Now try to add an LED whose brightness also varies with the light exposure to the photoresistor.  Think carefully both about the code and the circuit components that you need to make this addition.

## 26. How to code your microcontroller to constantly check an input while also running actuators (Class 16)

Suppose you want to check for the state of inputs while also running motors, lights, and other actuators.

In particular, try to do these three tasks at once:

1. flash an LED ("led_1" in the code), 3 seconds on, 3 seconds off.
2. constantly check for a button press that sets an input pin HIGH.
3. flash a *different* LED ("led_2" in the code) when the button is pressed.

### The naive approach

Here's a reasonable first attempt by a novice programmer to set up a microcontroller to check for input and flash a second LED when a button is pressed.

Why will this code probably **not work very well** to accomplish the goal stated above?

{{< expand "Click to see the code that won't work very well" "..." >}}
<pre class="code">
import board
import digitalio as dio
import time

led_1 = dio.DigitalInOut(board.D4)
led.direction = dio.Direction.OUTPUT

led_2 = dio.DigitalInOut(board.D5)
led_2.direction = dio.Direction.OUTPUT
    
button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

led_1.value = False

while True:
    # toggle the first LED
    if led_1.value is True:
        led_1.value = False
    else:
        led_1.value = True

    # wait the 3 seconds
    time.sleep(3.0)

    # check the button and toggle the second LED
    if button.value is True:
        led_2.value = True
    else:
        led_2.value = False
</pre>
{{< /expand >}}

### Try a state machine instead!

Writing code for “state machines” is a better technique for this situation. At this [link](https://gist.github.com/pingswept/1d37a74943f73a6266688db44f3e382d) (and in the box below) is one way to set up state machines in CircuitPython. 

{{< expand "Click to see the state machine code" "..." >}}
<pre class="code">
import board
import digitalio as dio
import time

led_1 = dio.DigitalInOut(board.D4)
led_1.direction = dio.Direction.OUTPUT

led_2 = dio.DigitalInOut(board.D5)
led_2.direction = dio.Direction.OUTPUT
    
button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

STATE_TOGGLE = 1       # these are just arbitrary constants used to number the states
STATE_CHECK_BUTTON = 2 # the values 1 and 2 are not significant

state = STATE_TOGGLE
next_toggle = 0
led_1.value = False

while True:
    if state is STATE_TOGGLE:
        if led_1.value is True:
            led_1.value = False
        else:
            led_1.value = True
        next_toggle = time.monotonic() + 3.0 # this is like setting a timer to expire 3 seconds in the future
        state = STATE_CHECK_BUTTON
    elif state is STATE_CHECK_BUTTON:
        if button.value is True:
            led_2.value = True
        else:
            led_2.value = False
        if time.monotonic() > next_toggle: # this is like checking the timer we set above
            state = STATE_TOGGLE
</pre>
{{< /expand >}}


State machine algorithms can be conceptually represented by circles and arrows. Each state is represented by one circle. Arrows indicate what happens immediately after the commands in one state have been completed. 

In the diagram below, add labels to the arrows to represent the rules for moving between the "CHECK BUTTON" and "TOGGLE" states.

![state machine diagram](/img/StateMachineDiagram.jpg)

## 27. Using a state machine with a motor (Class 17)

Imagine a Project 4 game with a 1-foot arm attached to the DC gearmotor shaft. Mounted at the end of the arm is a bowl. The motor switches directions every two seconds in order to move the bowl back and forth, switching directions every 2 seconds, as the player tries to toss a bean bag into the bowl.   In the base of the bowl is a button whose purpose is to sense the presence of the bean bag. When the button gets pressed by the bean bag, the player wins! The motor stops moving and a celebratory green LED light blinks quickly 10 times.

Let's set up a state machine for the code for this game.

Make a state machine diagram with circles and arrows to show:
1. What are the two states needed in the main program?
2. What are the rules for switching from one state to another, or for returning to the same state?

Draft the Circuit Python code to implement this state machine.

Sketch a circuit diagram that shows how you would wire up all the components.

## 28. Using a state machine with two inputs (Class 17)

Set up KB2040 challenge #10 (where the speed of a gearmotor on pin D6 is controlled by the light exposure on a photoresistor).

Now, add a button that switches which direction the motor is going. How could a state machine help you implement this feature?

## 29. Stepper motor set-up (Class 17)

With one or two partners, set up two working breadboard H-bridges. Choose one KB2040 and one stepper motor to use for this exercise. Hook up each coil of the stepper motor to one H-bridge. Connect one KB2040 digital output pin to each "diagonal" pair of H-bridge corners. You'll use four KB2040 output pins in total.  Control the motor using the code provided here: http://andnowforelectronics.com/notes/kb2040-programming/#stepper-motors

Note that you will need the adafruit_motor library. All CircuitPython libraries for the KB2040 can be downloaded [here](https://circuitpython.org/libraries). Download the entire library bundle to your laptop, and then transfer ONLY the libraries you need to your KB2040.

## 30. More sensors and actuators (Class 17)

1. **Potentiometer for input; motor speed for output.** Send the voltage output from a potentiometer (knob- or dial-like variable resistor) to an analog input pin on your KB2040. Use that varying voltage to vary the speed of a motor. **Extension:** Add a button that switches the direction of the motor (you'll likely need state machine code for this.)

3. **Ultrasonic distance sensor for input; motor direction for output.** Send the output voltage from a distance sensor to an analog input pin on your KB2040. Use that distance signal to trigger whether your motor spins clockwise or counter clockwise. You get to decide on the distance threshold for switching directions.

4. **Pushbutton for input; piezo buzzer for output.** Use a pushbutton to send either 3.3 V or 0 V to a digital input pin on your KB2040. Use that button signal to trigger the sound of a buzzer. Power the buzzer with PWM. Explore different frequency and duty cycle values, and see how that changes the sound of the button.

## 31. Raspberry Pi Flask set-up and challenges (Class 19)

Make sure you can complete [Raspberry Pi challenges #7, #8, and #9](http://andnowforelectronics.com/notes/pi-challenges/)

## 32. Amplify a strain gauge (Class 22)

Add details later

## 33. Project 5 planning, Q & A (Class 22 and 23)

(a) Discuss these Project 5 planning questions with your team: https://tufts.box.com/s/hs2supj34cp4mar33w4fsitflc4m4o6c

(b) Use this [shared doc](https://tinyurl.com/ME30questiondoc) to post questions about Project 5.

## 34. Oscilloscopes and PWM signals (Class 23)

Consider the following Python code, which powers pin 12 on a Raspberry Pi with the pulse-width modulation (PWM) protocol. The goal of this code is to gradually increase the speed of a motor, 2 seconds per speed increment, until it is running at full speed.

<pre class="code">
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pin12 = GPIO.PWM(12, 500)  # channel=12 frequency=500Hz

    while True:
        pin12.start(0)  # initial duty cycle of 0
        for i in range(0, 11):
            pin12.ChangeDutyCycle(10*i)
            time.sleep(2)
        pin12.stop
</pre>

Suppose the code doesn’t seem to be making the motor behave as predicted.

You decide to troubleshoot the code by monitoring the signal at pin 12 with an oscilloscope.

An oscilloscope is a tool for measuring electrical signals, like a multimeter, but it keeps a record of voltage and current over time. And it displays that record graphically, on a plot of voltage (or current) vs time. It can detect signals at very small time increments, down to milliseconds.

(1) To see the distinct PWM cycles in the oscilloscope window, to what horizontal and vertical scale should you set the window? Let’s say you want to see 5 distinct PWM cycles displayed on the window at any given point in time. What should be the settings for time per horizontal division and volts per vertical division? 

(2) Draw a quick sketch of what the signal should look like on the scope window when the for loop in the code is at i = 5.

(3) Use the oscilloscope simulator to represent what the signal will look like on the scope at i = 5. You’ll need to adjust both the signal generator (the instrument in the top half of the screen) and the scope settings.
https://www.pzdsp.com/elab/virtual_oscilloscope.html

## 35. ME 30 career connections and Project 6 planning (Class 26)

We'll use these slides today: https://docs.google.com/presentation/d/1KQUk6XxwHb4ZOj-VtnntzEh-BJyFNbJ3YQ1TYeTOjiQ/edit?usp=sharing



