class Solution:
    def checkAlmostEquivalent(self,s1,s2):
        alf=[i for i in 'abcdefghijklmnopqrstuvwxyz' if i in s1 or i in s2]
        for i in alf:
            if abs(s1.count(i)-s2.count(i))>3:
                return False
        return True

s=Solution()

print(s.checkAlmostEquivalent("abcdeef","abaaacc"))
print(s.checkAlmostEquivalent("aaaa","bccb"))