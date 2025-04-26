"""Leetcode 125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""
from string import punctuation

class Solution:
    def is_palindrome(self, s: str) -> bool:
        chars = punctuation
        for char in chars:
            if char in s:
                s = s.replace(char,"")
        s = s.replace(" ","")
        s = s.lower()
        return s == s[::-1]


# class Solution:
#     def is_palindrome(self, s: str) -> bool:
#         chars = [c for c in s.lower() if c.isalnum()]
#         return chars == chars[::-1]