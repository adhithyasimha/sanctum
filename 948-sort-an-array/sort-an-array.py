class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,r):
            if l>=r:
                return
            mid=(l+r)//2
            merge(l,mid)
            merge(mid+1,r)

            temp=[]
            i,j=l,mid+1
            while i<=mid and j<=r:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1

            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=r:
                temp.append(nums[j])
                j+=1
            for k in range(len(temp)):
                nums[l+k]=temp[k]
        
        merge(0,len(nums)-1)
        return nums

            
        