class Solution:
    def calPoints(self,a):
        r=[]
        for i in a:
            if i.isdigit() or i[1:].isdigit():
                r.append(int(i))
            if i=='+':
                r.append(r[-1]+r[-2])
            if i=='C':
                r.pop()
            if i=='D':
                r.append(r[-1]*2)
        return sum(r)
    
s=Solution()

print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))