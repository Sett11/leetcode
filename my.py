class Solution:
    def validIPAddress(self,s):
        a,b=s.split('.'),s.split(':')
        if len(a)!=4 and len(b)!=8:
            return 'Neither'
        if len(a)==4:
            try:
                return (all([int(i)>=0 and int(i)<256 and not (len(i)>1 and i[0]=='0') for i in a]) and 'IPv4') or 'Neither'
            except:
                return 'Neither'
        else:
            try:
                return (all([len(i)<=4 for i in b]) and [int(i,16) for i in b] and 'IPv6') or 'Neither'
            except:
                return 'Neither'
    
s=Solution()

print(s.validIPAddress("172.16.254.1"))
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(s.validIPAddress("192.168@1.1"))