class Solution:
    def restoreString(self,s,a):
        r=[]
        for i in range(len(a)):
            r.append([a[i],s[i]])
        return ''.join(list(map(lambda e:e[1],sorted(r))))
    
s=Solution()

print(s.restoreString("codeleet",[4,5,6,7,0,2,1,3]))