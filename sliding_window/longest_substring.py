"""Leetcode 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters."""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        left = 0
        res = 0
        hashmap = {}
        for right, c in enumerate(s):
            if c in hashmap:
                left = max(hashmap[c] + 1, left)
            hashmap[c] = right
            res = max(res, right - left + 1)
        return res
