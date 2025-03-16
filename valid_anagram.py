"""Leetcode 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise."""


# from collections import Counter


# def is_anagram(self, s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = set(s)
        for char in hashmap:
            if s.count(char) != t.count(char):
                return False
        return True
