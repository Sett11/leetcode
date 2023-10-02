from time import time

class Solution:
    def threeConsecutiveOdds(self,a):
        return '111' in ''.join(['1' if i&1 else '0' for i in a])

class Solution():
    def threeConsecutiveOdds(self,a):
        for i in range(len(a)-2):
            if a[i]&1 and a[i+1]&1 and a[i+2]&1:
                return True
        return False
    
s=Solution()

t=time()

print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))

e=time()

0.005007743835449219

print(e-t)