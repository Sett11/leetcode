class Solution:
    def numJewelsInStones(self,s,t):
        c=0
        for i in s:
            c+=t.count(i)
        return c
    
s=Solution()

print(s.numJewelsInStones("aA","aAAbbbb"))