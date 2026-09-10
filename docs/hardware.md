# Hardware Configuration

The project currently assumes the following wiring.

| Component | Configuration |
|---|---|
| Ultrasonic TRIG | BCM 23 |
| Ultrasonic ECHO | BCM 24 |
| IR left | BCM 22 |
| IR middle | BCM 27 |
| IR right | BCM 17 |
| Left track | Motor channels 2 and 4 |
| Right track | Motor channels 1 and 3 |
| Onboard LEDs | GPIO 9, 25, 11 |
| WS2812 LEDs | 2 pixels through `spi_ws2812` |

## Sensor polarity

`line_follow.py` uses:

```python
LINE_IS_BRIGHT = True
```

The code normalizes the sensor readings so that the decision logic always treats:

```text
1 = line detected
0 = no line
```

Verify the raw readings on your physical robot before changing the flag.

## Motor calibration

Physical turning depends on battery voltage, wheel traction, floor surface, and robot geometry. The square-driving exercise currently uses:

```python
TURN_TIME = 1.3
```

Tune this value experimentally if needed.
