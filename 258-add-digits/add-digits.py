class Solution:
    def addDigits(self, num: int) -> int:
        seen=set()
        while len(str(num))!=1 and num not in seen:
            seen.add(num)
            num=sum(int(d) for d in str(num))

        return num


        