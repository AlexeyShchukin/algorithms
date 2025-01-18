# Leetcode 268. Missing number
from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        """Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array."""
        expected_len = len(nums) + 1
        return sum(range(expected_len)) - sum(nums)
