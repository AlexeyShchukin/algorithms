from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    prefix = 1  # the product of all elements of the array that are to the left of the current element
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1  # the product of all elements of the array that are to the right of the current element
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
