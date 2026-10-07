"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left,
or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
import heapq


def minimum_effort_path(heights: list[list[int]]) -> int:
    rows = len(heights)
    cols = len(heights[0])

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    heap = [(0, 0, 0)]
    visited = set()
    max_effort = 0

    while heap:
        effort, row, col = heapq.heappop(heap)
        max_effort = max(max_effort, effort)

        if row == rows - 1 and col == cols - 1:
            return max_effort

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for r, c in directions:
            neighbor_row = row + r
            neighbor_col = col + c

            if not 0 <= neighbor_row < rows or not 0 <= neighbor_col < cols:
                continue

            heapq.heappush(
                heap,
                (
                    abs(heights[neighbor_row][neighbor_col] - heights[row][col]),
                    neighbor_row,
                    neighbor_col
                )
            )


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(minimum_effort_path(heights))
