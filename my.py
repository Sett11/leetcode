class Solution:
    def findGCD(self,a):
        n,m=min(a),max(a)
        return next(i for i in range(n,0,-1) if not n%i and not m%i)

s=Solution()

print(s.findGCD([2,5,6,9,10]))