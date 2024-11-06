---
title: "KB2040 challenges"
draft: false
---

## KB2040 challenges

### Set 1

1. Make your KB2040 flash an external LED so there are 2 flashes per second, controlled by pin D5.
2. Make your KB2040 send the text, "I, for one, welcome our new insect overlords." to your serial monitor once per second.[^1]
3. Use a 10k resistor to pull pin D5 high or low (i.e., physically toggle between sending it either positive voltage or 0 volts, through a resistor). Print out the pin's state as "HIGH" or "LOW" on the serial monitor every time it changes.
4. Make an LED on D6 mirror the state of D5, controlled by the 10k resistor as in the previous challenge.
5. Make an LED attached to pin D6 send Morse code for "TUFTS".
6. Turn your gearmotor on for 5 seconds, then off for 5 seconds, then repeat, using pin D6. You'll probably need a transistor for this.

### KB2040 + H-bridge challenge
Use an H-bridge circuit to make your gearmotor spin clockwise for 5 seconds, then counterclockwise for 5 seconds, using pins D5 and D6.


### Set 2

7. Make your gearmotor slowly increase in speed for 5 seconds, then slowly decrease in speed for 5 seconds, then repeat, using pin D6.
8. Use your potentiometer to make a variable voltage. Read the voltage with pin A0, then print the voltage (in volts) to the serial monitor.
9. Use your potentiometer on pin A0 to control the speed of your gearmotor on pin D6.
10. Use a resistor in series with your photoresistor to make a voltage that changes with light exposure. Use that voltage to control the speed of your gearmotor on pin D6.
11. Use a pushbutton on pin D5 to control when your motor is on and off, using D6 for motor control.


### Solutions for Set 1

{{< expand "See the schematic diagrams for 1 to 6" "..." >}}

![Schematics for challenges 1 to 6](/img/Challenge_Schematic_1-6.jpg)

{{< /expand >}}


{{< expand "See breadboard wiring sketches for 1 to 6" "..." >}}

![Schematics for challenges 1 to 6](/img/Challenge_Wiring_1-6.jpg)

{{< /expand >}}


{{< expand "See CircuitPython code for 1 to 6" "..." >}}

![Code for 1](/img/challenge1py.jpg)

![Code for 2](/img/challenge2py.jpg)

![Code for 3](/img/challenge3py.jpg)

![Code for 4](/img/challenge4py.jpg)

![Code for 6](/img/challenge6py.jpg)

{{< /expand >}}

### Solutions for H-bridge and Set 2

{{< expand "See the schematic diagrams for Set 2" "..." >}}

![Schematic for challenges 8 to 11](/img/Challenge_Schematic_8-11.jpg)

{{< /expand >}}


{{< expand "See breadboard wiring sketches for H-Bridge and Set 2" "..." >}}

![Schematics for challenges 8 to 10](/img/Challenge_Wiring_8-10.jpg)
![Schematics for challenges 11 and H-bridge](/img/Challenge_Wiring_11-Hbridge.jpg)


{{< /expand >}}


{{< expand "See CircuitPython code for H-bridge and Set 2" "..." >}}

![Code for 8](/img/challenge8py.jpg)

![Code for 9](/img/challenge9py.jpg)

![Code for 10](/img/challenge10py.jpg)

![Code for 11](/img/challenge11py.jpg)

![Code for H-bridge](/img/challengeHbridgepy.jpg)

{{< /expand >}}


[^1]: If you're like Kristen and didn't get this cultural reference, here's an explanation: https://knowyourmeme.com/memes/i-for-one-welcome-our-new-insect-overlords
