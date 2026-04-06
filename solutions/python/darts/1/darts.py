import math


def score(x, y):
    # Use pythag to calculate the distance from center
    distance_from_center = math.sqrt((x**2 + y**2))

    # Compare that distance to the limits to determine the circle
    if distance_from_center <= 1:
        return 10
    elif distance_from_center <= 5 and distance_from_center > 1:
        return 5
    elif distance_from_center <= 10 and distance_from_center > 5:
        return 1
    else:
        return 0
