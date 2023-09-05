class Solution:
    def coinChange(self,a,n):
        r=[n+1]*(n+1)
        r[0]=0
        a.sort()
        for i in range(1,n+1):
            for j in a:
                if i-j>=0:
                    r[i]=min(r[i],1+r[i-j])
        return r[n] if r[n]!=n+1 else -1
    
s=Solution()

print(s.coinChange([1,2,5],11))
print(s.coinChange([186,419,83,408],6249))