class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for ch in s:
            if ch.isalnum():
                arr.append(ch.lower())
        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True        