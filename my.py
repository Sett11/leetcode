class Solution:
    def maximumValue(self,a):
        return max([int(i) if all(j.isdigit() for j in i) else len(i) for i in a])
    
s=Solution()

print(s.maximumValue(["alic3","bob","3","4","00000"]))