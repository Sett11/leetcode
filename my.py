def wrap(a):
    return [int(str(i)[-1]) for i in a]

def triangle_sum(a):
    if len(a)==1:
        return a[0]
    return triangle_sum(wrap([a[i]+a[i+1] for i in range(len(a)-1)]))

class Solution:
    def triangularSum(self,a):
        return triangle_sum(wrap(a))
    
s=Solution()

print(s.triangularSum([1,2,3,4,5,6,7,8,9]))