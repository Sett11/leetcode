class Solution:
    def findAnagrams(self,s,t):
        r=[]
        t=sorted(t)
        for i in range(len(s)-len(t)+1):
            if sorted(s[i:i+len(t)])==t:
                r.append(i)
        return r
    
s=Solution()

print(s.findAnagrams('cbaebabacd','abc'))
print(s.findAnagrams('abab','ab'))