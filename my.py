class Solution:
    def kthFactor(self,n,k):
        r=[1]
        for i in range(2,n//2):
            if n%i==0:
                r.append(i)
                if len(r)==k:
                    return r[-1]
        if n%2==0 and n//2 not in r:
            r.append(n//2)
        r.append(n)
        return r[k-1] if k<=len(r) else -1


    
S=Solution()
    
print(S.kthFactor(2,2))