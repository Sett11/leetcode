class Solution:
    def maximumUnits(self,a,n):
        a=sorted(a,key=lambda e:e[1],reverse=True)
        i=c=0
        while i<len(a) and n:
            if n:
                while a[i][0] and n:
                    a[i][0]-=1
                    c+=a[i][1]
                    n-=1
                i+=1
        return c
    
s=Solution()

print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10))