class Solution:
    def makeFancyString(self, s: str) -> str:
        ref=[]
        count=1
        for i in s:
            if len(ref)==0:
                ref.append(i)
                count=1
            
            elif ref[-1]==i:
                count+=1
                ref.append(i)
                if count==3:
                    ref.pop()
                    count=2
            else:
                ref.append(i)
                count=1
        return ''.join(ref)
           
            
        
        