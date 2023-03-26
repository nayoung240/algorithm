class Solution:
    from collections import Counter

    def closeStrings(self, word1: str, word2: str) -> bool:
        a_len = len(word1)
        b_len = len(word2)

        if a_len != b_len:
            return False

        a = Counter(word1)
        b = Counter(word2)

        if set(a) - set(b):
            return False
        
        if Counter(a.values()) != Counter(b.values()):
            return False
        
        return True
