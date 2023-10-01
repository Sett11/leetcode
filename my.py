def canMakeArithmeticProgression(a):
    a.sort()
    n=a[1]-a[0]
    return all(a[i+1]-a[i]==n for i in range(len(a)-1))

class Solution:
    def checkArithmeticSubarrays(self,a,b,c):
        r=[]
        for i in range(len(b)):
            r.append(canMakeArithmeticProgression(a[b[i]:c[i]+1]))
        return r
        
    
s=Solution()

print(s.checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))