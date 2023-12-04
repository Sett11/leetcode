class Solution:
    def kthGrammar(self,n,k):
        v=True
        n=1<<(n-1)

        while n!=1:
            n//=2
            if k>n:
                k-=n
                v=not v
        
        return 0 if v else 1
    
S=Solution()

print(S.kthGrammar(2,2))