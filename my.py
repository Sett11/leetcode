from re import sub,search

class Solution:
    def largeGroupPositions(self,s):
        a=[i for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',s).split(' ') if len(i)>2]
        r=[]
        for i in a:
            t=list(search(i,s).span())
            t[-1]-=1
            s=s.replace(i,'&'*len(i),1)
            r.append(t)
        return r
    
s=Solution()

print(s.largeGroupPositions('abcdddeeeeaabbbcd'))
print(s.largeGroupPositions('nnnhaaannnm'))
print(s.largeGroupPositions('llleeeeemmkkkkeeeehh'))