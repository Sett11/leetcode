from itertools import permutations
class Solution:
    def minimumSum(self,n):
        a=list(str(n))
        p=[int(j[0])+int(j[1]) for j in [[a[0]+a[1],a[2]+a[3]],[a[0]+a[1],a[3]+a[2]],[a[1]+a[0],a[3]+a[2]],[a[1]+a[0],a[2]+a[3]],[a[0]+a[2],a[1]+a[3]],[a[2]+a[0],a[3]+a[1]],[a[0]+a[3],a[1]+a[2]],[a[3]+a[0],a[2]+a[1]]]]
        for i in range(len(a)):
            q=a.pop(0)
            p.extend(sum([[int(q)+int(''.join(j))] for j in permutations(a)],[]))
            a.append(q)
        return min(p)
    
s=Solution()

print(s.minimumSum(2436))