def check(a, n):
    return all(a[i] % 2 != a[i+1] % 2 and a[i] <= n and a[i+1] <= n for i in range(len(a)-1))


class Solution:
    def longestAlternatingSubarray(self, a, n):
        m = 0
        l = len(a)
        for i in range(l):
            if a[i] % 2 == 0 and a[i] <= n:
                for j in range(i+1, l+1):
                    t = a[i:j]
                    if check(t, n):
                        m = max(m, len(t))
                    else:
                        break
        return m


s = Solution()

print(s.longestAlternatingSubarray([3, 2, 5, 4], 5))
