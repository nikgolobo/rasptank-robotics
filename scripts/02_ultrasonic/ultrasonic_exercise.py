# ultrasonic_exercise.py
# Classify the measured distance from the ultrasonic sensor.

import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """Return the measured distance in centimetres, or None if the sensor times out."""
    GPIO.output(TRIG, False)
    time.sleep(0.05)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    t0 = time.time()
    while GPIO.input(ECHO) == 0:
        if time.time() - t0 > 0.1:
            return None
    pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        if time.time() - pulse_start > 0.1:
            return None
    pulse_end = time.time()
    return round((pulse_end - pulse_start) * 17150, 1)

def classify(distance):
    """Return a label based on the measured distance."""
    if distance is None:
        return 'NO SIGNAL'
    elif distance < 10:
        return 'DANGER'
    elif distance <= 30:
        return 'CLOSE'
    elif distance <= 100:
        return 'NEAR'
    else:
        return 'FAR'

try:
    while True:
        dist = get_distance()
        label = classify(dist)
        if dist is None:
            print(label)
        else:
            print(f'{dist} cm -> {label}')
        time.sleep(0.5)
finally:
    GPIO.cleanup()
