from re import sub

class Solution:
    def duplicateZeros(self,a):
        l=len(a)
        b=[int(j) for j in list(sub(r'0','00',''.join([str(i) for i in a])))]
        a.clear()
        a.extend(b[:l])
    
s=Solution()
arr=[1,0,2,3,0,4,5,0]
print(arr)
s.duplicateZeros(arr)
print(arr)