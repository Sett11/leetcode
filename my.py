class Solution:
    def mergeArrays(self,a,b):
        c=a+b
        r=[]
        i=0
        c.sort()
        while i<len(c):
            t=c[i]
            j=i+1
            while j<len(c):
                if t[0]==c[j][0]:
                    t[1]+=c[j][1]
                    c.pop(j)
                    j-=1
                j+=1
            i+=1
            r.append(t)
        return r
    
s=Solution()

print(s.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))
print(s.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))