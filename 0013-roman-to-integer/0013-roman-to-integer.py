class Solution(object):
    def romanToInt(self, s):
        k=0
        tot=0
        subt=0
        add=0
        d={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
            
        for i in range(1,len(s)):
            if d[s[k]]<d[s[i]]:
                tot=tot-d[s[k]]
            else:
                tot=tot+d[s[k]]
            k+=1
        l=len(s)-1
        tot=tot+d[s[l]]
        return tot