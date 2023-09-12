from bisect import insort,bisect_left

class Solution:
    def reversePairs(self,a):
        c=0
        t=[a[-1]*2]
        for i in range(len(a)-2,-1,-1):
            n=a[i]
            c+=bisect_left(t,n)
            insort(t,n*2)
        return c
    
s=Solution()

print(s.reversePairs([1,3,2,3,1]))
print(s.reversePairs([2,4,3,5,1]))