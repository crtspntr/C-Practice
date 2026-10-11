# C++Practice — Coding Teacher Starter

## Goal
A small C++ project you practice in VS Code while an open-model "teacher"
(Gemma 4 via Ollama, or `glm-4.7:cloud`/`minimax-m2.1:cloud`) creates GitHub
issues, grades your pull requests, and answers questions.

## Local Q&A (fast, offline)
- Install Ollama and pull `gemma4:e2b` (or `qwen3:8b`).
- Point the VS Code Ollama extension at `http://localhost:11434`.

## Teacher (cloud / heavier reasoning)
- Sign in to Ollama (`ollama signin`) and run `gemma4:cloud`.
- The teacher can create issues, post hints, and grade PRs using the chat or
  `gh`-based scripts below.

## Build / test locally
```
cmake -S . -B build -G "MinGW Makefiles" -DCMAKE_CXX_COMPILER=g++
cmake --build build
ctest --test-dir build
```

## Assignments
See `assignments/` for tasks. Each assignment has a starter file, tests, and a
short "what to do" note. Work on a branch, open a PR to `main`, then grade it
with `python scripts/grade.py <assignment_id> <pr_number>`.

## Grading (using GitHub CLI)
```
# Example: grade assignment 1 PR #5
python scripts/grade.py assignment1 5
```
The grader checks that `ctest` passes and posts a short review comment.
