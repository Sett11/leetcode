class Solution:
    def sortArrayByParity(self,a):
        b,c=[],[]
        [c.append(i) if i&1 else b.append(i) for i in a]
        return b+c
    
s=Solution()

print(s.sortArrayByParity([3,1,2,4]))