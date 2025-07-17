# 🧩 8-Tile Puzzle Solver | BFS & A* Search in Python

A Python-based solver for the classic **8-tile sliding puzzle**, supporting both **Breadth-First Search (BFS)** and **A\* Search with heuristic cost**. This project demonstrates algorithmic problem-solving, state modeling, and efficient search techniques for navigating large solution spaces.

---

## 🎯 Objective

The 8-tile puzzle involves sliding numbered tiles on a 3×3 board to achieve a target configuration:

```
Goal State:
1 2 3
8 0 4
7 6 5
```
Where `0` represents the blank space.

---

## 🧠 Key Features

- 🔍 **BFS Solver**: Explores shallowest nodes first for guaranteed shortest path (if solvable).
- 💡 **A* Solver**: Uses Manhattan distance-based cost function (g + h) for optimal pathfinding.
- 🧱 State hashing & duplicate detection to prevent redundant exploration.
- 📈 Tracks:
  - Total number of expanded nodes
  - Total path length (number of moves)
- 📁 Choose puzzles from predefined difficulty levels (very easy → very hard)

---

## 🧩 Search Algorithms

| Algorithm | Strategy | Optimal? | Uses Heuristic |
|-----------|----------|----------|----------------|
| BFS       | Uniform search (queue) | ✅ Yes | ❌ No |
| A* Search | Cost-based (priority queue) | ✅ Yes | ✅ Yes (Misplaced tiles) |

---

## 📂 Project Structure

```
EightTileSolver/
│
├── AStar.py # A* algorithm implementation
├── BFS.py # BFS algorithm implementation
├── Driver.py # CLI entry point for running the solver
├── Helper.py # Utilities: state hash, move generation, printing
├── mode/ # Puzzle input files
│ ├── very_easy.txt
│ ├── easy.txt
│ ├── medium.txt
│ ├── hard.txt
│ └── very_hard.txt
```
