class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        string1 = strs[0]
        string2 = strs[1:]
        final = ""

        for i, ch in enumerate(string1):
            matched = True
            for j in string2:
                if i >= len(j):
                    matched = False
                    break
                else:
                    if string1[i] != j[i]:
                        matched = False
                        break
            if matched == True:
                final += ch
            else:
                break

        return final
