"""Дан отсортированный массив и число. Вернуть массив из двух чисел в заданном массиве,
сумма которых максимально приближена к заданному числу."""


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    res = [nums[left], nums[right]]

    while left < right:
        sum_nums = nums[left] + nums[right]

        if abs(target - sum_nums) < abs(target - sum(res)):
            res = [nums[left], nums[right]]

        if sum_nums < target:
            left += 1
        elif sum_nums > target:
            right -= 1
        else:
            return res
    return res


print(two_sum(nums=[-10, -5, -2, 2, 2, 11, 13, 15], target=9))
