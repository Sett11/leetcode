class Solution:
    def maxPower(self,s):
        if len(set(s))==1:
            return len(s)
        s+='&&'
        r=[]
        for i in range(len(s)):
            c=s[i]
            for j in range(i+1,len(s)):
                if len(set(c))==1:
                    c+=s[j]
                else:
                    r.append(c[:-1])
                    break
        return len(sorted(r,key=len,reverse=True)[0])

s=Solution()

print(s.maxPower('abbcccddddeeeeedcba'))
print(s.maxPower('aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz'))