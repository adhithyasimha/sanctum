class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        freq_list=[]
        res=[]
        for num,freq in count.items():
            freq_list.append((freq,num))
        freq_list.sort(reverse=True)
        for i in range(k):
            res.append(freq_list[i][1])
        return res
        