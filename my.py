class Solution:
    def arrayRankTransform(self,a):
        o={}
        l=list(set(a))
        l.sort()
        for i in range(len(l)):
            o[l[i]]=i
        for i in range(len(a)):
            a[i]=o[a[i]]+1
        return a

s=Solution()

print(s.arrayRankTransform([40,10,20,30]))