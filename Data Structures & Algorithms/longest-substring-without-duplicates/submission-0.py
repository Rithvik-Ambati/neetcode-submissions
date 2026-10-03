class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # if duplicate found, shrink window from left
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # add current character
            window.add(s[right])

            # update max length
            max_len = max(max_len, right - left + 1)
            
        return max_len