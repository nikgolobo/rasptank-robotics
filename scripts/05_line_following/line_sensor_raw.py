#!/usr/bin/env python3
# line_sensor_raw.py
# Read three IR line sensors and print a direction.

import time
from gpiozero import InputDevice

left = InputDevice(pin=22)
middle = InputDevice(pin=27)
right = InputDevice(pin=17)

def get_direction(left_value, middle_value, right_value):
    """Convert sensor readings into a human-readable direction. 1=line, 0=no line."""
    if left_value == 1 and middle_value == 0 and right_value == 0:
        return 'LEFT'
    elif left_value == 0 and middle_value == 1 and right_value == 0:
        return 'CENTRE'
    elif left_value == 0 and middle_value == 0 and right_value == 1:
        return 'RIGHT'
    elif left_value == 0 and middle_value == 0 and right_value == 0:
        return 'LOST'
    elif left_value == 1 and middle_value == 1 and right_value == 0:
        return 'SLIGHT LEFT'
    elif left_value == 0 and middle_value == 1 and right_value == 1:
        return 'SLIGHT RIGHT'
    elif left_value == 1 and middle_value == 0 and right_value == 1:
        return 'CENTRE'
    elif left_value == 1 and middle_value == 1 and right_value == 1:
        return 'CENTRE'
    else:
        return 'UNKNOWN'

print('Left | Middle | Right | Direction')
print('-' * 42)
try:
    while True:
        left_value = left.value
        middle_value = middle.value
        right_value = right.value
        direction = get_direction(left_value, middle_value, right_value)
        print(f'  {left_value}  |   {middle_value}    |   {right_value}   | {direction}')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nStopped.')
