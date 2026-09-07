class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            k = 0

            while k < len(needle):
                if i + k >= len(haystack):
                    break

                if haystack[i + k] != needle[k]:
                    break

                k += 1

            if k == len(needle):
                return i

        return -1


sol = Solution()

haystack = "sadbutsad"
needle = "sad"

a = sol.strStr(haystack, needle)

print(a)