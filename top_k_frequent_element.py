"""Leetcode 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order."""
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [num for num, count in Counter(nums).most_common()[:k]]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
