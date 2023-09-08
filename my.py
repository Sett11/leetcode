class Solution:
    def intToRoman(self,n):
        o=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        s=''
        for i in o:
            while n>=i[0]:
                n-=i[0]
                s+=i[1]
        return s
    
s=Solution()

print(s.intToRoman(1994))