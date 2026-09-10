# move.py
# Drive the robot in a square using reusable movement functions.

import sys
import time
sys.path.insert(0, '/home/pi/raspTank/lib')
import motor as M

FORWARD = -1
BACKWARD = 1
LEFT_TRACK = (2, 4)
RIGHT_TRACK = (1, 3)
SPEED = 40

def _drive(left_direction, left_speed, right_direction, right_speed):
    """Set the direction and speed of both tracks."""
    for channel in LEFT_TRACK:
        M.Motor(channel, left_direction, left_speed)
    for channel in RIGHT_TRACK:
        M.Motor(channel, right_direction, right_speed)

def forward():
    _drive(FORWARD, SPEED, FORWARD, SPEED)

def backward():
    _drive(BACKWARD, SPEED, BACKWARD, SPEED)

def turn_left():
    _drive(FORWARD, 0, FORWARD, SPEED)

def turn_right():
    _drive(FORWARD, SPEED, FORWARD, 0)

def stop():
    M.motorStop()

DRIVE_TIME = 1.5
TURN_TIME = 1.3

try:
    for side in range(4):
        print(f'Side {side + 1}: forward')
        forward()
        time.sleep(DRIVE_TIME)
        stop()
        time.sleep(0.2)
        print(f'Turn {side + 1}: right')
        turn_right()
        time.sleep(TURN_TIME)
        stop()
        time.sleep(0.2)
    print('Square complete.')
    stop()
except KeyboardInterrupt:
    print('\nProgram stopped by user.')
    stop()
finally:
    M.motorStop()
    M.destroy()
