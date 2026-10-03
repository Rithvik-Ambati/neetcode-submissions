class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_array = [1] * n

        # Product of elements to the left
        prod = 1
        for i in range(n):
            prod_array[i] = prod
            prod = prod * nums[i]

        # Product of elements to the right
        prod = 1
        for i in range(n - 1, -1, -1):
            prod_array[i] = prod_array[i] * prod
            prod = prod * nums[i]

        return prod_array