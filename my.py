class Solution:
    def nextGreatestLetter(self,s,t):
        return next((i for i in s if i>t),s[0])
    
s=Solution()

print(s.nextGreatestLetter(["c","f","j"],'a'))
print(s.nextGreatestLetter(["c","f","j"],'c'))