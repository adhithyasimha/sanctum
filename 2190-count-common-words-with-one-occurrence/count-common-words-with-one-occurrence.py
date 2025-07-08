class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ch=[]
        count=0
        a=Counter(words1)
        b=Counter(words2)

        for i ,j in a.items():
            if j==1:
                ch.append(i)
        for i in ch:
            if b[i]==1:
                count+=1
        return count
