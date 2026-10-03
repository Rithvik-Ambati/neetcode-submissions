class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        max_vol = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                cur_vol = min(heights[i],heights[j])*(j-i)
                if cur_vol >= max_vol:
                    max_vol = cur_vol
        return max_vol
        """
        left = 0
        right = len(heights) - 1
        max_vol = 0
        while left < right:
            cur_vol = min(heights[left],heights[right])*(right - left)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            if cur_vol >= max_vol:
                max_vol = cur_vol
        return max_vol
        