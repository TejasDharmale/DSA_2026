class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for ch in s:
        #     if s.count(ch)==1:
        #         return s.index(ch)
        # return -1
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
