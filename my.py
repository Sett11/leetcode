class Solution:
    def reverseWords(self,s):
        return ' '.join([i for i in s.split(' ') if i][::-1])
    
s=Solution()

print(s.reverseWords("a good   example"))