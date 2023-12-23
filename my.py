from bisect import insort

class Solution:
    def findClosestElements(self,a,n,k):
        r=[]
        for i in a:
            insort(r,[abs(k-i),i])
        return list(map(lambda y:y[1],sorted(r[:n],key=lambda x:x[1])))
    
S=Solution()

print(S.findClosestElements([1,2,3,4,5],4,3))
print(S.findClosestElements([1,1,1,10,10],1,9))