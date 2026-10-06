class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        ptr2 = n-1
        ptr3 = m + n - 1
        while ptr3 >= 0 and ptr1 >=0 and ptr2 >=0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr3], nums1[ptr1] = nums1[ptr1],nums1[ptr3]
                ptr1 -= 1
                ptr3 -= 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
                ptr3 -= 1
        if ptr1 < 0:
            for i in range(ptr2+1):
                nums1[i] = nums2[i]
        return nums1