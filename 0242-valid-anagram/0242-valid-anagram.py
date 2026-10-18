class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        count1={}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        
        for char in t:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1
        return count==count1
        
        