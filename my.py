class Solution:
    def mostWordsFound(self,a):
        return max((len(i.split(' ')) for i in a))
    
s=Solution()

print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))