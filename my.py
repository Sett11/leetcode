class Solution:
    def reorderSpaces(self,s):
        a,n,r=s.split(),s.count(' '),''
        if not n:
            return s
        if len(a)==1:
            return a[0]+' '*n
        k=n//(len(a)-1)
        for i in range(len(a)):
            r+=a[i]+' '*k
            if i!=len(a)-1:
                n-=k
        r=r.strip()
        return r+' '*n
    
S=Solution()

print(S.reorderSpaces("  this   is  a sentence "))
print(S.reorderSpaces(" practice   makes   perfect"))