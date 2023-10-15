from collections import Counter
from bisect import insort


class Solution:
    def findWinners(self, a):
        s = set(sum(a, []))
        b = Counter([i[1] for i in a])
        r = []
        for i in b:
            if b[i] == 1:
                insort(r, i)
        return [sorted(s.difference(b)), r]


s = Solution()

print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [
      5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
