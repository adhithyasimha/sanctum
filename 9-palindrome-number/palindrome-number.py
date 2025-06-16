class Solution:
    def isPalindrome(self, x: int) -> bool:
        to_str=str(x)
        if to_str == to_str[::-1]:
            return True
        else:
            return False
        
        