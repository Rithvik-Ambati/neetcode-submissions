class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for i in range(len(strs)):
            a = [0] * 26
            for j in range(len(strs[i])):
                ascii_letter = ord(strs[i][j]) - ord("a")
                a[ascii_letter] += 1
            tup_c = tuple(a)
            if tup_c not in freq_dict:
                freq_dict[tup_c] = [strs[i]]
            else:
                freq_dict[tup_c].append(strs[i])
        
        ans = []
        for val in freq_dict.values():
            ans.append(val)
        return ans