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