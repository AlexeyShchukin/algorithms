"""
110. Balanced Binary Tree

Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and
right subtrees of every node differ in height by no more than 1.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            height_left = dfs(node.left)
            height_right = dfs(node.right)

            balanced = height_left[0] and height_right[0] and abs(height_left[1] - height_right[1]) <= 1

            return [balanced, 1 + max(height_left[1], height_right[1])]

        return dfs(root)[0]
