class Solution:
    def numSimilarGroups(self,s):
        r=[]
        while s:
            t=[s.pop(0)]
            i=0
            while i<len(s):
                k=0
                while k<len(t):
                    if len([h for h in [t[k][j]==s[i][j] for j in range(len(s[i]))] if not h])<=2:
                        t.append(s.pop(i))
                        i=-1
                        break
                    k+=1
                i+=1
            r.append(t)
        return len(r)
    
s=Solution()

print(s.numSimilarGroups(["tars","rats","arts","star"]))
print(s.numSimilarGroups(["omv","ovm"]))
print(s.numSimilarGroups(["kccomwcgcs", "socgcmcwkc", "sgckwcmcoc", "coswcmcgkc", "cowkccmsgc", "cosgmccwkc", "sgmkwcccoc", "coswmccgkc", "kowcccmsgc", "kgcomwcccs"]))