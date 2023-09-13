class Solution:
    def check(self,a):
        b=sorted(a)
        for i in range(len(a)):
            if a[i:]+a[:i]==b:
                return True
        return False
    
s=Solution()

print(s.check([2,5,1,3,4,7]))
print(s.check([3,4,5,1,2]))