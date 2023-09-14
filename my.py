class Solution:
    def isOneBitCharacter(self,a):
        s=''.join([str(i) for i in a[:-1]]).replace('11','').replace('10','').replace('0','')
        return not s and not a[-1]
    
s=Solution()

print(s.isOneBitCharacter([0,0]))
print(s.isOneBitCharacter([1,1,0,0]))