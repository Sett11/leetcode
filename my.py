class Solution:
    def maxProduct(self,a):
        m=0
        a=list(set(a))
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                s=0
                for h in a[i]:
                    if h not in a[j]:
                        s=len(a[i])*len(a[j])
                    else:
                        s=0
                        break
                m=max(m,s)
        return m
    
s=Solution()

print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))