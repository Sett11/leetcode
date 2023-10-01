class Solution:
    def sumOddLengthSubarrays(self,a):
        l=len(a)
        c=0
        for i in range(l):
            for j in range(i+1,l+1):
                t=a[i:j]
                if len(t)&1:
                    c+=sum(t)
        return c
    
s=Solution()

print(s.sumOddLengthSubarrays([1,4,2,5,3]))