class Solution:
    def countSegments(self,s):
        return len([i for i in s.split(' ') if i])
    
s=Solution()

print(s.countSegments("Hello, my name is John"))
print(s.countSegments("    , , , ,        a, eaefa"))
print(s.countSegments(''))