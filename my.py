class Solution:
    def checkPossibility(self,a):
        b=sorted(a)
        for i in range(len(a)):
            t=a.pop(i)
            g=b.index(t)
            b.pop(g)
            if a==b:
                return True
            else:
                a.insert(i,t)
                b.insert(g,t)
        return False
    
s=Solution()

print(s.checkPossibility([4,2,3]))
print(s.checkPossibility([-1,4,2,3]))