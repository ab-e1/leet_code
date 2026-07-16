class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:

            if i >= len(strs[0]):
                break
            letter = strs[0][i]

            j = 1
            while j < len(strs):
                if i >= len(strs[j]):
                    return strs[0][:i]
                elif strs[j][i] != letter:
                    return strs[0][:i]
                j+=1

            i+=1
        return strs[0]
            

        