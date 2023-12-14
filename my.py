class Solution:
    def powerfulIntegers(self,x,y,n):
        a=sorted(x**i+y**j for i in range(35) for j in range(25))
        for i in range(len(a)):
            if a[i]>n:
                return list(set(a[:i]))
            if a[i]==n:
                return list(set(a[:i+1]))
        return list(set(a))

    
S=Solution()

print(S.powerfulIntegers(3,5,15))
print(S.powerfulIntegers(1,1,40000))