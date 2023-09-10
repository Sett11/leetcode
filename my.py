from itertools import combinations

class Solution:
    def findSubsequences(self,a):
        r=[]
        for j in range(2,len(a)):
            r.extend([list(i) for i in combinations(a,j)])
        r.append(a)
        return list(filter(lambda e:e==sorted(e) and len(e)>1,[[int(h) for h in k.split('&')] for k in set(['&'.join([str(j) for j in i]) for i in r])]))
    
s=Solution()

print(s.findSubsequences([4,6,7,7]))
print(s.findSubsequences([4,4,3,2,1]))