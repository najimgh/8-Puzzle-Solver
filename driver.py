from solver import Solver

def main():
    initial_state = [2, 8, 3, 1, 6, 4, 7, "B", 5]
    goal_state = [1, 2, 3, 8, "B", 4, 7, 6, 5]

    # Modify the solver based on the algorithms you want to run
    solver = Solver(initial_state, goal_state, 'dfs')
    # solver = Solver(initial_state, goal_state, 'astar', 'manhattan')
    solver.solve()

if __name__ == '__main__':
    main()