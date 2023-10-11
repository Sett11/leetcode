class Solution:
    def countConsistentStrings(self,s,a):
        return len([i for i in a if all(j in s for j in i)])
    
s=Solution()

print(s.countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))