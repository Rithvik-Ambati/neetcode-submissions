class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_ans = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for x in range(k + 1, len(nums)):

                        if nums[i] + nums[j] + nums[k] + nums[x] == target:

                            iter_answer = tuple(sorted([
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[x]
                            ]))

                            final_ans.add(iter_answer)

        return [list(x) for x in final_ans]