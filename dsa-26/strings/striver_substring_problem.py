class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                odd_count = 0
                ch = s[j]
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1

                for value in freq.values():
                    if value % 2 != 0:
                        odd_count += 1
                if odd_count <= 1:
                    result += 1

        return result

# this is a brute force solution with time complexity of O(n^3) where n is the length of s.
# here we are checking all the substrings of s and counting the frequency of each character in the substring.
# checking if the substring can be rearranged to form a palindrome by counting the number of characters with odd frequency.
# time exceeds for large inputs. so best solution is to use dynamic programming or center expansion technique to reduce the time complexity to O(n^2).
