class Solution:
    def rotateString(self,s,t):
        i=0
        while i<len(s):
            if s==t:
                return True
            s=s[1:]+s[0]
            i+=1
        return False
    
s=Solution()

print(s.rotateString('abcde','bcdea'))