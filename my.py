from re import sub

class Solution:
    def sortJumbled(self,a,b):
        o={}
        for i,j in enumerate(a):
            o[str(i)]=str(j)
        return [i[1] for i in sorted(enumerate(b),key=lambda u:(int(sub(r'.',lambda e:o[e.group()],str(u[1]))),u[0]))]

s=Solution()

print(s.sortJumbled([8,9,4,0,2,1,3,5,7,6],[991,338,38]))
print(s.sortJumbled([0,1,2,3,4,5,6,7,8,9],[789,456,123]))