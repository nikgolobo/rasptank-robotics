# obstacle_alert.py
# Robot drives forward, stops when an obstacle is detected, flashes LEDs, then resumes.

import sys
import time
import RPi.GPIO as GPIO
sys.path.insert(0, '/home/pi/raspTank/lib')
import motor as M
from spi_ws2812 import Adeept_SPI_LedPixel

FORWARD = -1
SPEED = 35
LEFT_TRACK = (2, 4)
RIGHT_TRACK = (1, 3)
TRIG = 23
ECHO = 24
THRESHOLD_CM = 20

def forward():
    for channel in LEFT_TRACK + RIGHT_TRACK:
        M.Motor(channel, FORWARD, SPEED)

def stop_motors():
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

led = Adeept_SPI_LedPixel(count=2, bus=0, device=0)

def flash_red(times=3, period=0.3):
    for _ in range(times):
        led.set_all_led_color(255, 0, 0)
        time.sleep(period / 2)
        led.set_all_led_color(0, 0, 0)
        time.sleep(period / 2)

try:
    while True:
        distance = get_distance()
        if distance < 0:
            print('No valid sensor reading', flush=True)
            stop_motors()
        elif distance <= THRESHOLD_CM:
            print(f'Obstacle at {distance} cm -> STOP', flush=True)
            stop_motors()
            flash_red(times=3)
        else:
            print(f'Clear: {distance} cm -> FORWARD', flush=True)
            led.set_all_led_color(0, 0, 0)
            forward()
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nProgram stopped.')
finally:
    stop_motors()
    led.set_all_led_color(0, 0, 0)
    led.led_close()
    M.destroy()
    GPIO.cleanup()
