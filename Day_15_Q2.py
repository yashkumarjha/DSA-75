# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d_set = set()
        result = 0

        for r in range(len(s)):
            while(s[r] in d_set):
                d_set.remove(s[left])
                left = left+1
            d_set.add(s[r])
            result = max(result, r-left+1)
        return result
