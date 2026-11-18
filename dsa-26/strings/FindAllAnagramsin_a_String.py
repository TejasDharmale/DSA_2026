class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        p_freq = {}
        for ch in p:
            if ch in p_freq:
                p_freq[ch] += 1
            else:
                p_freq[ch] = 1
        for i in range(0, len(s)-len(p)+1):
            s_freq = {}
            for j in range(i, i + len(p)):
                ch = s[j]
                if ch in s_freq:
                    s_freq[ch] += 1
                else:
                    s_freq[ch] = 1
            if s_freq == p_freq:
                result.append(i)
        return result


# this brute force solution has time complexity of O(n*m) where n is the length of s and m is the length of p.
