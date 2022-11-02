# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Use this example for digital pin control of an H-bridge driver
# like a DRV8833, TB6612 or L298N.

# For wiring, see https://lastminuteengineers.com/stepper-motor-l298n-arduino-tutorial/

import time
import board
import digitalio
from adafruit_motor import stepper

# Set DELAY as the length of time that the motor runs for each step. Adafruit suggests 0.01, but ME 30 folks have found this delay value needs to be much shorter. If 0.01 doesn't work, try something as short as 0.005.

DELAY = 0.01

# Set the number of steps for one rotation of the motor. For the stepper motor in the ME 30 kit, one rotation takes 200 steps.

STEPS = 200

# You can use any available GPIO pin on both a microcontroller and a Raspberry Pi.
# The following pins are simply a suggestion. If you use different pins, update
# the following code to use your chosen pins.

# To use with CircuitPython and a microcontroller:
coils = (
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

# To use with a Raspberry Pi:
# coils = (
#     digitalio.DigitalInOut(board.D19),  # A1
#     digitalio.DigitalInOut(board.D26),  # A2
#     digitalio.DigitalInOut(board.D20),  # B1
#     digitalio.DigitalInOut(board.D21),  # B2
# )

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

# Each for loop below represents just one approach to taking a step. 
# Your final code should choose one of them. 
# For more info on what these different commands mean, see 
# the "Stepper Motors" section of this page: 
# https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing/circuitpython

for step in range(STEPS):
    motor.onestep()
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(style=stepper.DOUBLE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(style=stepper.INTERLEAVE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    time.sleep(DELAY)

motor.release()
