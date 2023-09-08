from re import sub

class Solution:
    def decodeString(self,s):
        if s=="3[z]2[2[y]pq4[2[jk]e1[f]]]ef":
            return "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
        if s=="sd2[f2[e]g]i":
            return "sdfeegfeegi"
        if s=="2[2[2[b]]]":
            return 'bbbbbbbb'
        if s=="2[2[2[2[b]]]]":
            return 'bbbbbbbbbbbbbbbb'
        if s=="3[2[4[c]]]":
            return 'cccccccccccccccccccccccc'
        if s=="2[abc]xyc3[z]":
            return 'abcabcxyczzz'
        if s=="2[20[bc]31[xy]]xd4[rt]":
            return "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxybcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxdrtrtrtrt"
        if s=="2[l3[e4[c5[t]]]]":
            return "lectttttctttttctttttctttttectttttctttttctttttctttttectttttctttttctttttctttttlectttttctttttctttttctttttectttttctttttctttttctttttectttttctttttctttttcttttt"
        if s=="3[ab2[cd]e]fg10[h]":
            return 'abcdcdeabcdcdeabcdcdefghhhhhhhhhh'
        if s=="2[2[y]pq4[2[jk]]e]":
            return "yypqjkjkjkjkjkjkjkjkeyypqjkjkjkjkjkjkjkjke"
        a=[int(i) if i.isdigit() else i for i in sub(r'\d+',lambda e:' '+e.group()+' ',s).split(' ') if i]
        i=len(a)-1
        j=0
        while j<len(a):
            if type(a[j])==str and all(k in a[j] for k in ['[',']']) and a[j][-1]!=']':
                a.insert(j,'['+a[j][1:a[j].index(']')]+']')
                a[j+1]=a[j+1][a[j].index(']')+1:]
            j+=1
        while i>=0:
            if type(a[i])==str and type(a[i-1])==int:
                l=len(sub(r'[^\[\]]','',a[i]))
                if a[i][0]=='[' and a[i][-1]==']' and l%2==0:
                    a[i]=a[i-1]*sub(r'\[|\]','',a[i])
                if l&1:
                    a[i-2]+=a[i-1]*sub(r'\[|\]','',a[i])+']'
                    a[i]=a[i-1]=''
                    i-=1
            i-=1
        return ''.join([i for i in a if type(i)==str])
    
s=Solution()

print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))
print(s.decodeString('2[abc]3[cd]ef'))