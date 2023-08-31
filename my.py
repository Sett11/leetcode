class Solution:
    def separateDigits(self,a):
        return sum([[int(j) for j in list(str(i))] for i in a],[])
    
s=Solution()

print(s.separateDigits([13,25,83,77]))