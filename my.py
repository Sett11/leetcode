class Solution:
    def findSubarrays(self,a):
        r=[sum([a[i],a[i+1]]) for i in range(len(a)-1)]
        return len(set(r))!=len(r)
    
s=Solution()

print(s.findSubarrays([4,2,4]))