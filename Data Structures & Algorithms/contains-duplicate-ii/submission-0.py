class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            left = i
            right = left + 1
            for j in range(right,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False