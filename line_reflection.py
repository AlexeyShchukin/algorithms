# LeetCode 356. Line Reflection

def is_reflected(points) -> bool:
    min_x, max_x = float('inf'), float('-inf')  # infinity
    points_set = set()

    for x, y in points:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        points_set.add((x, y))

    s = (min_x + max_x) / 2  # symetry line

    for x, y in points_set:
        if (s * 2 - x, y) not in points_set:  # check for reflection for each point
            return False
        return True


if __name__ == '__main__':
    print(is_reflected([(1, 1), (3, 1), (2, 2)]))
