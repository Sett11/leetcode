class Solution:
    def twoOutOfThree(self,a,b,c):
        s=set(a+b+c)
        r=[]
        for i in s:
            if len([j for j in [i in a, i in b, i in c] if j])>1:
                r.append(i)
        return r
    
s=Solution()

print(s.twoOutOfThree([1,1,3,2],[2,3],[3]))