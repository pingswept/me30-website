---
title: "Class 20: Raspberry Pi challenges"
draft: false
---

## Raspberry Pi challenges

1. Boot the Pi and log in.
2. Create a new directory called `fun-stuff`.
3. Create a new file in `fun-stuff` that is called `poem.txt` and write a poem about ME 30.
4. Install `pip` and `RPi.GPIO` and write a Python 3 script that sets pin 13 high. Test with an LED (don't forget a current-limiting resistor for your LED).
5. Write a Python 3 script that sets pin 13 high if the value of pin 16 is also high. Test with an LED at pin 13 and a button and 10K pull-down resistor at pin 16.
6. Write a Python 3 script that prints "button pressed" when you press a button that you've wired between ground and pin 18. (Hint: you'll probably need to set pin 18's internal pull-up resistor.)
7. Write a Python 3 script to change the speed of your motor using PWM.
8. Install Flask and start it running.
9. Modify your Flask instance so when you request the URL `http://IP_ADDRESS_OF_YOUR_PI:5000/runmotor`, your motor turns on.
