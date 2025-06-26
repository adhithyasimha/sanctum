class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less,equal=0,0

        for num in nums:
            if num<target:
                less+=1
            elif num==target:
                equal+=1
        
        return[i for i in range(less,less+equal)]

