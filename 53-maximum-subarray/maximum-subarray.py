class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overall=nums[0]
        current=nums[0]

        for i in range(1,len(nums)):
            current=max(nums[i],nums[i]+current)
            overall=max(overall,current)

        return overall
        