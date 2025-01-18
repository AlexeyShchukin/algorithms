# 414. Third Maximum Number

# # O(n) time complexity
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Given an integer array nums, return the third distinct maximum number in this array.
        If the third maximum does not exist, return the maximum number."""
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        else:
            first_max = float('-inf')
            second_max = float('-inf')
            third_max = float('-inf')
            for num in set_nums:
                if num > first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = num
                elif num > second_max:
                    third_max = second_max
                    second_max = num
                elif num > third_max:
                    third_max = num
            return third_max

    # O(nlogn) time complexity
    # def thirdMax(self, nums: List[int]) -> int:
    #     set_nums = set(nums)
    #     if len(set_nums) < 3:
    #         return max(set_nums)
    #     return sorted(set_nums)[-3]