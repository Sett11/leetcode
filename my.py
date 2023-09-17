class Solution:
    def arrangeWords(self,s):
        return ' '.join(sorted(s.lower().split(' '),key=len)).capitalize()
    
s=Solution()

print(s.arrangeWords("Keep calm and code on"))
print(s.arrangeWords("To be or not to be"))