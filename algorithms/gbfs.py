from util.priority_queue import PriorityQueue

def GBFS(initial_state, heuristic_cost):
    """
    Greedy Best-First search algorithm.
    Using the heuristic cost to calculate the priority
    """
    # Using PriorityQueue defined in priority_queue.py
    open = PriorityQueue()
    open.put(initial_state, heuristic_cost(initial_state))
    # Used to check if the state is not already in the open list.
    # This is for cases where the search makes a move that backtracks to the parent state
    open_state = []
    open_state.append(tuple(initial_state.currentState))
    closed = set()
    nodes_explored = 0
    max_search_depth = 0

    while not open.is_empty():
        state = open.get()
        closed.add(state)
        # Check if state is the goal state
        if state.is_goal():
            return (state, nodes_explored, max_search_depth)

        nodes_explored = nodes_explored + 1

        # Iterate over the children of the state
        for child in state.expand():
            # If the child is not in the closed list or already in the open list
            if child not in closed and tuple(child.currentState) not in open_state:
                open.put(child, heuristic_cost(child))
                open_state.append(tuple(child.currentState))
                if child.cost > max_search_depth:
                    max_search_depth = child.cost
    
    return None