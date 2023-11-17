from collections import defaultdict
from heapq import heappush,heappop

def convert_two_dimensional_array_to_graph(a):
    d=defaultdict(list)

    for i,j in a:
        d[i].append(j)
        d[j].append(i)

    return d

class Solution:
    def maxStarSum(self,v,r,k):
        g=convert_two_dimensional_array_to_graph(r)
        if not r:
            return max(v)
        m=float('-inf')

        for i in g:
            t=[]
            for j in g[i]:
                heappush(t,v[j])
                while len(t)>k:
                    heappop(t)
            p=v[i]
            for x in range(len(t)):
                p=max(p,p+t[x])
                m=max(m,p)

        return max(m,max(v))
    
S=Solution()

print(S.maxStarSum([1,2,3,4,10,-10,-20],[[0,1],[1,2],[1,3],[3,4],[ 3,5],[3,6]],2))
print(S.maxStarSum([-2,-1,-2],[[0,2]],1))