class Solution:
    def checkInclusion(self,t,s):
        r=[]
        t=sorted(t)
        for i in range(len(s)-len(t)+1):
            if sorted(s[i:i+len(t)])==t:
                return True
        return False
    
s=Solution()

print(s.checkInclusion('ab','"eidbaooo"'))
print(s.checkInclusion('ab','eidboaoo'))