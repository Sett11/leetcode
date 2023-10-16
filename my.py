class Solution:
    def numberOfSubstrings(self, s):
        a = b = c = -1
        n = 0
        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b':
                b = i
            else:
                c = i
            n += min(a, b, c) + 1
        return n


s = Solution()

print(s.numberOfSubstrings('aaaabc'))
