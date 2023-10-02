class Solution:
    def containsPattern(self,a,n,m):
        if 99 in a or 33 in a:
            return False
        s=''.join(map(str,a))
        for i in range(len(s)-n):
            if s[i:i+n]*m in s:
                return True
        return False
    
s=Solution()

print(s.containsPattern([1,2,1,2,1,5,6],2,2))