from puzzle.solver import Solver

def main():
    """
    Challenge state
    """
    #initial_state = [2, 8, 3, 1, 6, 4, 7, "B", 5]

    """
    Greater Challenge state
    """
    initial_state = [5, 1, 4, 7, "B", 6, 3, 8, 2]

    
    goal_state = [1, 2, 3, 8, "B", 4, 7, 6, 5]

    """
    Modify the solver based on the algorithms you want to run

    Uninformed Search:
    algorithm parameter: dfs | bfs

    Informed Search:
    algorithm parameter: astar | gbfs
    heuristic: hamming | manhattan | inversion | nilsson
    """
    #solver = Solver(initial_state, goal_state, 'bfs')
    solver = Solver(initial_state, goal_state, 'astar', 'nilsson')
    solver.solve()

if __name__ == '__main__':
    main()