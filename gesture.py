import math

class Gesture:

    def __init__(self):
        pass

    def pinch(self, points):

        if points is None:
            return False

        if len(points) < 9:
            return False

        thumb = points[4]
        index = points[8]

        distance = math.sqrt(
            (thumb[1] - index[1]) ** 2 +
            (thumb[2] - index[2]) ** 2
        )

        return distance < 40