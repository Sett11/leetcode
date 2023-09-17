class Solution:
    def toGoatLatin(self,s):
        a=s.split(' ')
        for i in range(len(a)):
            if a[i][0].lower() in 'aioue':
                a[i]+='ma'+'a'*(i+1)
            else:
                a[i]=a[i][1:]+a[i][0]+'ma'+'a'*(i+1)
        return ' '.join(a)
    
s=Solution()

print(s.toGoatLatin("The quick brown fox jumped over the lazy dog"))