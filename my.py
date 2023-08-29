class Solution:
    def frequencySort(self,s):
        o={}
        for i in set(s):
            o[i]=s.count(i)
        return ''.join(sorted(s,key=lambda e:(o[e],-ord(e)),reverse=True))
    
s=Solution()

print(s.frequencySort('loveleetcode'))