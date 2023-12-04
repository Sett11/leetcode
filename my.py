class Solution:
    def generateParenthesis(self,n):
        r=[]

        def f(s,n,m):
            if [m,n]==[0,0]:
                r.append(s)
                return
            if not n:
                r.append(s+')'*m)
                return
            if n<m:
                f(s+')',n,m-1)
            f(s+'(',n-1,m)
        
        f('',n,n)

        return r


    
S=Solution()

print(S.generateParenthesis(8))