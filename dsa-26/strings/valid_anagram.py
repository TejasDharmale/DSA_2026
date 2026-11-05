class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        n = len(s)
        m = len(t)
        if n != m:
            return False
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for ch in t:
            if ch in freq:
                freq[ch] -= 1
            else:
                return False
        if all(value == 0 for value in freq.values()):
            return True
        else:
            return False
