"""Leetcode 49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order."""
from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)
        return list(hashmap.values())
