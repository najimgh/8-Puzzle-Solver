from importlib.resources import path
from state import State
from dfs import DFS
from bfs import BFS
from a_star import A_STAR
from heuristics import hamming_distance, manhattan_distance
import math
import time

class Solver(object):

    def __init__(self, initial_state, goal, algorithm='bfs', heuristic= None):
        self.initial_state = initial_state
        SIZE = 3
        """
        When the heuristic is not defined, do not define the cost function
        """
        if(heuristic is None):
            self.state = State(initial_state, SIZE, goal)
        else:
            self.state = State(initial_state, SIZE, goal, self.total_cost)

        """
        Set the algorithm variable and heuristic function if it is applicable
        """
        if(algorithm == 'bfs'): 
            self.search_alg = BFS

        if(algorithm == 'dfs'):
            self.search_alg = DFS

        if(algorithm == 'astar'):
            self.search_alg = A_STAR

            if(heuristic == 'hamming'):
                self.distance = hamming_distance
            elif(heuristic == 'manhattan'):
                self.distance = manhattan_distance
            elif(heuristic == None):
                raise Exception("A heuristic needs to be defined when using the A* search algorithm")

    def total_cost(self, state):
        """
        Calculate the total cost of a state using f(n) = g(n) + h(n)
        """
        sum_h = 0
        for i, value in enumerate(state.currentState):
            # Skip cost calculation for the empty tile
            if(value == "B"):
                continue
            # Position of current value
            current_row = i // state.size
            current_col = i % state.size
            # Position of goal  value
            goal_value_index = state.goal.index(value)
            goal_row = goal_value_index // state.size
            goal_col = goal_value_index % state.size

            sum_h += self.distance(current_row,current_col,goal_row,goal_col)
        sum_g = state.cost
        total_cost = sum_g + sum_h
        return total_cost

    def output(self, result, r_time):
        final_state, nodes_explored, max_search_depth = result
        path_cost = final_state.cost
        action_path = [final_state.operator]
        state_path_to_goal = [final_state]
        parent_state = final_state.parent
        search_depth = 0

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
        start_time = time.time()

        if(self.search_alg == A_STAR):
            results = self.search_alg(self.state, self.total_cost)
        else:
            results = self.search_alg(self.state)

        end_time = time.time()
        r_time = end_time - start_time
        self.output(results, r_time)

    
