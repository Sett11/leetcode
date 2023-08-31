class Solution:
    def prefixCount(self,a,p):
        return len([i for i in a if i.lstrip().startswith(p)])

s = Solution()

print(s.prefixCount(["pay"," attention ","practice"," attend "],'at'))