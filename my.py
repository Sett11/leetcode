class Solution:
    def arrangeCoins(self,n):
        c=0
        i=1
        while n>0:
            n-=i
            i+=1
            c+=1
        return c if not n else c-1
    
s=Solution()

print(s.arrangeCoins(8))
print(s.arrangeCoins(5))
print(s.arrangeCoins(10000000))