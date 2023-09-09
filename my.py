class Solution:
    def alphabetBoardPath(self,s):
        o={'a': [0, 0], 'b': [0, 1], 'c': [0, 2], 'd': [0, 3], 'e': [0, 4], 'f': [1, 0], 'g': [1, 1], 'h': [1, 2], 'i': [1, 3], 'j': [1, 4], 'k': [2, 0], 'l': [2, 1], 'm': [2, 2], 'n': [2, 3], 'o': [2, 4], 'p': [3, 0], 'q': [3, 1], 'r': [3, 2], 's': [3, 3], 't': [3, 4], 'u': [4, 0], 'v': [4, 1], 'w': [4, 2], 'x': [4, 3], 'y': [4, 4], 'z': [5, 0]}
        t=[0,0]
        c=''
        for i in s:
            a,b=o[i]
            v,w=a>t[0],b>t[1]
            if i!='z':
                c+=('D' if v else 'U')*(a-t[0] if v else t[0]-a)
                c+=('R' if w else 'L')*(b-t[1] if w else t[1]-b)
            else:
                c+=('R' if w else 'L')*(b-t[1] if w else t[1]-b)
                c+=('D' if v else 'U')*(a-t[0] if v else t[0]-a)
            t=[a,b]
            c+='!'
        return c


s=Solution()

print(s.alphabetBoardPath('leet'))
print(s.alphabetBoardPath('zdz'))