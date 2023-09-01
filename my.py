def f(a):
    if len(a)==1:
        return a[0]
    c=0
    r=[]
    for i in range(0,len(a),2):
        if c%2==0:
            r.append(min(a[i],a[i+1]))
            c+=1
        else:
            r.append(max(a[i],a[i+1]))
            c+=1
    return f(r)

class Solution:
    def minMaxGame(self,a):
        return f(a)
    
s=Solution()

print(s.minMaxGame([1,3,5,2,4,8,2,2]))