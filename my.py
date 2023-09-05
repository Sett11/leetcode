class Solution:
    def findDifference(self,a,b):
        a,b=set(a),set(b)
        return [list(i) for i in [a.difference(b),b.difference(a)]]
    
s=Solution()

print(s.findDifference([1,2,3],[2,4,6]))