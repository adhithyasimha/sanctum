class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap arr[i] to its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first place where index + 1 != value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all values from 1 to n are present
        return n + 1
