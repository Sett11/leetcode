class Solution:
    def findCenter(self,a):
        return list(set(a[0])&set(a[1]))[0]
    
S=Solution()

print(S.findCenter([[1,2],[2,3],[4,2]]))