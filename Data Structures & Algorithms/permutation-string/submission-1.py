class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        freq1 = {}
        freq2 = {}

        for char in s1:
            if char not in freq1:
                freq1[char] = 1
            else:
                freq1[char] += 1

        for i in range(len(s1)):
            char = s2[i]
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1

        if freq1 == freq2:
            return True
        
        for i in range(len(s1), len(s2)):
            char = s2[i]
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1
            old_char = s2[i - len(s1)]
            freq2[old_char] -= 1
            if freq2[old_char] == 0:
                del freq2[old_char]
            if freq1 == freq2:
                return True
        return False



