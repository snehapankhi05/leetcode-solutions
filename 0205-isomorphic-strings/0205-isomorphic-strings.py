class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        f = {}
        r = {}

        for i in range(len(s)):

            if s[i] in f:
                if f[s[i]] != t[i]:
                    return False
            else:
                f[s[i]] = t[i]

            if t[i] in r:
                if r[t[i]] != s[i]:
                    return False
            else:
                r[t[i]] = s[i]

        return True