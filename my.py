class Solution:
    def fairCandySwap(self,a,b):
        i=0
        while i<max(len(b),len(a)):
            q,w=a.copy(),b.copy()
            t=w.pop(i)
            q.append(t)
            c,d=sum(q),sum(w)
            n=(c+d)//2-d
            if n in q:
                return [n,t]
            i+=1

    
s=Solution()

print(s.fairCandySwap([2],[1,3]))