class Solution:
    def kidsWithCandies(self,a,k):
        r=[]
        [r.append(True) if i+k>=max(a) else r.append(False) for i in a]
        return r
    
s=Solution()

print(s.kidsWithCandies([2,3,5,1,3],3))
print(s.kidsWithCandies([4,2,1,1,2],1))