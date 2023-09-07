def wrap(m):
    a=[[0]*3 for _ in range(3)]
    for i in range(len(m)):
        if i&1:
            a[m[i][0]][m[i][1]]='O'
        else:
            a[m[i][0]][m[i][1]]='X'
    return a

def f(a):
    r,i=[],0
    while i<len(a):
        r.append(a[i][i])
        i+=1
    return r

class Solution:
    def tictactoe(self,m):
        a=wrap(m)
        r=[j for j in [list(i) for i in zip(*a)]+a+[f(a)]+[f([i[::-1] for i in a])] if len(set(j))==1 and j[0]]
        return 'Draw' if not r and len(m)==9 else 'Pending' if not r else 'A' if r[0][0]=='X' else 'B'
    
s=Solution()

print(s.tictactoe([[0,0],[1,1]]))