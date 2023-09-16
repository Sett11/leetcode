def shange(a):
    for i in [0,1]:
        t=a[i].split(':')
        a[i]=float(t[0]+'.'+t[1])
    return a

class Solution:
    def haveConflict(self,a,b):
        a,b=shange(a),shange(b)
        return True if (b[1]>=a[0] and b[1]<=a[1]) or b[0]==a[1] or (a[1]>=b[0] and a[1]<=b[1]) else False
    
s=Solution()

print(s.haveConflict(["01:00","02:00"],["01:20","03:00"]))