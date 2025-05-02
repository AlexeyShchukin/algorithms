"""Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it can trap after raining."""


class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res
