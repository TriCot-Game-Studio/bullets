def map_range(x, min_1, max_1, min_2, max_2):
    new_range = (x - min_1) / (max_1 - min_1)
    new_range *= max_2 - min_2
    new_range += min_2

    return new_range
