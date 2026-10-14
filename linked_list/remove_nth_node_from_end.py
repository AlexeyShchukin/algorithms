"""
Remove Nth Node From End of List

Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
