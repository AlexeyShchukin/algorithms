# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]


def max_area_of_island(grid: list[list[int]]) -> int:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ROWS = len(grid)
    COLS = len(grid[0])
    max_area = 0
    area = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
            return

        nonlocal area
        area += 1
        grid[r][c] = 0
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                dfs(r, c)
                max_area = max(max_area, area)
                area = 0

    return max_area


print(max_area_of_island(grid))
