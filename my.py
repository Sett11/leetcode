class Solution:
    def findThePrefixCommonArray(self,a,b):
        return [len(set(a[:i]).intersection(set(b[:i]))) for i in range(1,len(a)+1)]

    
s=Solution()

print(s.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
print(s.findThePrefixCommonArray([2,3,1],[3,1,2]))