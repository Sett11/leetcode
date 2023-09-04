from itertools import combinations
class Solution:
    def subsets(self,a):
        r=[]
        for i in range(1,len(a)):
            r.extend(['&'.join([str(k) for k in sorted(j)]) for j in combinations(a,i)])
        return [[]]+[[int(j) for j in i.split('&')] for i in set(r)]+[a]
    
s=Solution()

print(s.subsets([1,2,2]))