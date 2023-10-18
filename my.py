class Solution:
    def buyChoco(self,a,n):
        q=min(a)
        a.remove(q)
        s=n-(min(a)+q)
        return s if s>=0 else n


s = Solution()

print(s.buyChoco([1,2,2],3))
print(s.buyChoco([98,54,6,34,66,63,52,39],62))