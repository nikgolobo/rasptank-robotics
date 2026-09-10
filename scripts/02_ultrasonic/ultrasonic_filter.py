# ultrasonic_filter.py
# Implement the three filtering functions.

import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """Returns one raw reading in cm, or None on timeout."""
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

def median_of(readings):
    """Return the median value from a list of numbers."""
    sorted_readings = sorted(readings)
    middle_index = len(sorted_readings) // 2
    return sorted_readings[middle_index]

def get_stable_distance(samples=5):
    """Take several raw readings, ignore None values, and return the median."""
    readings = []
    for _ in range(samples):
        distance = get_distance()
        if distance is not None:
            readings.append(distance)
    if len(readings) == 0:
        return None
    return median_of(readings)

history = []

def moving_average(new_value, window=5):
    """Keep only the latest window values and return their average."""
    history.append(new_value)
    history[:] = history[-window:]
    average = sum(history) / len(history)
    return round(average, 1)

try:
    while True:
        raw = get_distance()
        stable = get_stable_distance(samples=5)
        smooth = moving_average(stable) if stable is not None else None
        print(f'raw: {str(raw):>7} cm  |  median: {str(stable):>7} cm  |  smoothed: {str(smooth):>7} cm')
        time.sleep(0.1)
finally:
    GPIO.cleanup()
