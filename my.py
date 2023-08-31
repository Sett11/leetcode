class Solution:
    def countEven(self,n):
        return len([i for i in range(2,n+1) if sum([int(j) for j in str(i)])%2==0])
    
s=Solution()

print(s.countEven(30))