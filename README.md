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
- Nilsson Sequence

# Results

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
