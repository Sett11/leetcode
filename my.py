class Solution:
    def search(self,a,n):
        for i in range(len(a)):
            if a[i]==n:
                return i
        return -1
s=Solution()

print(s.search([4,5,6,7,0,1,2],0))