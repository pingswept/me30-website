---
title: "Crucial questions"
draft: false
---

## Crucial questions for the semester  

1. If we're trying to light up an LED with a 5 V supply, why do we need a resistor in series?
2. How much power can 5 V drive into a 100 ohm resistor? Could the resistors in your project kit handle that?
3. Does a motor get hotter when it's going fast or slow? Why?
4. Can you store more energy in a 100 uF capacitor or in a lithium ion battery of the same volume?
5. Why are extension cords rated for a certain voltage and current? How is a cord with higher ratings different?
6. Using the stuff in your project kit, devise a few different ways to overload your voltage regulator circuit and tell us which one would dissipate the most power, and why.
7. How much energy is there in an AA battery? In a 9V battery? Which has higher energy density by volume, and why?
8. Compared to the N-channel set-up, what would you need to do differently to use a P-channel MOSFET to switch your 12-V DC gearmotor on and off? 
9. What would be the advantages of using the P-channel as a high-side driver instead of a low-side driver?
10. How would you select an appropriate motor for a robot elbow?


## Learning objectives

1.	Complete five hands-on circuit design projects:
    a.	  Build a prototype and PCB of a breadboard power supply that accepts power from a 12 V wall supply and emits 12 V, 5 V, and 3.3 V at the same time.
    b.	  Build a prototype and PCB of an H-bridge motor controller to make a motor spin both ways.
    c.	  Build an electromechanical game including microcontroller, moving mechanical element, and user input.
    d.	  Build a node including both sensor(s) and actuator(s) in an internet-connected, electronic system.
    e.	  Combine an internet-connected, electronic system with a moving mechanical element.
2.	Distinguish between voltage and current and apply working definitions of voltage and current to explain energy transfer in simple circuits. 
3.	Describe the relationships among voltage, current, resistance, and power. 
4.	Gain proficiency with breadboard prototyping.
5.	Turn a breadboard prototype into a printed circuit board using PCB design software.
6.	Explain how to use transistors to control high power with low power.
7.	Compare and contrast different types of motors (DC, stepper, and servo) and build circuits incorporating each kind.
8.	Explain how an H-bridge motor controller works.
9.	Learn the basic code/upload/test/debug cycle for microcontrollers. 
10.	Gain basic familiarity with microcontroller hardware.
11.	Gain familiarity with incorporating microcontroller hardware peripherals into circuit designs, including the i2C module, PWM module, and serial port module.
12.	Gain enough familiarity with Python programming to code an electromechanical game controlled by an RP2040 microcontroller.
13.	Describe how the internet works.
14.	Gain familiarity with Linux basics and explain how they relate to the functioning of a Raspberry Pi. 
15.	Identify the main components and functions of the Raspberry Pi.
16.	Describe the basics types of control in the context of the motor(s) used in course projects, and RP2040 or RPi.
17.	Become familiar with the frequency domain and digital filters.
18.	Reflect on strengths and weaknesses of one’s project management approach in an open-ended design project. 
19.	Gain exposure to managing a bill of materials, supply chain, and verification vs validation.
20.	Build engineering ethics fluency by exploring the impact of internet-connected electronic technologies on various stakeholders, including in environmental and societal contexts.
21.	Define discriminatory design, explain a case where it has occurred, and identify an approach to avoid it.

**Feather RP2040 prep**  

(1) If you are a complete newcomer to microcontrollers, consider attending one of the special office hour tutorials in which we will walk you through the steps outlined below. Schedule for those tutorials are TBD.

(2) Skim the ME 30 website notes [on microcontrollers](http://andnowforelectronics.com/notes/microcontrollers/), the [Feather RP2040](http://andnowforelectronics.com/notes/feather-rp2040-hardware/), and [Feather programming](http://andnowforelectronics.com/notes/feather-programming/). (You'll want to read them in more depth later on; for now, just get a sense for what's there.)  

(3) Download the Mu editor from Adafruit's website and install the Mu editor on your laptop. https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor 

(4) Follow the directions for installing Circuit Python on your Feather RP2040. https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

(5) Complete the following initial Feather programming task:

Make your Feather blink its onboard LED once per second. You can find code and instructions in the "Creating Code" section of Adafruit's Circuit Python tutorial website [here](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code).  


