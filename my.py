class Solution:
    def maxSum(self,a):
        a=sorted([[max(list(map(int,str(i)))),i] for i in a])
        m=-1
        for i in range(len(a)-1):
            if a[i][0]==a[i+1][0]:
                m=max(m,a[i][1]+a[i+1][1])
        return m


s = Solution()

print(s.maxSum([51,71,17,24,42]))
