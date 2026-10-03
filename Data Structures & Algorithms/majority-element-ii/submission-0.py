class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        n = len(nums)
        ans = []

        for key in freq:
            if freq[key] > n//3:
                ans.append(key)

        return ans 
