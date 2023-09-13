class Solution:
    def myAtoi(self, s):
        c = ''
        a = [-2**31, 2147483647]
        v = False
        for i in s.lstrip():
            if (i not in ['-', '+'] and not i.isdigit()) or (not i.isdigit() and v):
                break
            c += i
            v = True
        try:
            n = int(c)
            return a[0] if n < a[0] else a[1] if n > a[1] else n
        except:
            return 0


s = Solution()

print(s.myAtoi("4193 with words"))
print(s.myAtoi("-419"))
print(s.myAtoi("    with words 4193 "))
print(s.myAtoi("+1"))
print(s.myAtoi("-5-"))
