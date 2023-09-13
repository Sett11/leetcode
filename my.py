class Solution:
    def dominantIndex(self,a):
        b=a.copy()
        
        def f(l):
            return l.pop(l.index(max(l)))
        
        return b.index(max(b)) if f(a)>=f(a)*2 else -1
    
s=Solution()

print(s.dominantIndex([3,6,1,0]))
print(s.dominantIndex([4,2,3,1]))