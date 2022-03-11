from collections import deque

def DFS(initial_state):
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
        state.display_state()
        closed.add(tuple(state.currentState))
        #print("Closed List:", closed)
        if state.is_goal():
            return (state, nodes_explored, max_search_depth)

        nodes_explored = nodes_explored + 1

        for child in state.expand(True):
            # print("This is the child", child.currentState)
            if tuple(child.currentState) not in closed and tuple(child.currentState) not in open_state:
                open.append(child)
                open_state.append(tuple(child.currentState))
                if child.cost > max_search_depth:
                    max_search_depth = child.cost

    return None
