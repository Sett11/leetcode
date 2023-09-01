class Solution:
    def containsDuplicate(self,a):
        return len(set(a))!=len(a)
    
s=Solution()

print(s.containsDuplicate([1,2,3,4,1]))