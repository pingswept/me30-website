Example

```python
# Joystick math based on code by Richard Klancer, circa 2012

MAX_SPEED = 100

import RPi.GPIO as GPIO
from math import atan2, sin, cos, pi, sqrt

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

pwmLeft = GPIO.PWM(12, 0.5)
pwmRight = GPIO.PWM(32, 0.75)

@public.route('/joystick/<x>/<y>')
def joystick(x, y):

    """Accepts a joystick position (x, y) where x and y represent a point within the unit circle.
       Returns a tuple (left, right) of the corresponding motor speeds for a left and right motor in
       a differential drive setup. Left and right are integers in the range -MAX_SPEED..MAX_SPEED"""

    fx = float(x)
    fy = float(y)
    
    angle = atan2(fy, fx) - pi/4

    # interpret the distance from the center
    speed = sqrt(fx*fx + fy*fy)
    if speed > 1.0:
        raise ValueError("Joystick input outside the unit circle")

    left = sin(angle)
    right = cos(angle)
    # scale the motor speeds so that, if the joystick is pushed to its maximum distance from the
    # center, the faster motor is at max speed regardless of the angle
    scale = MAX_SPEED * speed / max(abs(left), abs(right))
    pwmLeft.start(int(scale * left + 0.5))
    pwmRight.start(int(scale * right + 0.5))
    return "ok"
```
