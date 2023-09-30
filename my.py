class Solution:
    def findOcurrences(self,t,f,s):
        a=t.split(' ')
        r=[]
        for i in range(len(a)-2):
            if a[i]==f and a[i+1]==s:
                r.append(a[i+2])
        return r
    
s=Solution()

print(s.findOcurrences("alice is a good girl she is a good student",'a','good'))