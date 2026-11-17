class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        new_s = s.rstrip()
        for i, ch in enumerate(new_s[::-1]):
            if ch == " ":
                break
            else:
                count += 1
        return count
