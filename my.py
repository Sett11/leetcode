class Solution:
    def averageValue(self,a):
        a=[i for i in a if not i&1 and not i%3]
        return int(sum(a)/len(a)) if len(a) else 0
            
    
s=Solution()

print(s.averageValue([1,3,6,10,12,15]))