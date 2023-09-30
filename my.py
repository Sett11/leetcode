class Solution:
    def relativeSortArray(self,a,b):
        return sorted([i for i in a if i in b],key=b.index)+sorted([i for i in a if i not in b])
    
s=Solution()

print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
print(s.relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))