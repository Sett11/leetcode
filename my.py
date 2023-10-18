class Solution:
    def semiOrderedPermutation(self,a):
        one=a.index(1)
        m=max(a)
        n=a.index(m)
        c=0
        while one!=0 or n!=len(a)-1:
            while one!=0:
                a[one],a[one-1]=a[one-1],a[one]
                one=a.index(1)
                c+=1
            n=a.index(m)
            while n!=len(a)-1:
                a[n],a[n+1]=a[n+1],a[n]
                n=a.index(m)
                c+=1
        return c

s = Solution()

print(s.semiOrderedPermutation([2,1,3]))
print(s.semiOrderedPermutation([2,4,1,3]))