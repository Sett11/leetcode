class Solution:
    def fourSum(self,a,d):
        a.sort()
        l=len(a)
        s=set()
        for i in range(l):
            o=a[i]
            for j in range(i+1,l):
                t=a[j]
                k=j+1
                h=l-1
                while k<h:
                    th=a[k]
                    f=a[h]
                    p=o+t+th+f
                    if p==d:
                        s.add((o,t,th,f))
                        k+=1
                        h-=1
                    elif p>d:
                        h-=1
                    elif p<d:
                        k+=1
                    else:
                        h-=1
                        k+=1
        return s
    

s=Solution()

print(s.fourSum([1,0,-1,0,-2,2],0))
print(s.fourSum([2,2,2,2,2],0))