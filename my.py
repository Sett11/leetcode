class Solution:
    def findWords(self,w):
        a,b,c='qwertyuiop','asdfghjkl','zxcvbnm'
        return [i for i in w if all(j.lower() in a for j in i) or all(j.lower() in b for j in i) or all(j.lower() in c for j in i)]

s=Solution()

print(s.findWords(["Hello","Alaska","Dad","Peace"]))