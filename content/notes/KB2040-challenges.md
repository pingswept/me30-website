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
11. Use a pushbutton on pin D5 to control when your motor is on and off, using D6 for motor control.
12. Use an H-bridge circuit to make your gearmotor spin clockwise for 5 seconds, then counterclockwise for 5 seconds, using pins D5 and D6.

### Hints

{{< expand "Click to see circuit schematics for the challenges" "..." >}}

![schematics](/img/Challenge_Schematicsnew.jpg)
{{< /expand >}} 


{{< expand "Click to see wiring diagrams for the challenges" "..." >}}

Note that circuits 6, 7, 9, 10, and 11 include pull-down resistors between the MOSFET gate and ground. Your circuits would basically work without them, but your motor might spin even when the MOSFET gate is not being intentionally sent 3.3 V.

![wiring 1-7](/img/Challenge_Wiring1-7new.jpg)

![wiring 8-10](/img/Challenge_Wiring8-10new.jpg)

![wiring 11-12](/img/Challenge_Wiring11-12new.jpg)
{{< /expand >}} 

{{< expand "Click to see CircuitPython code for the challenges" "..." >}}

![py1](/img/challenge1py.jpg)

![py2](/img/challenge2py.jpg)

![py3](/img/challenge3py.jpg)

![py4](/img/challenge4py.jpg)

![py6](/img/challenge6py.jpg)

![py7](/img/challenge7py.jpg)

![py8](/img/challenge8py.jpg)

![py9](/img/challenge9py.jpg)

![py10](/img/challenge10py.jpg)

![py11](/img/challenge11py.jpg)

![py12](/img/challenge12py.jpg)

{{< /expand >}} 

[^1]: If you're like Kristen and didn't get this cultural reference, here's an explanation: https://knowyourmeme.com/memes/i-for-one-welcome-our-new-insect-overlords
