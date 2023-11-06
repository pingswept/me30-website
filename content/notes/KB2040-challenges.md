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

### Set 2

7. Make your gearmotor slowly increase in speed for 5 seconds, then slowly decrease in speed for 5 seconds, then repeat, using pin D6.
8. Use your potentiometer to make a variable voltage. Read the voltage with pin A0, then print the voltage (in volts) to the serial monitor.
9. Use your potentiometer on pin A0 to control the speed of your gearmotor on pin D6.
10. Use a resistor in series with your photoresistor to make a voltage that changes with light exposure. Use that voltage to control the speed of your gearmotor on pin D6.
11. Using D6 for motor control, use a pushbutton on pin D5 to trigger when your motor is on and off.
12. Use an H-bridge circuit to make your gearmotor spin clockwise for 5 seconds, then counterclockwise for 5 seconds, using pins D5 and D6.

### Hints
    {{< expand "Click to see circuit schematics for all the challenges." "..." >}}

![schematics](/img/Challenge_Schematics.jpg)
{{< /expand >}} 

    {{< expand "Click to see wiring diagrams for all the challenges." "..." >}}

![wiring 1-7](/img/Challenge_Wiring1-7.jpg)

![wiring 8-10](/img/Challenge_Wiring8-10.jpg)

![wiring 11-12](/img/Challenge_Wiring11-12.jpg)
{{< /expand >}} 

[^1]: If you're like Kristen and didn't get this cultural reference, here's an explanation: https://knowyourmeme.com/memes/i-for-one-welcome-our-new-insect-overlords
