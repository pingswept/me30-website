---
title: "Class 15: PWM"
draft: false
---

# Pulse width modulation (PWM) for variable speed control

Here is some sample CircuitPython code that uses PWM to run a motor first at full speed, then at half speed, and then at quarter speed. Note that we have to import the pwmio library to run this code, and we have to initiate a pin as a pwmio.PWMOut pin.

```python
import board
import pwmio
import time

my_control_pin = pwmio.PWMOut(board.D6, frequency=500, duty_cycle=0)
# creates a new object called “my_control_pin” that will hold all 
    # the information about sending out 
    # pulse-width modulation at pin D6

while True:
    my_control_pin.duty_cycle = 65535
    time.sleep(3)
    my_control_pin.duty_cycle = 32770
    time.sleep(3)
    my_control_pin.duty_cycle = 16400
    time.sleep(3)
```

**Frequency**: This CircuitPython parameter refers to the number of voltage pulse initiations per second.
- Set this to 500 for the KB2040, because its main processing chip can handle outputting that many cycles per second.

**Duty_cycle**: This CircuitPython parameter refers to the length of each voltage pulse. It's the duration of time, within each very brief control cycle, at which the voltage is ON or HIGH (i.e., 3.3 V).

For the KB2040, a duty cycle value of 65535 corresponds to the voltage being turned on for 100% of each very short PWM cycle, which means the motor gets 100% of the voltage available to it.

Because 50% of 65536 is about 32770, a duty cycle of about 32770 corresponds to the voltage being set high for 50% of the cycle, or the motor getting about 50% of the voltage available to it. The motor will spin at half speed.

A duty cycle of about 6550 corresponds to the voltage being set high for 10% of the cycle, or the motor getting about 10% of the voltage available to it.  The motor would spin at 10% speed IF that is enough voltage to overcome its internal friction (you’ll probably find that it’s not enough voltage for the motor to turn at all).

To use PWM to control the speed of a motor, you send the PWM signal to the control pin (gate or base) of a transistor. As shown below, the device that you are controlling (below, a motor) is wired to the main current-conducting path of the transistor.  

![Connecting a PWM pin to a transistor gate and motor](/img/pwm_motor_connection.jpg)

![Plot showing 3 duty cycles](/img/pwm_plot.jpg)
