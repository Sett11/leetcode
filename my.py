class Solution:
    def frequencySort(self,a):
        return sorted(a,key=lambda e:(a.count(e),-e))
    
s=Solution()

print(s.frequencySort([1,1,2,2,2,3]))
print(s.frequencySort([2,3,1,3,2]))