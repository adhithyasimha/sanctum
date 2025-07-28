class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)

        dp_max=[0]*n
        dp_max[0]=nums[0]
        for i in range(1,n):
            dp_max[i]=max(nums[i],dp_max[i-1]+nums[i])
        dp_=max(dp_max)

        dp_min=[0]*n
        dp_min[0]=nums[0]
        for i in range(1,n):
            dp_min[i]=min(nums[i],dp_min[i-1]+nums[i])
        dp__=min(dp_min)

        if dp_<0:
            return dp_
        
        return max(dp_,total_sum-dp__)
