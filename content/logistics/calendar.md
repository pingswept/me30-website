---
title: "Calendar"
draft: false
---

# 2026 Class Calendar

## Phase 1: Circuit basics

| Class | Date  | Class topics                                  | Hands-on                                        | What to study                                                                                                | What's due                                                    |
|:-----:|:-----:|--------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
|   01  | 9/9   | Course overview, introductions, kit contents  | Breadboard basics; power an LED with wall power | [LEDs](/notes/leds/); [Prototyping](/notes/prototyping/); [Voltage and current](/notes/voltage-and-current/) |          |
|   02  | 9/14  | Voltage, current, resistors, voltage dividers | Voltage dividers  | [Multimeters](/notes/multimeter/); [Resistors](/notes/resistors/); [Series vs. parallel](/notes/series-vs-parallel/) |  |
|   03  | 9/16  | Voltage regulators, capacitors, Project 1 & Motor hub HW intro                | Project 1 start; labs begin                     | [Capacitors](/notes/capacitors/); [Voltage regulators](/notes/voltage-regulation/); [Videos for P1](/notes/demo-videos/#videos-for-project-1)  |  |
|   04  | 9/21  | Voltage regulators, Project 1                 | Debug your voltage regulator, capacitor circuit     | [Voltage regulators](/notes/voltage-regulation/); [Videos for P1](/notes/demo-videos/#videos-for-project-1); [Adafruit soldering guide](https://learn.adafruit.com/adafruit-guide-excellent-soldering/making-a-good-solder-joint)    | [P1   proto](/logistics/projects/#project-1-build-a-breadboard-power-supply) |        |
|   05  | 9/23  | KiCad                                         | KiCad demo                                      | [PCB design](/notes/pcb/); Kicad resources  | Motor hub HW due 9/25 |
|   06  | 9/28  | PCB design                                    | KiCad Q & A; Soldering demo                                     | [PCB design](/notes/pcb/); [KiCad demo videos](/notes/demo-videos/#introduction-to-kicad-with-a-simple-led-board)    |  |


## Phase 2: Motors and transistors

| Class | Date  | Class topics                                  | Hands-on                        | What to study                                                            | What's due                                                    |
|:-----:|:-----:|-----------------------------------------------|---------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------|
|   07  | 9/30  | Transistors as switches                       | Make a switch with a BJT        | [Low power/high power](/notes/low-power-high-power/)|[P1 PCB](/logistics/projects/#project-1-build-a-breadboard-power-supply)|        |
|   08  | 10/5  | Intro to P2 (game v1), DC motors, MOSFETs     | Run a motor with a MOSFET       | [Motors](/notes/motors/) |              |
|   09  | 10/7  | Microcontrollers, CircuitPython               | KB2040 set-up                   | [KB2040 hardware](/notes/feather-rp2040-hardware/); [Microcontrollers](/notes/microcontrollers/); Solder pins to your KB2040 and bring to class |  Motor bracket HW due 10/9    |
|       | 10/12 | NO CLASS                                      | (Indigenous People's Day)       |  |        |
|   10  | 10/14 | Digital and analog I/O hardware               | De-bugging challenges; KB2040 challenges set 1  |    [KB2040 programming](/notes/kb2040-programming/); [KB2040 challenges](/notes/kb2040-challenges/)    |   
|   11  | 10/19 | H-bridges, P3 intro                                     | Start building an H-bridge      | [H-bridge motor driver](/notes/h-bridge/) | [P2 (game v1)](/logistics/projects) due Wed. in class|
|   12  | 10/21 | More H-bridge details            | More H-bridge work              | [H-bridge motor driver](/notes/h-bridge/); [Intro and video for P3](/logistics/projects/#project-2-build-an-h-bridge-motor-controller)             | [KB2040 challenge #6 HW](http://andnowforelectronics.com/notes/kb2040-challenges/)      |
|   13  | 10/26 | Motor electrical & mechanical power   | Motor measurement; Run your H-bridge with your KB2040   |     |[P3 proto](/logistics/projects/#project-2-build-an-h-bridge-motor-controller)|
|   14  | 10/28 | Intro to P4, PWM           | More motor measurement  |   |  |


## Phase 3: Microcontrollers and sensors

| Class | Date  | Class topics                       | Hands-on                 | What to study | What's due  |
|:-----:|:-----:|------------------------------------|--------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------|
|   15  | 11/2  | Motor modeling, more PWM                | KB2040 challenge #7; P4 planning              |      | [P3 PCB](/logistics/projects/#project-2-build-an-h-bridge-motor-controller)   |
|   16  | 11/4  | Sensors, state machines intro      | KB2040 challenges, set 2 | [KB2040 challenges](/notes/kb2040-challenges/); [KB2040 programming](/notes/kb2040-programming/) | P4 learning goal HW due 11/6 |
|   17  | 11/9  | State machines, Stepper motors     | KB2040 challenges, set 2 | [KB2040 challenges](/notes/kb2040-challenges/); [KB2040 programming](/notes/kb2040-programming/)| KB 2040 challenge #10 HW |
|   18  | 11/10 | Ethical considerations for lithium batteries  | P4 work                  | | Lithium batteries HW due 11/12   |
|       | 11/11 | NO CLASS, but notice Tuesday, 11/10 | (Veteran's Day)          |  |  |
|   19  | 11/16 | Raspberry Pi intro                 | Booting the Raspberry Pi | [Raspberry Pi programming](/notes/pi-programming/); [Raspberry Pi setup](/notes/pi-setup/)   |      |
|   20  | 11/18 | P4 reflection; Intro to P5 Stage 1     | P4 demo day              |       |   [P4](/logistics/projects); Pi set-up HW due 11/20  |  

## Phase 4: Driving robots with operating systems

| Class | Date  | Class topics                  | Hands-on                   | What to study | What's due  |
|:-----:|:-----:|-------------------------------|----------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------|
|   21  | 11/23 | Raspberry Pi programming      | Pi challenges              | [Raspberry Pi challenges](/notes/pi-challenges/)  |    | 
|       | 11/25 | NO CLASS                      | (Thanksgiving)             |           |        |
|   22  | 11/30 | Sensor amplification; op-amps          | Amplify a strain gauge; measure with multimeter     | [I2C sensors](/notes/i2c/); [Sensor amplification](/notes/amplification)      |      |
|   23  | 12/2  | Oscilloscopes                  | Oscilloscope sim; load cell de-bugging |       | Load cell FBD HW     |
|   24  | 12/7  | How does the internet work?   | P5 work time               | [Internet](/notes/internet/); [Servers and clients](/notes/servers/)              | Op amp circuit HW  |
|   25  | 12/9  | P5 Stage 2                 | P5 Stage 1 reflection                |          | [P5](/logistics/projects) due Tues. night  |
|   26  | 12/14 | Career trajectories | P5 Stage 2 Q & A                   |                               |         |
|       | 12/16 | 12 to 2 PM - Project demo option 1       |                            |             |[P5 stage 2](/logistics/projects)|
|       | 12/17 | 12 to 2 PM - Project demo option 2    |                            |             |[P5 stage 2](/logistics/projects)|
|       | 12/18 | 12 to 4 PM - Project demo option 3       |                            |             |[P5 stage 2](/logistics/projects)|

## Lab Calendar

| Lab # | Lab dates          | Lab focus  | 
|:-----:|:------------------:|----------------------|
|   0   | 9/9-9/11           | No lab; Drop-in help sessions for breadboard novices during lab times |
|   1   | 9/16-9/18          | Voltage divider & voltage regulator circuits |
|   2   | 9/23-9/25          | Learn KiCad |
|   3   | 9/30-10/2          | Control a motor with BJT + potentiometer |
|   4   | 10/7-10/9          | P2 help |
|   5   | 10/14-10/16        | KB2040 challenges set 1 |
|   6   | 10/21-10/23        | H-bridges on breadboards |
|   7   | 10/28-10-30        | H-bridge PCB help |
|   8   | 11/4-11/6          | KB2040 challenges w/ sensors (set 2) |
|   9  | 11/10, 11/12-11/13 | P4 help |
|   10  | 11/18-11/20        | Rasp Pi set-up and challenges |
|       | 11/25-11/27        | No labs (Thanksgiving week) |
|   11  | 12/2-12/4          | Sensor amplifier |
|       | 12/9-12/11         | Labs shift to drop-in help sessions open to all |






