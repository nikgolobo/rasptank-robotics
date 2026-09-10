# Project Description

This project is a practical Python robotics project for a Raspberry Pi–based Adeept RaspTank-style tracked robot.

The robot is programmed around the classic **sense–decide–act** control loop:

1. **Sense** — read ultrasonic and IR sensors.
2. **Decide** — filter noisy data, interpret the environment, and choose a movement command.
3. **Act** — control the tracks and LEDs in real time.

## Main capabilities

The project includes:

- onboard LED and WS2812 RGB LED control;
- ultrasonic distance sensing;
- median filtering and moving-average smoothing;
- reusable motor-control abstractions;
- calibrated forward, backward, left-turn, right-turn, and stop functions;
- square-driving experiments;
- obstacle alerts with LED feedback;
- reactive obstacle avoidance;
- raw IR line-sensor diagnostics;
- sensor-polarity normalization;
- line-following logic;
- temporary line-loss recovery using remembered turn direction;
- live console telemetry for debugging robot decisions.

## Physical testing and calibration

A major part of the work was testing the robot on a real indoor course and tuning the control parameters from observation.

The experiments show that robotics is not only about writing correct code. Physical behaviour is affected by:

- motor differences;
- battery voltage;
- floor friction;
- wheel or track slip;
- turning duration;
- sensor noise;
- sensor polarity;
- overshoot and oscillation.

The final testing included driving on a marked indoor course, adjusting turn behaviour, observing line-following corrections, and monitoring live sensor and decision output from the terminal.

## Engineering focus

The project demonstrates the progression from low-level hardware commands to reusable abstractions such as `forward()`, `turn_left()`, `turn_right()`, and `stop()`.

It also introduces practical control-system ideas including filtering, thresholds, dead zones, proportional correction, recovery logic, and the importance of testing one calibration parameter at a time.

## Academic context

This project is connected to practical robotics study following the **Constructor University and Constructor Talent School Summer Camp 2026** in Bremen, Germany, where the academic focus included **Mathematics & Modeling** and **Neural Networks & Robotics**.
