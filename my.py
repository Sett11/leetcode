class Solution:
    def countMatches(self,a,k,v):
        c=0
        for i in a:
            if k=='type' and i[0]==v or k=='color' and i[1]==v or k=='name' and i[2]==v:
                c+=1
        return c
    
s=Solution()

print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],'type','phone'))