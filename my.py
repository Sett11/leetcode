class Solution:
    def numberOfLines(self,a,s):
        b=[a[ord(i)-97] for i in s]
        c=i=k=0
        while i<len(b):
            if (c+b[i])<=100:
                c+=b[i]
            else:
                k+=1
                c=0
                i-=1
            i+=1
        return [k+1,c]
    
s=Solution()

print(s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10. ,10,10,10],'bbbcccdddaaa'))
print(s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],'abcdefghijklmnopqrstuvwxyz'))