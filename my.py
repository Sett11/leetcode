class Solution:
    def canVisitAllRooms(self,a):
        s=set(a[0])
        a[0]=0

        for i in range(1,len(a)):
            if i in s:
                if a[i]:
                    s.update(a[i])
                    for j in a[i]:
                        if a[j]:
                            s.update(a[j])
                            a[j]=0
                a[i]=0
                
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
        c=s.copy()     
        for i in c:
            if a[i]:
                s.update(a[i])
                a[i]=0
       
        return all(not i or j in s for j,i in enumerate(a))


S=Solution()

print(S.canVisitAllRooms([[1],[2],[3],[]]))
print(S.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(S.canVisitAllRooms([[7,16,8,19],[10],[9,11],[3,14,16,19],[8,10,19,1,7],[13,5,10, 15,4],[6,13],[14,11,12,18],[3],[17,9],[1,2,6,9],[12,2],[4] ,[2,13,17],[17],[],[11,15],[3,5],[15,18,5],[7,18,1]]))
print(S.canVisitAllRooms([[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5] ,[2,3,1]]))