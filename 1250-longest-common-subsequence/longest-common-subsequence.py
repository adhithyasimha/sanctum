class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def backtrack(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + backtrack(i + 1, j + 1)
            else:
                return max(backtrack(i + 1, j), backtrack(i, j + 1))

        return backtrack(0, 0)
