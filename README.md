# RaspTank Robotics Exercises

A collection of Raspberry Pi / Adeept RaspTank robotics exercises covering LEDs, ultrasonic sensing, motor control, obstacle avoidance, and IR line following.

## Repository structure

```text
rasptank-robotics/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── docs/
│   ├── achievement.md
│   ├── hardware.md
│   ├── project-description.md
│   └── running.md
├── scripts/
│   ├── 01_leds/
│   ├── 02_ultrasonic/
│   ├── 03_motors/
│   ├── 04_obstacle_avoidance/
│   └── 05_line_following/
├── .gitignore
├── CONTRIBUTING.md
├── README.md
└── requirements.txt
```

## Hardware assumptions

These scripts were written for a Raspberry Pi based Adeept RaspTank-style robot.

Important mappings used by the exercises:

- Ultrasonic sensor: `TRIG = BCM 23`, `ECHO = BCM 24`
- IR line sensors: left `BCM 22`, middle `BCM 27`, right `BCM 17`
- Left motor track: channels `2, 4`
- Right motor track: channels `1, 3`
- Three onboard LEDs: GPIO `9, 25, 11`
- Two WS2812 LEDs: accessed through the robot's `spi_ws2812` library
- Robot library path: `/home/pi/raspTank/lib`

Check your own robot before running the scripts because motor direction, sensor polarity, and wiring can differ.

## Setup

Clone the repository on the Raspberry Pi:

```bash
git clone <your-repository-url>
cd rasptank-robotics
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

The Adeept-specific `motor` and `spi_ws2812` modules are expected to already exist in:

```text
/home/pi/raspTank/lib
```

## Exercises

### 1. LEDs

```bash
python3 scripts/01_leds/custom_led_pattern.py
python3 scripts/01_leds/ws2812_colors.py
```

### 2. Ultrasonic sensor

```bash
sudo python3 scripts/02_ultrasonic/ultrasonic_exercise.py
sudo python3 scripts/02_ultrasonic/ultrasonic_filter.py
```

### 3. Motor control

```bash
sudo python3 scripts/03_motors/motor_speeds.py
sudo python3 scripts/03_motors/move.py
```

`move.py` contains the calibrated square-driving version with `TURN_TIME = 1.3`.

### 4. Obstacle avoidance

```bash
sudo python3 scripts/04_obstacle_avoidance/obstacle_alert.py
sudo python3 scripts/04_obstacle_avoidance/obstacle_avoidance.py
```

### 5. Line following

First inspect the raw IR readings:

```bash
sudo python3 scripts/05_line_following/line_sensor_raw.py
```

Then run the line follower:

```bash
sudo python3 scripts/05_line_following/line_follow.py
```

The current `line_follow.py` is the latest version from the project and uses differential track speeds for smoother corrections.


## Achievement

### Constructor University Summer Camp 2026

Participated in the **Constructor University and Constructor Talent School Summer Camp 2026** in Bremen, Germany, from **24 July to 4 August 2026**.

Academic focus:
- Mathematics & Modeling
- Neural Networks & Robotics

The camp included hands-on work with robotics, sensors, programming, and applied problem-solving.

## Project Description

This repository contains a hands-on Raspberry Pi robotics project developed around an Adeept RaspTank-style robot. The project demonstrates progressively more advanced robot-control tasks in Python, including:

- onboard LED and WS2812 RGB LED control;
- ultrasonic distance measurement and noise filtering;
- reusable motor-control abstractions;
- calibrated forward movement and turning;
- obstacle detection and reactive obstacle avoidance;
- IR line-sensor reading and polarity handling;
- line-following logic with recovery after temporary loss of the line.

The project was built as part of practical robotics study focused on understanding how sensors, control logic, and actuators work together in a real robot.


## Project Demonstration

The repository includes two videos from physical robot testing on a marked indoor course.

### Course test 01

![Robot course test 01 preview](assets/images/robot-course-test-01-preview.jpg)

[Watch `robot-course-test-01.mp4`](assets/videos/robot-course-test-01.mp4)

### Course test 02

![Robot course test 02 preview](assets/images/robot-course-test-02-preview.jpg)

[Watch `robot-course-test-02.mp4`](assets/videos/robot-course-test-02.mp4)

These recordings document real-world calibration of movement and navigation behaviour. They show why physical robotics requires iterative tuning: turning and tracking depend on motor characteristics, battery level, wheel traction, and floor surface.

See [`docs/media.md`](docs/media.md) for more detail.

## Safety

Test motor scripts with the tracks lifted off the floor first. Keep the robot in a clear area and be ready to stop the program with `Ctrl+C`.

## Notes

This repository keeps the original exercise scripts separate rather than converting them into a Python package, because they directly control hardware and are intended to be run individually.
