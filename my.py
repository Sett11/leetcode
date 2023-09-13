class Solution:
    def countSeniors(self,a):
        c=0
        for i in a:
            if int(i[11:13])>60:
                c+=1
        return c
    
s=Solution()

print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))