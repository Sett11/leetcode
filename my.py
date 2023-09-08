class Solution:
    def increasingTriplet(self,a):
        b,c=[float('inf')]*2
        for i in a:
            if i<=b:
                b=i
            elif i<=c:
                c=i
            elif i>c:
                return True
        return False

s=Solution()

print(s.increasingTriplet([2,1,5,0,4,6]))
print(s.increasingTriplet([20,100,10,12,5,13]))