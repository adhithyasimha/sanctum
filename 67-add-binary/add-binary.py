class Solution:
    def addBinary(self, a: str, b: str) -> str:
        deci_a=int(a,2)
        deci_b=int(b,2)

        tot=deci_a+deci_b

        tot_bin=bin(tot)[2:]
        return tot_bin