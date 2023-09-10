class Solution:
    def sumBase(self,n,k):
        i=0
        while n:
            if n//k:
                i+=n%k
                n//=k
            else:
                i+=n
                n=0
        return i

    
s=Solution()

print(s.sumBase(34,6))