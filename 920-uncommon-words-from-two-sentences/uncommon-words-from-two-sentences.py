class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dummy=[]
        for i in s1.split():
            dummy.append(i)
        for i in s2.split():
            dummy.append(i)
        res=[]
        count=Counter(dummy)
        for i,j in count.items():
            if j==1:
                res.append(i)
        return res



        