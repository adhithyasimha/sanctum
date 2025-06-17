class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count_map={}
        res=[]

        for num in nums:
            if num in count_map:
                count_map[num]+=1
            else:
                count_map[num]=1
        
        for num,count in count_map.items():
            if count>n//3:
                res.append(num)
        return res
