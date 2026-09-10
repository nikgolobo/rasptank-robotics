# obstacle_avoidance.py
# Drive forward, detect obstacles, alternate left/right turns, and continue.

import sys
import time
import RPi.GPIO as GPIO
sys.path.insert(0, '/home/pi/raspTank/lib')
import motor as M

FORWARD = -1
LEFT_TRACK = (2, 4)
RIGHT_TRACK = (1, 3)
SPEED = 35
TRIG = 23
ECHO = 24
THRESHOLD_CM = 25
TURN_TIME = 0.6

def _drive(left_direction, left_speed, right_direction, right_speed):
    for channel in LEFT_TRACK:
        M.Motor(channel, left_direction, left_speed)
    for channel in RIGHT_TRACK:
        M.Motor(channel, right_direction, right_speed)

def forward():
    _drive(FORWARD, SPEED, FORWARD, SPEED)

def turn_left():
    _drive(FORWARD, 0, FORWARD, SPEED)

def turn_right():
    _drive(FORWARD, SPEED, FORWARD, 0)

def stop():
    M.motorStop()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance(timeout=0.04):
    GPIO.output(TRIG, False)
    time.sleep(0.05)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    wait_start = time.time()
    while GPIO.input(ECHO) == 0:
        if time.time() - wait_start > timeout:
            return -1.0
    pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        if time.time() - pulse_start > timeout:
            return -1.0
    pulse_end = time.time()
    return round((pulse_end - pulse_start) * 17150, 1)

turn_left_next = True

try:
    while True:
        distance = get_distance()
        print(f'Distance: {distance} cm', flush=True)
        if distance < 0:
            print('No reading -> STOP', flush=True)
            stop()
            time.sleep(0.2)
        elif distance <= THRESHOLD_CM:
            stop()
            time.sleep(0.2)
            if turn_left_next:
                print('Obstacle -> TURN LEFT', flush=True)
                turn_left()
            else:
                print('Obstacle -> TURN RIGHT', flush=True)
                turn_right()
            time.sleep(TURN_TIME)
            stop()
            time.sleep(0.1)
            turn_left_next = not turn_left_next
        else:
            forward()
        time.sleep(0.05)
except KeyboardInterrupt:
    print('\nProgram stopped.')
finally:
    stop()
    M.destroy()
    GPIO.cleanup()
