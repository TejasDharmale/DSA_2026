class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()
        string = rev[::-1]
        final_res = " ".join(string)
        return final_res
