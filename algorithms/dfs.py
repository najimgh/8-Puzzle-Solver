from collections import deque

def DFS(initial_state):
    # Open list is a deque which essentially behaves like a stack
    open = deque()
    open.append(initial_state)
    # Used to check if the state is not already in the open list.
    # This is for cases where the search makes a move that backtracks to the parent state
    open_state = []
    open_state.append(tuple(initial_state.currentState))
    closed = set()
    nodes_explored = 0
    max_search_depth = 0

    while open:
        state = open.pop()
        closed.add(tuple(state.currentState))
        # Check if state is the goal state
        if state.is_goal():
            return (state, nodes_explored, max_search_depth)

        nodes_explored = nodes_explored + 1

        # Iterate over the children of the state
        for child in state.expand():
            # If the child is not in the closed list or already in the open list
            if tuple(child.currentState) not in closed and tuple(child.currentState) not in open_state:
                open.append(child)
                open_state.append(tuple(child.currentState))
                if child.cost > max_search_depth:
                    max_search_depth = child.cost

    return None
