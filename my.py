def f(a,k,t):
    i,j,q,w=t+1,t-1,-1,-1
    while i<=len(a):
        if a[i]!=k or i==len(a)-1:
            q=a[i]
            break
        i+=1
    while j>=0:
        if a[j]!=k or not j:
            w=a[j]
            break
        j-=1
    return w,q

class Solution:
    def countHillValley(self,a):
        r,q=[],[]
        for i in range(1,len(a)-1):
            t=f(a,a[i],i)
            if (t[0]>a[i] and t[1]>a[i]) or (t[0]<a[i] and t[1]<a[i]):
                r.append(a[i])
        i=0
        while i<len(r):
            if i==len(r)-1:
                q.append(r[i])
                break
            if r[i]!=r[i+1]:
                q.append(r[i])
            i+=1
        return len(q)
    
s=Solution()

print(s.countHillValley([2,4,1,1,6,5]))
print(s.countHillValley([6,6,5,5,4,1]))
print(s.countHillValley([3,3,1]))