class Solution:
    def longestPalindromeSubseq(self,a):
        b=a[::-1]
        n,m=len(a),len(b)
        r=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i-1]==b[j-1]:
                    r[i][j]=1+r[i-1][j-1]
                else:
                    r[i][j]=max(r[i-1][j],r[i][j-1])
        return r[-1][-1]

s=Solution()

print(s.longestPalindromeSubseq('abcddce'))