class Solution:
    def circularGameLosers(self,n,k):
        a=[i for i in range(1,n+1)]
        r=[1]
        i=k
        j=2
        while True:
            i+=j*k
            j+=1
            c=a[i%n]
            if c in r:
                break
            r.append(c)
        return list(set(a).difference(r))
    
s=Solution()

print(s.circularGameLosers(3,1))