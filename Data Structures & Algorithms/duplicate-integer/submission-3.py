class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        present = set()
        for i in range (len(nums)):
            if nums[i] not in present:
               present.add(nums[i])
           else:
                return True
        return False
        """
        return len(nums) > len(set(nums)) 
