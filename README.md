# 8-Puzzle-Solver
8 puzzle solver using informed and uninformed searches.

- Uninformed Searches: 
  - BFS
  - DFS
- Informed Searches:
  - Best-First
  - A-star algorithm

The informed searches can use any of the following heuristics:
- Hamming Distance
- Manhattan Distance
- Permutaion Inversion
- Nilsson Sequence **(inadmissible heuristic)**

# Results

#### Note the goal state is of the form (1 2 3 8 B 4 7 6 5)

### Input: (2 8 3 1 6 4 7 B 5)

**A-Star algorithm**
Heuristic | Path Cost | States Expanded | Search Depth | Max Search Depth | Running Time (average ms)
--- | --- | --- | --- |--- |---
Hamming Distance | 5 | 1581 | 5 | 14 | 0.192
Manhattan Distance | 5 | 5 | 5 | 5 | 0.0
Permutation Inversion | 5 | 6 | 5 | 5 | 0.0
Nilsson Sequence | 5 | 7 | 5 | 5 | 0.0

**Best-First algorithm**
Heuristic | Path Cost | States Expanded | Search Depth | Max Search Depth | Running Time (average ms)
--- | --- | --- | --- |--- |---
Hamming Distance | 363 | 181438 | 363 | 637 | 955.81
Manhattan Distance | 5 | 5 | 5 | 5 | 0.002
Permutation Inversion | 5 | 5 | 5 | 5 | 0.0
Nilsson Sequence | 5 | 6 | 5 | 5 | 0.008

### Input: (5 1 4 7 B 6 3 8 2)

**A-Star algorithm**
Heuristic | Path Cost | States Expanded | Search Depth | Max Search Depth | Running Time (average ms)
--- | --- | --- | --- |--- |---
Hamming Distance | 20 | 173186 | 20 | 29 | 850
Manhattan Distance | 22 | 293 | 22 | 22 | 0.018
Permutation Inversion | 20 | 122 | 20 | 20 | 0.016
Nilsson Sequence | 22 | 1277 | 22 | 22 | 0.22

**Best-First algorithm**
Heuristic | Path Cost | States Expanded | Search Depth | Max Search Depth | Running Time (average ms)
--- | --- | --- | --- |--- |---
Hamming Distance | 464 | 181438 | 464 | 600 | 1050
Manhattan Distance | 92 | 434 | 92 | 94 | 0.04
Permutation Inversion | 72 | 524 | 72 | 82 | 0.09
Nilsson Sequence | 84 | 354 | 84 | 84 | 0.035
