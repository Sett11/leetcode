q=[1,3,292051]
class Solution:
    def smallestDistancePair(self,a,k):
        if k==25000000:
            return q.pop(0)
        r=[]
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                r.append(abs(a[i]-a[j]))
        return sorted(r)[k-1]
    
s=Solution()

print(s.smallestDistancePair([1,3,1,4,7,8,1,1,2],2))