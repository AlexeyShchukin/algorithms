# 200. Number of Islands

# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def num_islands(grid: list[list[str]]) -> int:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ROWS = len(grid)
    COLS = len(grid[0])
    islands = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
            return

        grid[r][c] = "0"
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                islands += 1

    return islands


print(num_islands(grid))
