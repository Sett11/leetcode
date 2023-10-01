class Solution:
    def runningSum(self,a):
        r=[]
        c=0
        for i in range(len(a)):
            c+=a[i]
            r.append(c)
        return r
    
s=Solution()

print(s.runningSum([1,2,3,4]))