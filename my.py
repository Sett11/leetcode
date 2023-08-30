class Solution:
    def isHappy(self,n):
        a=[]
        while 1:
            n=sum([int(i)**2 for i in str(n)])
            if n==1:
                return True
            if n in a:
                return False
            a.append(n)
    
s=Solution()

print(s.isHappy(19))
print(s.isHappy(2))