class Solution:
    def divisorSubstrings(self,n,k):
        s=list(str(n))
        a=[int(j) for j in [''.join(s[i:i+k]) for i in range(0,len(s))] if len(j)==k]
        c=0
        for i in a:
            if i and n%i==0:
                c+=1
        return c
    
s=Solution()

print(s.divisorSubstrings(430043,2))
print(s.divisorSubstrings(240,2))