class Solution:
    def maximumNumberOfStringPairs(self,s):
        return len(s)-len(set([''.join(sorted(i)) for i in s]))
    
s=Solution()

print(s.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))