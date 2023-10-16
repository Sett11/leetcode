class Solution:
    def maximizeSum(self,a,k):
        c=max(a)
        r=[]
        while len(r)<k:
            r.append(c)
            c+=1
        return sum(r)

s = Solution()

print(s.maximizeSum([1,2,3,4,5],3))
