class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map={}
        nums_sorted=sorted(nums)
        for num in nums_sorted:
            if num in count_map:
                count_map[num]+=1
            else:
                count_map[num]=1
        for num,count in count_map.items():
                        if count<2:
                            return num
                   