class Solution:
    def isCircularSentence(self,s):
        a=s.split(' ')
        for i in range(len(a)-1):
            if a[i][-1]!=a[i+1][0]:
                return False
        return s[0]==s[-1]
    
s=Solution()

print(s.isCircularSentence("leetcode exercises sound delightful"))
print(s.isCircularSentence("Leetcode is cool"))