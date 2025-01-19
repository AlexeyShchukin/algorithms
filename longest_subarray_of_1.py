# Leetcode 1493. Longest Subarray of 1's After Deleting One Element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """Given a binary array nums, you should delete one element from it.
        Return the size of the longest non-empty subarray containing only 1's in the resulting array.
        Return 0 if there is no such subarray."""
        longest = 0
        prev = 0
        curr = 0
        for num in nums:
            if num:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))


print(Solution().longestSubarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1]))
