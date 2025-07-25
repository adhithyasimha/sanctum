class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]


                