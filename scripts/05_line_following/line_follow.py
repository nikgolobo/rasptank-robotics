#!/usr/bin/env python3
# line_follow.py
# Follow a line using three IR sensors.

import sys
import time
from gpiozero import InputDevice
sys.path.insert(0, '/home/pi/raspTank/lib')
import motor as M

FORWARD = -1
LEFT_TRACK = (2, 4)
RIGHT_TRACK = (1, 3)
SPEED = 35
TURN_FAST_SPEED = 50
TURN_SLOW_SPEED = 15
LOST_TIMEOUT = 0.6
LINE_IS_BRIGHT = True

left_ir = InputDevice(pin=22)
middle_ir = InputDevice(pin=27)
right_ir = InputDevice(pin=17)

def _drive(left_dir, left_spd, right_dir, right_spd):
    """Set direction and speed for the left and right tracks."""
    for channel in LEFT_TRACK:
        M.Motor(channel, left_dir, left_spd)
    for channel in RIGHT_TRACK:
        M.Motor(channel, right_dir, right_spd)

def forward():
    _drive(FORWARD, SPEED, FORWARD, SPEED)

def turn_left():
    _drive(FORWARD, TURN_SLOW_SPEED, FORWARD, TURN_FAST_SPEED)

def turn_right():
    _drive(FORWARD, TURN_FAST_SPEED, FORWARD, TURN_SLOW_SPEED)

def stop():
    M.motorStop()

last_seen = 0
last_turn = stop

print('L | M | R | Action')
print('-' * 34)

try:
    while True:
        l = left_ir.value
        m = middle_ir.value
        r = right_ir.value
        if not LINE_IS_BRIGHT:
            l = 1 - l
            m = 1 - m
            r = 1 - r
        if m and not l and not r:
            action = forward
            name = 'forward'
            last_seen = time.time()
        elif l and not r:
            action = turn_left
            name = 'turn left'
            last_turn = turn_left
            last_seen = time.time()
        elif r and not l:
            action = turn_right
            name = 'turn right'
            last_turn = turn_right
            last_seen = time.time()
        elif not l and not m and not r:
            if time.time() - last_seen < LOST_TIMEOUT:
                action = last_turn
                name = 'lost -> keep last turn'
            else:
                action = stop
                name = 'lost -> stop'
        else:
            action = stop
            name = 'intersection -> stop'
        print(f'{l} | {m} | {r} | {name}', flush=True)
        action()
        time.sleep(0.04)
except KeyboardInterrupt:
    print('\nStopping.', flush=True)
finally:
    stop()
    M.destroy()
