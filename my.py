class Solution:
    def evenOddBit(self,n):
        s=bin(n)[2:]
        k=h=0
        if len(s)&1:
            for i,j in enumerate(s):
                if i&1 and j=='1':
                    h+=1
                if not i&1 and j=='1':
                    k+=1
        else:
            for i,j in enumerate(s):
                if i&1 and j=='1':
                    k+=1
                if not i&1 and j=='1':
                    h+=1
        return [k,h]
       
s=Solution()

print(s.evenOddBit(17))
print(s.evenOddBit(2))