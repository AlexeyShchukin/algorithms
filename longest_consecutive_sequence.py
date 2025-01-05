from typing import List


def longest_consecutive(nums: List[int]) -> int:
    my_set = set(nums)
    res = 0
    for num in my_set:
        if num - 1 not in my_set:
            length = 1
            while num + length in my_set:
                length += 1
            res = max(res, length)
    return res


if __name__ == '__main__':
    print(longest_consecutive([3, 3, 2, 5, 7, 8, 1, 9, 20, 11, 10]))
