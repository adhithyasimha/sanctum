class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        sign=1
        res=0

        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=="+":
                res+=num*sign
                num=0
                sign=1
            elif c=="-":
                res+=num*sign
                num=0
                sign=-1
            elif c=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif c==")":
                res+=num*sign
                num=0
                res*=stack.pop()
                res+=stack.pop()
        if num!=0:
            res+=sign*num
        
        return res
        