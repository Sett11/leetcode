class Solution:
    def findAndReplacePattern(self, a, t):
        r = []
        for i in a:
            if len(i) == len(t) and all(i.count(i[j]) == t.count(t[j]) and i.index(i[j]) == t.index(t[j]) for j in range(len(t))):
                r.append(i)
        return r


s = Solution()

print(s.findAndReplacePattern(
    ["abc", "deq", "mee", "aqq", "dkd", "ccc"], 'add'))
