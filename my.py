from re import sub

class Solution:
    def mostCommonWord(self,s,a):
        t=[i for i in sub(r'[^A-z ]',' ',s.lower()).split(' ') if i not in a and i]
        r=set(t)
        o={}
        m=0
        for i in r:
            n=t.count(i)
            o[n]=i
            m=max(m,n)
        return o[m]
    
s=Solution()

print(s.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.',["hit"]))
print(s.mostCommonWord("a,a,a,a,b,b,b,c,c",["a"]))
print(s.mostCommonWord("a.",[]))