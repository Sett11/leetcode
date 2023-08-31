class Solution:
    def groupAnagrams(self,a):
        s,r,i=sorted([[sorted(i),i] for i in a])+[[[''],'']],[],0
        t=[]
        while i<len(s)-1:
            if s[i][0]==s[i+1][0]:
                t.append(s.pop(i+1)[1])
                i-=1
            else:
                t.append(s.pop(i)[1])
                r.append(t)
                t=[]
                i-=1
            i+=1
        return r
    
s=Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))