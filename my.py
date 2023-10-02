class Solution():
    def threeConsecutiveOdds(self,a):
        for i in range(len(a)-2):
            if a[i]&1 and a[i+1]&1 and a[i+2]&1:
                return True
        return False
    
s=Solution()


print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))