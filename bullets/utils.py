import math


def map_range(x, min_1, max_1, min_2, max_2):
    new_range = (x - min_1) / (max_1 - min_1)
    new_range *= max_2 - min_2
    new_range += min_2

    return new_range


def rotate(x, y, theta):
    new_x = x * math.cos(theta) + x * math.sin(theta)
    new_y = y * -math.sin(theta) + y * math.cos(theta)
    return new_x, new_y
