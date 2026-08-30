class Solution(object):
    def longestCommonPrefix(self, strs):
        smallest = len(strs[0])
        s = ""

        for word in strs:
            if len(word) < smallest:
                smallest = len(word)

        for i in range(smallest):
            for j in strs:
                if j[i] != strs[0][i]:
                    return s

            s = s + strs[0][i]

        return s