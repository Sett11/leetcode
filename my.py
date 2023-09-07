class Solution:
    def longestPalindrome(self,s):
        q=set()
        for i in s:
            if i not in q:
                q.add(i)
            else:
                q.remove(i)
        return len(s)-len(q)+bool(s and q)
    
s=Solution()

print(s.longestPalindrome('abccccdd'))
print(s.longestPalindrome('abcckkkkkkdpkkkkwwwwwwoooooooo'))