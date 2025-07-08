class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=sentence.lower()
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in s:
                return False
        return True
        