class Solution:
    def findDuplicates(self,a):
        a.sort()
        r=[]
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                r.append(a[i])
        return r

s=Solution()

print(s.findDuplicates([4,3,2,7,8,2,3,1]))