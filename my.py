from collections import Counter

class Solution:
    def singleNonDuplicate(self,a):
        a=Counter(a)
        for i in a:
            if a[i]==1:
                return i

s=Solution()

print(s.singleNonDuplicate([3,3,7,7,10,11,11]))