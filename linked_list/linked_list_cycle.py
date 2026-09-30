"""141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false."""


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current = head
        while current:
            if current in visited_nodes:
                return True
            else:
                visited_nodes.add(current)
                current = current.next
        return False


class Solution:
    def has_cycle2(self, head: Optional[ListNode]) -> bool:
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False