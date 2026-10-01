"""
703. Kth Largest Element in a Stream

You are part of a university admissions office and need to keep track of the kth highest test score
from applicants in real-time. This helps to determine cut-off marks for interviews and admissions
dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores
and continuously returns the kth highest test score after a new score has been submitted. More specifically,
we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth
largest element in the pool of test scores so far.
"""


import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(3)
param_2 = obj.add(5)
param_3 = obj.add(10)
param_4 = obj.add(9)
param_5 = obj.add(4)
print(param_1, param_2, param_3, param_4, param_5)
