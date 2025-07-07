class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = nums1[:m] + nums2[:n] 
        res.sort()

        for i in range(len(res)):
            nums1[i] = res[i]

        for i in range(len(res), len(nums1)):
            nums1[i] = 0
