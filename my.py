class Solution:
    def isAlienSorted(self,w,s):
        a=[[s.index(j) for j in i] for i in w]
        return sorted(a)==a
    
s=Solution()

print(s.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))