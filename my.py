class Solution:
    def isAcronym(self,a,s):
        return [i[0] for i in a]==list(s)
    
s=Solution()

print(s.isAcronym(["alice","bob","charlie"],"abc"))