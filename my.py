class Solution:
    def sortPeople(self,a,b):
        return [j[1] for j in sorted([[b[i],a[i]] for i in range(len(a))],reverse=True)]
    
s=Solution()

print(s.sortPeople(["Mary","John","Emma"],[180,165,170]))