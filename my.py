class Solution:
    def countBattleships(self,a):
        q=sum([[[i,j] for j,k in enumerate(h) if k=='X'] for i,h in enumerate(a)],[])
        r=[]
        while q:
            t=[q.pop(0)]
            i=0
            while i<len(q):
                b,c=t[-1]
                w=[[b,c+1],[b,c-1],[b+1,c],[b-1,c]]
                if q[i] in w:
                    t.append(q.pop(i))
                    i=-1
                i+=1
            r.append(t)
        return len(r)
    
s=Solution()

print(s.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".", ".","X"]]))