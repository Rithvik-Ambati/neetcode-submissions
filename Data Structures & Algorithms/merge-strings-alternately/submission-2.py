class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        n = len(word1)
        m = len(word2)
        combi = ""
        if m > n:
            for i in range (n):
                combi += word1[i]
                combi += word2[i]
            combi += word2[n:]
        else:
            for i in range (m):
                combi += word1[i]
                combi += word2[i]
            combi += word1[m:] 

        return combi