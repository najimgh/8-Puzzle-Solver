import math

def hamming_distance(x1, y1, x2, y2):
    """
    Distance is equal to 1 for a specific tile if its is out of place
    (i.e add +1)
    """
    distance = 0
    same_row = False
    same_column = False
    if(x1 == x2): same_row = True
    if(y1 == y2): same_column = True

    if(same_row and same_column):
        distance = 1
    return distance

def manhattan_distance(x1, y1, x2, y2):
    """
    The sum of the difference between x1, x2 and y1, y2
    """
    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)

    return distance_x + distance_y

def perm_inversion(currentState):
    """
    Since the Goal state is not a list of numbers in ascening order, we cannot simply compare which is greater than the other.
    For each specific value, we need to check what values on the right side of it are wrong.
    """
    inversion_count = 0
    for i in range(len(currentState)):
        for j in range(i + 1, len(currentState)):
            if (currentState[i] != 'B' and currentState[j] != 'B'):
                if(currentState[i] == 2 and currentState[j] == 1):
                    inversion_count += 1
                if(currentState[i] == 3 and (currentState[j] == 1 or currentState[j] == 2)):
                    inversion_count += 1
                if(currentState[i] == 4 and (currentState[j] == 1 or currentState[j] == 2 or currentState[j] == 3 or currentState[j] == 8)):
                    inversion_count += 1
                if(currentState[i] == 5 and (currentState[j] == 1 or currentState[j] == 2 or currentState[j] == 3 or currentState[j] == 8 or currentState[j] == 4 or currentState[j] == 7 or currentState[j] == 6)):
                    inversion_count += 1
                if(currentState[i] == 6 and (currentState[j] == 1 or currentState[j] == 2 or currentState[j] == 3 or currentState[j] == 8 or currentState[j] == 4 or currentState[j] == 7)):
                    inversion_count += 1
                if(currentState[i] == 7 and (currentState[j] == 1 or currentState[j] == 2 or currentState[j] == 3 or currentState[j] == 8 or currentState[j] == 4)):
                    inversion_count += 1
                if(currentState[i] == 8 and (currentState[j] == 1 or currentState[j] == 2 or currentState[j] == 3)):
                    inversion_count += 1
    return inversion_count

def nilsson_sequence(state):
    """
    The inadmissible heuristic.
    The Nilsson Sequence heurisitic is of the form h(n) = P(n) + 3*S(n)
    where P(n) is the manhattan distance of each tile from its proper position
    and S(n) is a sequence score obtained by checking around the noncentral squares in turn.
    We give a score of 2 for every tile not followed by its proper successor and 0 for every other tile.
    Except that a tile at the center that is not the empty tile is given a score of 1.
    """
    # Each value from currentState is given a specific index
    # based on their position in the 8-puzzle
    square_numbers = {}

    square_numbers[state.currentState[0]] = 0
    square_numbers[state.currentState[1]] = 1
    square_numbers[state.currentState[2]] = 2
    square_numbers[state.currentState[3]] = 7
    square_numbers[state.currentState[4]] = 8
    square_numbers[state.currentState[5]] = 3
    square_numbers[state.currentState[6]] = 6
    square_numbers[state.currentState[7]] = 5
    square_numbers[state.currentState[8]] = 4

    # The goal state with each value having a specific position
    goal_numbers = {}
    for i in range(1,9):
        goal_numbers[i] = i -1
    goal_numbers['B'] = 8

    sum_p = 0
    sum_s = 0
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

        sum_p += manhattan_distance(current_row,current_col,goal_row,goal_col)

        # When tile is in the center, add score 3*1
        # When tile not in center, add score 3*2
        if(square_numbers[value] == 8):
            sum_s += 3*1
        elif(square_numbers[next_val(state.currentState, square_numbers, value)] != (goal_numbers[value] + 1)):
            sum_s = 3*2

    print("Nilsson Sequence sum:", sum_p + sum_s)
    return sum_p + sum_s


def next_val(currentState, square_numbers, value):
    """
    Gets the next value in the currentState using a clockwise navigation.
    """
    next_num = 0
    currentNumber = square_numbers[value]
    if(currentNumber >= 0 and currentNumber < 2):
        next_num = currentNumber + 1
    elif(currentNumber == 2):
        next_num = 5
    elif(currentNumber == 3):
        next_num = 8
    elif(currentNumber == 4):
        next_num = 7
    elif(currentNumber == 5):
        next_num = 6
    elif(currentNumber == 6):
        next_num = 3
    else:
        next_num = 0

    return currentState[next_num]


