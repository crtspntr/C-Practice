# Assignment 1: clamp & fibonacci

## Task
Implement/modify:

- `fibonacci(int n)` for `n >= 0`
- `clamp_value(value, low, high)` so that value is constrained into `[low, high]`

## Requirements
- All CTest tests pass.
- Code compiles cleanly (`-Wall -Wextra -Wpedantic`).
- Explain what improved and any edge cases.

## Local workflow
1. Create a branch: `git checkout -b feature/assignment1`
2. Edit `src/calc.cpp`.
3. Run tests: `ctest --test-dir build`
4. Push branch and open a PR:
   ```
   git push origin feature/assignment1
   gh pr create --title "Assignment 1" --body "..."
   ```
5. Grade locally: `python scripts/grade.py assignment1 <pr_number>`
