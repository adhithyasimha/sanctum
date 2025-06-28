class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        original=nums[:]

        nums.sort()
        res=nums[-k:]
        ans=[]
        count={}

        for num in res:
            count[num] = count.get(num, 0) + 1

        for num in original:
            if num in count and count[num] > 0:
                ans.append(num)
                count[num] -= 1
                if len(ans) == k:
                    break

        return ans