class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div=[]
        notdiv=[]
        for i in range(1,n+1):
            if i%m==0:
                div.append(i)
            else:
                notdiv.append(i)
        total=sum(notdiv)-sum(div)
        return total

        