class Solution:
    def shiftingLetters(self,s,a):
        alf='abcdefghijklmnopqrstuvwxyz'
        l=len(s)
        n=sum(a)
        r=list(s)
        for i in range(l):
            if i:
                n-=a[i-1]
            r[i]=alf[(alf.index(r[i])+n)%26]
        return ''.join(r)
        
    
s=Solution()

print(s.shiftingLetters('abc',[3,5,9]))
print(s.shiftingLetters('aaa',[1,2,3]))