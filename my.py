from re import sub
class Solution:
    def sortByBits(self,a):
        return [j[1] for j in sorted([[len(sub(r'[^1]','',bin(i))),i] for i in a],key=lambda e:(e[0],e[1]))]
    
s=Solution()

print(s.sortByBits([0,1,2,3,4,5,6,7,8]))