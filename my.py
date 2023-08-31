class Solution:
    def commonChars(self,a):
        s=set(''.join(a))
        a=[list(i) for i in a]
        r=[]
        for i in s:
            if all(i in j for j in a):
                m=min([j.count(i) for j in a])
                r.extend([i]*m)
        return r
    
s=Solution()

print(s.commonChars(["bella","label","roller"]))