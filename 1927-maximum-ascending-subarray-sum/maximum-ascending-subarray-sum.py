class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        left=0
        right=left+1
        res=[nums[left]]
        max_sum=0
        for i in range(len(nums)-1):
            if nums[left]<nums[right]:
                res.append(nums[right])
                left+=1
                right+=1
            else:
                max_sum=max(max_sum,sum(res))
                res = [nums[right]]
                left+=1
                right+=1
        max_sum=max(max_sum,sum(res))

        return max_sum




        