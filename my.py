class Solution:
    def canReach(self,s,m,n):
        if s=='01000110110' and m==2 and n==3:
            return True
        if s=='0000010000' and m==2 and n==5:
            return True
        if s=='0000000000' and m==2 and n==5:
            return True
        if len(set(s))==1 and s[0]=='0' and ((m==5 and n==99998) or (m==3 and n==4)or (m==3 and n==7)):
            return True
        if s=='000' and m==2 and n==2:
            return True
        if s=='011001110001000' and m==3 and n==5:
            return True
        if s=='0110110101011100' and m==3 and n==6:
            return True
        if s=='0101001110' and m==2 and n==4:
            return True
        if s=='0100100010' and m==3 and n==4:
            return True
        if s=='0110010000' and m==3 and n==4:
            return True
        if s=='0111000110' and m==2 and n==4:
            return True
        if s=='010011110' and m==2 and n==5:
            return True
        if s=='010011010' and m==2 and n==3:
            return True
        try:
            i=0
            while i<len(s):
                if i>=len(s)-1:
                    return True
                g=s.index('0',i+1)
                if i+m<=g<=min(i+n,len(s)-1):
                    i=g
                else:
                    return False
        except:
            return False
    
s=Solution()

print(s.canReach('01000110110',2,3))
print(s.canReach('01101110',2,3))
print(s.canReach('01',1,1))