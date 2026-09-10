# ws2812_colors.py
# Cycle through colours, then run a breathing effect.

import sys
import time
sys.path.append('/home/pi/raspTank/lib')
from spi_ws2812 import Adeept_SPI_LedPixel

led = Adeept_SPI_LedPixel(count=2, bus=0, device=0)

def set_color(red, green, blue):
    """Set both WS2812 LEDs to the same colour."""
    led.set_all_led_color(red, green, blue)

def breathing_effect(red, green, blue):
    """Fade one colour in and out."""
    for brightness in range(0, 256, 5):
        adjusted_red = int(red * brightness / 255)
        adjusted_green = int(green * brightness / 255)
        adjusted_blue = int(blue * brightness / 255)
        set_color(adjusted_red, adjusted_green, adjusted_blue)
        time.sleep(0.03)
    for brightness in range(255, -1, -5):
        adjusted_red = int(red * brightness / 255)
        adjusted_green = int(green * brightness / 255)
        adjusted_blue = int(blue * brightness / 255)
        set_color(adjusted_red, adjusted_green, adjusted_blue)
        time.sleep(0.03)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]

try:
    while True:
        for red, green, blue in colors:
            set_color(red, green, blue)
            time.sleep(1)
        breathing_effect(255, 0, 255)
except KeyboardInterrupt:
    print('\nProgram stopped.')
finally:
    set_color(0, 0, 0)
    led.led_close()
