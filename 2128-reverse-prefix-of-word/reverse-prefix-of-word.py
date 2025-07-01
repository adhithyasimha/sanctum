class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            indx=word.index(ch)
            first=word[:indx+1]
            second=word[indx+1:]
            reverse=first[::-1]
            return str(reverse+second)
        else:
            return word
            
        