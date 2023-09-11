class Solution:
    def digitCount(self,s):
        return all(s.count(str(i))==int(s[i]) for i in range(len(s)))
    
s=Solution()

print(s.digitCount('1210'))