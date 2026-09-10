# Project Media

This folder contains visual evidence of the robot being tested on a physical indoor course.

## Robot course test 01

**Video:** [`robot-course-test-01.mp4`](../assets/videos/robot-course-test-01.mp4)

This recording shows the Raspberry Pi–based tracked robot operating on a marked floor course during physical testing. It demonstrates the transition from code-level movement logic to real-world robot behaviour, where motor speed, turn duration, wheel traction, and floor surface all affect the resulting path.

The test is useful for validating:
- forward movement;
- turn calibration;
- track balance;
- course-following behaviour;
- the gap between ideal program logic and physical motion.

## Robot course test 02

**Video:** [`robot-course-test-02.mp4`](../assets/videos/robot-course-test-02.mp4)

This recording shows another physical run of the robot and complements the first test by providing additional evidence of real-world calibration and debugging.

The project was developed iteratively: movement parameters were adjusted after observing the robot on the floor rather than assuming that theoretical timing values would produce exact turns.

## Why these videos matter

The videos document an important robotics engineering principle: the same control code can behave differently on real hardware because of battery voltage, motor tolerances, surface friction, wheel slip, and sensor behaviour.

They therefore form part of the project evidence, not just a demonstration.
