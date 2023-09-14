class Solution:
    def findLengthOfLCIS(self,a):
        m=0
        t=[a.pop(0)]
        while a:
            if a and t[-1]<a[0]:
                t.append(a.pop(0))
            else:
                m=max(len(t),m)
                t=[a.pop(0)]
        m=max(len(t),m)
        return m
    
s=Solution()

print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([1,2,3,4,5]))