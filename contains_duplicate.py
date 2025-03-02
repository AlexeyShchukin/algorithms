# Leetcode 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        temp = set()
        for num in nums:
            if num in temp:
                return True
            temp.add(num)
        return False


    def contains_duplicate2(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        return len(nums) != len(nums_set)