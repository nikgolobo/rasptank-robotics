# custom_led_pattern.py
# Custom heartbeat pattern for three onboard LEDs.

from gpiozero import LED
import time

led1 = LED(9)
led2 = LED(25)
led3 = LED(11)

def all_leds_on():
    led1.on()
    led2.on()
    led3.on()

def all_leds_off():
    led1.off()
    led2.off()
    led3.off()

try:
    while True:
        all_leds_on()
        time.sleep(0.1)
        all_leds_off()
        time.sleep(0.1)
        all_leds_on()
        time.sleep(0.25)
        all_leds_off()
        time.sleep(0.8)
except KeyboardInterrupt:
    print('Program stopped.')
finally:
    all_leds_off()
