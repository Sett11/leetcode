class Solution:
    def minCostClimbingStairs(self,a):
        n=len(a)
        r=[0]*n
        r[0],r[1]=a[0],a[1]
        for i in range(2,n):
            r[i]=a[i]+min(r[i-1],r[i-2])
        return min(r[-1],r[-2])

s=Solution()

print(s.minCostClimbingStairs([10, 15,20]))
print(s.minCostClimbingStairs([ 1 ,100, 1 ,1, 1 , 100, 1 , 1 ,100, 1]))