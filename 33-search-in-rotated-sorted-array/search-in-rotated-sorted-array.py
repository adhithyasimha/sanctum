class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1


        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            #check if the left side is sorted
            if nums[l]<=nums[mid]:
                #check if the nums[i]<target<nums[mid]
                if nums[l]<=target<nums[mid]:
                    """ if the num is present in between i and mid i can reduce the r size """
                    r=mid-1
                #if its not present than it is towards the right
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1



