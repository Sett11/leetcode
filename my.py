from bisect import insort_left

class Solution:
    def mergeSimilarItems(self,a,b):
        a=a+b
        i=0
        r=[]
        while i<len(a):
            j=i+1
            while j<len(a):
                if a[i][0]==a[j][0]:
                    a[i][1]+=a[j][1]
                    a.pop(j)
                    j-=1
                j+=1
            insort_left(r,a[i])
            i+=1
        return r

s=Solution()

print(s.mergeSimilarItems([[1,3],[2,2]],[[7,1],[2,2],[1,4]]))