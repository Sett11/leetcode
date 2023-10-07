class Solution:
    def findKDistantIndices(self,a,k,n):
        s=set()
        for i in range(len(a)):
            for j in range(len(a)):
                if abs(i-j)<=n and a[j]==k:
                    s.add(i)
        return list(s)

s=Solution()

print(s.findKDistantIndices([3,4,9,1,3,9,5],9,1))