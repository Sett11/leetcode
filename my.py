class Solution:
    def divideArray(self,a):
        a.sort()
        r=[a[i]==a[i+1] for i in range(0,len(a)-1,2)]
        return all(r) and len(r)==len(a)/2
    
s=Solution()

print(s.divideArray([3,2,3,2,2,2]))