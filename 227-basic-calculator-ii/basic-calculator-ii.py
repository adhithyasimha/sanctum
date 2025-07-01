class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        s += '+'  

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                num = num * 10 + int(c)

            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))

                sign = c
                num = 0

        return sum(stack)
