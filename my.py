class Solution:
    def reverseWords(self,s):
        return ' '.join([i[::-1] for i in s.split(' ')])
    
s=Solution()

print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords('God Ding'))