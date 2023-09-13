class Solution:
    def countSubstrings(self,s):
        l=len(s)
        c=0
        for i in range(l):
            for j in range(i+1,l+1):
                if s[i:j]==s[i:j][::-1]:
                    c+=1
        return c
    
s=Solution()

print(s.countSubstrings('abc'))
print(s.countSubstrings('aaa'))