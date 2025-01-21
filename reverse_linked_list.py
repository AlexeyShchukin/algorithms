# Leetcode 206. Reverse Linked List

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the head of a singly linked list, reverse the list, and return the reversed list."""
        next_node = None
        while head:
            new_head = head.next
            head.next = next_node
            node = head
            head = new_head
        return next_node
