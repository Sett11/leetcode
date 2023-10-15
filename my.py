class Solution:
    def minNumber(self,a,b):
        c=set(a).intersection(b)
        return sorted(c)[0] if c else int(''.join([str(i) for i in sorted([sorted(a)[0]]+[sorted(b)[0]])]))
    
s=Solution()

print(s.minNumber([4,1,3],[5,7]))
print(s.minNumber([3,5,2,6],[3,1,7]))