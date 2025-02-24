# Leetcode 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        hashmap = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if char != hashmap[stack.pop()]:
                        return False
        return not stack
