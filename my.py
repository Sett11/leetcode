class Solution:
    def destCity(self,a):
        for i in set(sum(a,[])):
            if any(j[1]==i for j in a) and not any(j[0]==i for j in a):
                return i
    
s=Solution()

print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))