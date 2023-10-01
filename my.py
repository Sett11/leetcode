class Solution:
    def average(self,a):
        a.remove(min(a))
        a.remove(max(a))
        return sum(a)/len(a)
    
s=Solution()

print(s.average([4000,3000,1000,2000]))