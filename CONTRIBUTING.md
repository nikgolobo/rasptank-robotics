# Contributing

## Development rules

1. Keep each hardware exercise in its existing topic folder.
2. Do not change GPIO or motor mappings without documenting the hardware reason.
3. Test motor-control changes with the robot lifted off the floor first.
4. Keep functions small and descriptive (`forward()`, `turn_left()`, `get_distance()`, etc.).
5. When tuning physical behavior, change one parameter at a time and document the value tested.

## Pull requests

A pull request should describe:

- what changed;
- which script was changed;
- which hardware configuration was used;
- how the change was tested;
- any calibration values that were modified.
