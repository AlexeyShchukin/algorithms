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
        # создаем три указателя предыдущий (None), текущий (head) и следующий элемент (None)
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next  # запоминаем следующий элемент

            curr.next = prev  # разворачиваем стрелку в обратную сторону
            prev = curr  # смещаем указатели вправо
            curr = next_node

        return prev  # если curr указывает уже на пустой элемент, вернем последний prev