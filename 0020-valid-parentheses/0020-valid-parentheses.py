class Solution(object):
    def isValid(self, s):
        stack = []
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in d:
                # Opening bracket
                stack.append(char)
            else:
                # Closing bracket
                if not stack:
                    return False

                if char != d[stack[-1]]:
                    return False

                stack.pop()

        return len(stack) == 0


sol = Solution()

s = "()[]{}"
print(sol.isValid(s))