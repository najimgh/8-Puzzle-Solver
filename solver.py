from importlib.resources import path
from state import State
from dfs import DFS
import math
import time

class Solver(object):

    def __init__(self, initial_state, goal, algorithm='bfs', heuristic= None):
        self.initial_state = initial_state
        SIZE = 3
        self.state = State(initial_state, SIZE, goal)

        # if(algorithm == 'bfs'): 
        #     self.search_alg = BFS

        if(algorithm == 'dfs'):
            self.search_alg = DFS

        # if(algorithm == 'ast'):
        #     self.search_alg = A_STAR


    def output(self, result, r_time):
        final_state, nodes_explored, max_search_depth = result
        path_cost = final_state.cost
        parent_state = final_state.parent
        search_depth = 0

        while parent_state:
            if parent_state.parent:
                search_depth += 1
            parent_state = parent_state.parent

        print("\n" + "------ Results ------")
        print("path_cost:", str(path_cost) + "\n")
        print("nodes_explored:", str(nodes_explored) + "\n")
        print("search_depth:", str(search_depth) + "\n")
        print("max_search_depth:", str(max_search_depth) + "\n")
        print("running time:", str(r_time) + "\n")

    def solve(self):
        start_time = time.time()
        results = self.search_alg(self.state)
        end_time = time.time()
        r_time = end_time - start_time
        self.output(results, r_time)

    
