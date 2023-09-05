class Solution:
    def intersection(self,a,b):
        return list(set(a).intersection(set(b)))
    
s=Solution()

print(s.intersection([4,9,5],[9,4,9,8,4]))