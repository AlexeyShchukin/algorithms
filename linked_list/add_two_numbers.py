"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode()
        rest = 0
        while l1 or l2 or rest:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            node_sum = val1 + val2 + rest

            rest = node_sum // 10
            node_sum %= 10

            res.next = ListNode(node_sum)
            res = res.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
