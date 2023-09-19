class Solution:
    def rotatedDigits(self,n):
        c=0
        for i in range(2,n+1):
            t=str(i)
            if len([j for j in '347' if j in t]):
                continue
            else:
                k=int(''.join(['2' if j=='5' else '5' if j=='2' else '6' if j=='9' else '9' if j=='6' else j for j in t]))
                if k!=i:
                    c+=1
        return c
    
s=Solution()

print(s.rotatedDigits(10000))