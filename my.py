class Solution:
    def sequentialDigits(self,a,b):
        n,m,t,r=len(str(a)),len(str(b))+1,'123456789',[]

        while n<m:
            for i in range(10-n):
                x=int(t[i:i+n])
                if a<=x<=b:
                    r.append(x)
            n+=1

        return r

    

S=Solution()

print(S.sequentialDigits(1000,10**9))