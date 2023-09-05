class Solution:
    def kthDistinct(self,a,k):
        r=[i for i in a if a.count(i)==1]
        return '' if len(r)<k else r[k-1]

s=Solution()

print(s.kthDistinct(["d","b","c","b","c","a"],2))
print(s.kthDistinct(['a','a'],1))