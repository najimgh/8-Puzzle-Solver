def manhattan_distance(x1, y1, x2, y2):
    """
    The sum of the difference between x1, x2 and y1, y2
    """
    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)

    return distance_x + distance_y