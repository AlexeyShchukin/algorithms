"""Leetcode 74. Search a 2D Matrix
You are given an m x n integer matrix `matrix` with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity."""


class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        return False
