class Solution:
    def hammingDistance(self,a,b):
        a,b=bin(a)[2:],bin(b)[2:]
        x,y=len(a),len(b)
        if x<4:
            a='0'*(4-x)+a
        if y<4:
            b='0'*(4-y)+b
        x,y=len(a),len(b)
        if x<y:
            a='0'*(y-x)+a
        if y<x:
            b='0'*(x-y)+b
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        return c
    
s=Solution()

print(s.hammingDistance(1,4))