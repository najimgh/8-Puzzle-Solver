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