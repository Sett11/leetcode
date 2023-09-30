class Solution:
    def getSmallestString(self,n,k):
        a=['a']*n
        v=n
        for i in range(n-1,-1,-1):
            if v==k:
                break
            v-=1
            a[i]=chr(96+min(k-v,26))
            v+=ord(a[i])-96
        return ''.join(a)
    
s=Solution()

print(s.getSmallestString(5,73))