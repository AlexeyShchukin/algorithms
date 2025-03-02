# find length of the longest substring of distinct characters

def longest_substring(s: str) -> int:
    hashset = set()
    res, left, right = 0, 0, 0

    while right < len(s):
        char = s[right]
        if char not in hashset:
            hashset.add(char)
            right += 1
            res = max(res, right - left)
        else:
            while char in hashset:
                hashset.remove(s[left])
                left += 1
    return res


print(longest_substring('abcdbfbqwer'))
print(longest_substring('aaaaa'))
print(longest_substring('abacbbaacnfghbxa'))
