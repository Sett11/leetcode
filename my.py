from collections import Counter

class Solution:
    def findSpecialInteger(self,a):
        n,c,s=len(a)//4,Counter(a),set(a)
        for i in s:
            if c[i]>n:
                return i
    
S=Solution()

print(S.findSpecialInteger([1,2,2,6,6,6,6,7,10]))