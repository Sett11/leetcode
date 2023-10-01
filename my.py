from re import sub

class Solution:
    def reformatDate(self,s):
        mounth={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        s=s.split(' ')
        n=sub(r'\D','',s[0])
        if len(n)==1:
            n='0'+n
        return f'{s[-1]}-{mounth[s[1]]}-{n}'
    
s=Solution()

print(s.reformatDate("6th Jun 1933"))
print(s.reformatDate("20th Oct 2052"))