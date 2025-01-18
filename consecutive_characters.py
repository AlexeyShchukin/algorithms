# Leetcode 1446. Consecutive Characters

class Solution:
    """The power of the string is the maximum length of a non-empty substring
    that contains only one unique character.
    Given a string s, return the power of s."""

    def max_power(self, s: str) -> int:
        res = 1
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            res = max(res, count)

        return res


if __name__ == '__main__':
    s = "leetcode"
    print(Solution().max_power(s))

    s = "abbcccddddeeeeedcba"
    print(Solution().max_power(s))

    s = "cc"
    print(Solution().max_power(s))
