# utils.py

from constant import START_X, GAP, TUBE_WIDTH

def get_tube_from_x(x):
    """
    Returns the tube index based on the X coordinate.
    Returns None if the finger is not over any tube.
    """

    for i in range(4):

        left = START_X + (i * GAP)
        right = left + TUBE_WIDTH

        if left <= x <= right:
            return i

    return None


def inside_tube(x, y):
    """
    Check whether the finger is inside the tube area.
    """

    if y < 180 or y > 500:
        return False

    return True