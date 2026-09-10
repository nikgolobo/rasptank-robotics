# motor_speeds.py
# Move the robot forward at three different speeds.

import sys
import time
sys.path.insert(0, '/home/pi/raspTank/lib')
import motor as M

FORWARD = -1

def set_speed(speed):
    """Set all four motors to the same forward speed."""
    for channel in (1, 2, 3, 4):
        M.Motor(channel, FORWARD, speed)

try:
    print('Full speed: 100')
    set_speed(100)
    time.sleep(2)
    print('Half speed: 50')
    set_speed(50)
    time.sleep(2)
    print('Quarter speed: 25')
    set_speed(25)
    time.sleep(2)
    print('Stop')
    M.motorStop()
finally:
    M.motorStop()
    M.destroy()
