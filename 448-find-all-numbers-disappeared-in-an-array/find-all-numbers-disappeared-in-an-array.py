class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        exp=set(range(1,n+1))
        actual=set(nums)
        return list(exp-actual)