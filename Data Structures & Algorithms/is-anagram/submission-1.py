class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = {}
        freq2 = {}
        for i in range (len(s)):
            if s[i] not in freq1:
                freq1[s[i]] = 1
            else:
                freq1[s[i]] = freq1[s[i]] + 1
            
            if t[i] not in freq2:
                freq2[t[i]] = 1
            else:
                freq2[t[i]] = freq2[t[i]] + 1
        for letter in freq1.keys():
            if letter not in freq2.keys():
                return False
            if freq1[letter] != freq2[letter]:
                return False
        return True
              