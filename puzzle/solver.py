from importlib.resources import path
from puzzle.state import State
from algorithms.dfs import DFS
from algorithms.bfs import BFS
from algorithms.gbfs import GBFS
from algorithms.a_star import A_STAR
from heuristics.hamming import hamming_distance
from heuristics.inversion import perm_inversion
from heuristics.manhattan import manhattan_distance
from heuristics.nilsson import nilsson_sequence
import time

class Solver(object):
    """
    The Solver ckass is used to instatiate the object with the desired initial state, goal state, search algorithm and the heuristic (if applicable).
    The Solver calculates the appropriate cost of a state and gives an output with different information when the 8-Puzzle is solved.
    """

    def __init__(self, initial_state, goal, algorithm='bfs', heuristic= None):
        self.heuristic = heuristic
        self.algorithm = algorithm
        self.initial_state = initial_state
        SIZE = 3
        """
        When a heuristic is not defined, do not define the cost function
        """
        if(heuristic is None):
            self.state = State(initial_state, SIZE, goal)
        else:
            self.state = State(initial_state, SIZE, goal, self.total_cost)

        """
        Set the search algorithm function and heuristic function (if applicable)
        """
        if(algorithm == 'bfs'): 
            self.search_alg = BFS

        if(algorithm == 'dfs'):
            self.search_alg = DFS

        if(algorithm == 'astar'):
            self.search_alg = A_STAR
        
        if(algorithm == 'gbfs'):
            self.search_alg = GBFS

        if(algorithm == 'gbfs' or algorithm == 'astar'):
            if(heuristic == 'hamming'):
                self.distance = hamming_distance
            elif(heuristic == 'manhattan'):
                self.distance = manhattan_distance
            elif(heuristic == 'inversion'):
                self.distance = perm_inversion
            elif(heuristic == 'nilsson'):
                self.distance = nilsson_sequence
            elif(heuristic == None):
                raise Exception("A heuristic needs to be defined when using the A* search algorithm")

    def total_cost(self, state):
        """
        Calculate the total cost of a state using f(n) = g(n) + h(n).
        If using GBFS as the search algorithm, calculate only the heuristic cost h(n).
        """
        sum_h = 0
        if(self.heuristic == 'nilsson'):
             # h(n) comes from the Nilsson Sequence heuristic
            sum_h += self.distance(state)
        elif(self.heuristic == 'inversion'):
            # h(n) comes from the Permutation Inversion heuristic
            sum_h = self.distance(state.currentState)
        else:
            for i, value in enumerate(state.currentState):
                # Skip cost calculation for the empty tile
                if(value == "B"):
                    continue
                # Position of current value
                current_row = i // state.size
                current_col = i % state.size
                # Position of goal value
                goal_value_index = state.goal.index(value)
                goal_row = goal_value_index // state.size
                goal_col = goal_value_index % state.size
        
                # h(n) comes from either the hamming distance heuristic or the manhattan distance heuristic
                sum_h += self.distance(current_row,current_col,goal_row,goal_col)
        # Return only the heuristic cost if the algorithm is GBFS 
        if(self.algorithm == 'gbfs'):
            return sum_h
        sum_g = state.cost
        total_cost = sum_g + sum_h
        return total_cost

    def output(self, result, r_time):
        """
        Prints to the console with information about the results obtained
        depending the on the search algorithm and/or the heuristic used to solve the 8=Puzzle.
        """
        # Results from the search algorithm
        final_state, nodes_explored, max_search_depth = result
        # The cost of the path to the goal state or g(n)
        path_cost = final_state.cost
        # The actions taken to arrive to the goal state
        action_path = [final_state.operator]
        # The states generated to arrive at the goal state
        state_path_to_goal = [final_state]
        # The parent state
        parent_state = final_state.parent
        search_depth = 0

        # Calculate the search path to the goal state
        # Find the actions taken to arrive at the goal state
        # Find the states generated to arrive at the goal state
        while parent_state:
            search_depth += 1
            action_path.append(parent_state.operator)
            state_path_to_goal.append(parent_state)
            parent_state = parent_state.parent
        action_path.reverse()
        state_path_to_goal.reverse()

        print("\n" + "------ Results ------" + "\n")

        print("action_path:", str(action_path) + "\n")
        print("State Path to Goal:" + "\n")
        for state in state_path_to_goal:
            state.display_state()
        print("\n")
        print("path_cost:", str(path_cost) + "\n")
        print("nodes_explored:", str(nodes_explored) + "\n")
        print("search_depth:", str(search_depth) + "\n")
        print("max_search_depth:", str(max_search_depth) + "\n")
        print("running time:", str(r_time) + "\n")

    def solve(self):
        """
        Function used to start solving the puzzle
        """
        start_time = time.time()

        if(self.search_alg == A_STAR or self.search_alg == GBFS):
            results = self.search_alg(self.state, self.total_cost)
        else:
            results = self.search_alg(self.state)

        end_time = time.time()
        r_time = end_time - start_time
        self.output(results, r_time)

    
