class Solution:
    def findClosestNumber(self,a):
        if 0 in a:
            return 0
        if len(set(a))==1:
            return a[0]
        a.append(0)
        a=sorted(set(a))
        i=a.index(0)
        if i==0:
            return a[i+1]
        if i==len(a)-1:
            return a[i-1]
        if len(a)==2:
            return [i for i in a if i][0]
        a=sorted([i for i in a if i][i-1:i+1],key=abs)
        if abs(a[0])==abs(a[1]):
            return abs(a[0])
        return a[0]
    
s=Solution()

print(s.findClosestNumber([-10,-12,-54,-12,-544,-10000]))