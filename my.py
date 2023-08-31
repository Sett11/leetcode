class Solution:
    def lengthOfLastWord(self,s):
        return len([i for i in s.split(' ') if i][-1])

s = Solution()

print(s.lengthOfLastWord("   fly me   to   the moon  "))