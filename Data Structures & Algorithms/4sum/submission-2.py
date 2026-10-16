class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def three_sum(curr_start,target_for_threesum):
            j = curr_start + 1
            result_for_twosum = set()

            while j < len(nums):
                left = j + 1
                right = len(nums) - 1
                target_for_twosum = target_for_threesum - nums[j]

                while left < right:
                    if nums[left] + nums[right] == target_for_twosum:
                        result_for_twosum.add(tuple([nums[j]] + [nums[left]] + [nums[right]]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target_for_twosum:
                        left += 1
                    else:
                        right -= 1
                j += 1

            final_result_fortwosum = list(result_for_twosum)
            for i in range(len(final_result_fortwosum)):
                final_result_fortwosum[i] = list(final_result_fortwosum[i])

            return final_result_fortwosum

        nums.sort()
        final_result = set()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            result_threesum = three_sum(i,target - nums[i])
            result = [[nums[i]] + result_threesum[l] for l in range(len(result_threesum))]
            for m in range(len(result)):
                final_result.add(tuple(result[m]))

        final_result = list(final_result)
        for i in range(len(final_result)):
            final_result[i] = list(final_result[i])

        return final_result        
        