class Solution:
    def reverseString(self, s: list[str]) -> None:
       
        n = len(s)
        
        for ch in range(n//2):
            s[ch], s[n-1-ch] = s[n-1-ch], s[ch]
        return s    
        
        
        