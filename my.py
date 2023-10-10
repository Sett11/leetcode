class Solution:
    def deleteGreatestValue(self,a):
        m=0
        while all(i for i in a):
            n=0
            for i in range(len(a)):
                n=max(n,a[i].pop(a[i].index(max(a[i]))))
            m+=n
        return m
    
s=Solution()

print(s.deleteGreatestValue([[1,2,4],[3,3,1]]))