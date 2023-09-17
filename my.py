class Solution:
    def divideString(self,s,k,f):
        r=[s[i:i+k] for i in range(0,len(s),k)]
        l=len(r[-1])
        if l<k:
            r[-1]+=f*(k-l)
        return r
    
s=Solution()

print(s.divideString('abcdefghij',3,'x'))