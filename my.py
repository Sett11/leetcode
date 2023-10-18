from collections import Counter as c


class Solution:
    def isGood(self, a):
        b = c(a)
        m = max(a)
        if len(a)-1 != m:
            return False
        for i in range(1, m+1):
            if (i != m and b[i] != 1) or (i == m and b[i] != 2):
                return False
        return True


s = Solution()

print(s.isGood([1, 2, 3, 3]))
