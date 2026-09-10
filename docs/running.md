# Running the Scripts

## Activate the environment

```bash
source .venv/bin/activate
```

## Run hardware scripts

Many GPIO and motor scripts may require elevated permissions:

```bash
sudo python3 path/to/script.py
```

## Stop a running script

Use:

```text
Ctrl+C
```

The scripts use `try/finally` or cleanup logic where appropriate so motors and GPIO resources are released when the program exits.

## Recommended test sequence

1. Test LEDs.
2. Test ultrasonic readings.
3. Test motors with the tracks lifted.
4. Test obstacle detection.
5. Test raw line-sensor polarity.
6. Test line following at low speed.
