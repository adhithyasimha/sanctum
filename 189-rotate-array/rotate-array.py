class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums,start,end):
            while start < end:
                nums[start],nums[end]=nums[end],nums[start]

                start+=1
                end-=1

        n=len(nums)
        k%=n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)

        
        