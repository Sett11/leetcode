class Solution:
    def setZeroes(self,m):
        a=[q for q in [[[j,i] for i,k in enumerate(h) if not k] for j,h in enumerate(m)] if q]
        if not a:
            return m
        q=[]
        [q.extend(i) for i in a]
        a=q
        w=m.copy()
        for i in a:
            w[i[0]]=[0]*len(w[i[0]])
        w=[list(i) for i in zip(*w)]

        for i in a:
            w[i[1]]=[0]*len(w[i[1]])
        
        w=[list(i) for i in zip(*w)]
        m.clear()
        for i in w:
            m.append(i)
        
        return m

s=Solution()

print(s.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))
print(s.setZeroes([[1],[2],[3],[0]]))
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))