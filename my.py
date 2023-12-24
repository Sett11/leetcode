from collections import defaultdict

class Solution:
    def countLargestGroup(self,n):
        d,m=defaultdict(dict),0
        for i in range(1,n+1):
            t=sum(map(int,str(i)))
            if t not in d:
                d[t]=1
            else:
                d[t]+=1
            m=max(d[t],m)
        return len(list(filter(lambda x:x[1]==m,d.items())))

    
S=Solution()

print(S.countLargestGroup(13))