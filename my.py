class Solution:
    def isPrefixString(self,s,a):
        t=a.pop(0)
        while a:
            if t==s:
                return True
            if not s.startswith(t):
                return False
            t+=a.pop(0)
        return t==s

s = Solution()

print(s.isPrefixString('iloveleetcode',["i","love","leetcode","apples"]))
print(s.isPrefixString('z',['z']))