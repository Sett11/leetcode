class Solution:
    def longestConsecutive(self,b):
        a=['&']+sorted(set(b))+['&']
        m=1
        r=m
        for i in range(2,len(a)-1):
            if a[i]-a[i-1]==1:
                m+=1
                r=max(r,m)
            else:
                m=1
        return r if b else 0

    
S=Solution()

print(S.longestConsecutive([100,4,200,1,3,2]))
print(S.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(S.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,- 3]))