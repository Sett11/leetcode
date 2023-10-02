class Solution:
    def truncateSentence(self,s,c):
        return ' '.join(s.split(' ')[:c])
    
s=Solution()

print(s.truncateSentence("Hello how are you Contestant",4))