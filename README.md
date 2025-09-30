[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/dBMhcRtR)
# HW2 — Theme Park Gate (Two Queues, Service Ratio)

## Story
A theme park has two lines at a ride: **FastPass** and **Regular**. For fairness and speed, the operator serves 1 FastPass rider, then 3 Regular riders, repeating that cycle all day.

## Task (Technical)
Implement a gate controller:
- Two queues: `fastpass` and `regular`.
- `arrive(line, person_id)` enqueues to the chosen line.
- `serve() -> person_id` pops the next rider according to the repeating ratio **[F, R, R, R]**.
- If a line in the current slot is empty, **skip** to the next slot.
- `peek_next_line() -> str` returns `"fastpass"` or `"regular"` based on the upcoming slot (after any necessary skips).

## Hints
1) Keep a pointer `i` cycling through `[0,1,2,3]` for the pattern.
2) On each serve, attempt the current line; if empty, advance until you find a non-empty or you’ve checked all four.
3) Use `collections.deque` for O(1) ends.

## Run tests locally
```bash
python -m pytest -q
```
## Submit
Push to GitHub Classroom

Commit → push → check Actions.

## Common problems
- Forgetting to advance the cycle when the chosen line is empty.

- Serving 4 regulars when FastPass is empty (you should still cycle).