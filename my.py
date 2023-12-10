class Solution:
    def replaceElements(self,a):
        m=-1
        for i in range(len(a)-1,-1,-1):
            a[i],m=m,max(a[i],m)
        return a


    
S=Solution()
    
print(S.replaceElements([17,18,5,4,6,1]))