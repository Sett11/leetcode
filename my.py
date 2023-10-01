class Solution:
    def canMakeArithmeticProgression(self,a):
        a.sort()
        return all(a[i+1]-a[i]==a[1]-a[0] for i in range(len(a)-1))
        
    
s=Solution()

print(s.canMakeArithmeticProgression([3,1,5]))