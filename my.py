class Solution:
    def xorOperation(self,n,k):
        i=k
        s=''
        c=1
        while c<=n:
            s+=f'{i}^'
            i+=2
            c+=1
        return eval(s[:-1])
    
s=Solution()

print(s.xorOperation(4,3))
print(s.xorOperation(5,0))