class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])

        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
        ans = ""

        for i in range(min_len):

            char = strs[0][i]

            for word in strs:
                if word[i] != char:
                    return ans

            ans += char

        return ans