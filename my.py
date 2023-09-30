class Solution:
    def uniqueOccurrences(self,a):
        b=[a.count(i) for i in set(a)]
        return len(b)==len(set(b))
    
s=Solution()

print(s.uniqueOccurrences([1,1,1,2,2,3]))