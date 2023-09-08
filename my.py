class Solution:
    def customSortString(self,t,s):
        return ''.join(map(lambda e:e[1],sorted([[t.index(i) if i in t else s.index(i),i] for i in s])))
    
s=Solution()

print(s.customSortString("cba","abcd"))
print(s.customSortString("cbafg","abcd"))