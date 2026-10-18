# C++Practice — Coding Teacher Roadmap

## The Interleaved Learning Plan
Instead of linear chapters, we use a "cognitive loop":
**Prime (Upcoming)** $\rightarrow$ **Review (Past)** $\rightarrow$ **Core (Current Focus)**.

### Assignment Schedule
| Assignment | Core Focus (Topic X) | Review Topics (A, B, C) | Prime (Look-ahead) |
| :--- | :--- | :--- | :--- |
| **1** | Basic Booleans | Data Types, I/O | If...Else |
| **2** | If...Else / Nested If | Booleans, Operators | Switch Statement |
| **3** | Switch Statement | If...Else, Data Types | While Loops |
| **4** | While Loops | Switch, Booleans | For Loops |
| **5** | For Loops | While Loops, Operators | Break/Continue |
| **6** | Break / Continue | For/While Loops, If...Else | Arrays |
| **7** | Arrays (1D) | For Loops, Data Types | Structures/Enums |
| **8** | Structures & Enums | Arrays, Basic Types | References/Pointers |

## Assignment Structure
Each assignment folder (`assignments/assignmentN`) contains:
- `README.md`: The "Prime" context, the "Review" requirements, and the "Core" task.
- `starter.cpp`: A skeletal implementation with `TODO` markers.
- `tests/` (integrated in `tests/calc_test.cpp`): GoogleTest cases.

## Grading Logic (`scripts/grade.py`)
- **Automated**: Checks if `ctest` passes.
- **Manual/AI**: The teacher (gemma4:cloud) reviews the PR for architectural elegance, efficiency, and adherence to W3Schools standards.
