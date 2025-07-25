class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        mid=n//2
        if n%2!=0:
            return float(merged[n//2])
        return(merged[mid-1]+merged[mid])/2

        