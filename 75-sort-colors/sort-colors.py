class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3  
        for num in nums:
            count[num] += 1
        idx = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[idx] = color
                idx += 1

