class Solution:
    def firstPalindrome(self,a):
        try:
            return next(i for i in a if i==i[::-1])
        except:
            return ''
    
s=Solution()

print(s.firstPalindrome(["def","ghi"]))