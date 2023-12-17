class Solution:
    def countOperations(self,a,b):
        c=0
        while a and b:
            if a>=b:
                a-=b
            else:
                b-=a
            c+=1
        return c

S=Solution()

print(S.countOperations(2,3))