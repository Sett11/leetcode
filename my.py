class Solution:
    def countPrefixes(self,a,p):
        return len([i for i in a if p.startswith(i)])

s = Solution()

print(s.countPrefixes(["a","b","c","ab","bc","abc"],'abc'))