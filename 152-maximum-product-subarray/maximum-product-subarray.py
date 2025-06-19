class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_min = current_max = overall =nums[0]

        for i in range(1, len(nums)):
            num=nums[i]
            temp_max = max(num,num*current_min,num*current_max)
            current_min=min(num,num*current_min,num*current_max)
            current_max=temp_max

            overall=max(overall,current_max)
        return overall        