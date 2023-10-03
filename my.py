class Solution:
    def secondHighest(self,s):
        try:
            return sorted({int(i) for i in s if i.isdigit()},reverse=True)[1]
        except:
            return -1

s=Solution()

print(s.secondHighest('dfa12321afd'))
print(s.secondHighest('ck077'))