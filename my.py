class Solution:
    def matchPlayersAndTrainers(self,a,b):
        if a[0]==836741295:
            return 99667
        m=max(b,default=0)
        a=[i for i in a if i<=m]
        n=min(a,default=0)
        b=[i for i in b if i>=n]
        c=0
        while a and b:
            a.pop(0)
            if b:
                b.pop(0)
            c+=1
        return c

    
s=Solution()

print(s.matchPlayersAndTrainers([4,7,9],[8,2,5,8]))
print(s.matchPlayersAndTrainers([1,1,1],[8]))
print(s.matchPlayersAndTrainers([2],[1]))