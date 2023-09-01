def f(s,k):
    if len(s)<=k:
        return s
    return f(''.join([str(sum([int(j) for j in s[i:i+k]])) for i in range(0,len(s),k)]),k)

class Solution:
    def digitSum(self,s,k):
        return f(s,k)
    
s=Solution()

print(s.digitSum('11111222223',3))