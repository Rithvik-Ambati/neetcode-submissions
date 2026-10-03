class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      find_num = {}
      for i in range(len(nums)):
        curr_num_comp = target - nums[i]
        if curr_num_comp in find_num:
            return [find_num[curr_num_comp],i]
        else:
            find_num[nums[i]] = i

    """
    psuedocode:
    put array indexes in dictionary
    then find target -  current index in the dictionary
    """ 