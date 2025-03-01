"""Leetcode 1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order."""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # {value: index}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[v] = i
