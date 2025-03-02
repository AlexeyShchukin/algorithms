"""Дан отсортированный массив и число. Вернуть индексы двух чисел из массива,
сумма которых максимально приближена к заданному числу."""


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    res = []
    while left < right:
        sum_nums = nums[left] + nums[right]

        if target - sum_nums < sum(res):
            res = [left, right]

        if sum_nums < target:
            left += 1
        elif sum_nums > target:
            right -= 1
        else:
            return res
    return res


print(two_sum(nums=[-10, -5, 2, 2, 11, 13, 15], target=9))
