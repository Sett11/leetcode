class Solution:
    def lexicalOrder(self,n):
        return sorted([i for i in range(1,n+1)],key=str)
    
s=Solution()

print(s.lexicalOrder(50000))