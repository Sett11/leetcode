class Solution:
    def sortSentence(self,s):
        return ' '.join([j[1] for j in sorted([[int(i[-1:]),i[:-1]] for i in s.split(' ')])])
    
s=Solution()

print(s.sortSentence("is2 sentence4 This1 a3"))