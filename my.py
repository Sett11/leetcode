class Solution:
    def decodeMessage(self,k,s):
        a=[]
        alf=[chr(i) for i in range(97,123)]
        for i in k:
            if i not in a and i!=' ':
                a.append(i)
        o=dict(zip(a,alf))
        return ''.join([o[i] if i in alf else i for i in s])
    
s=Solution()

print(s.decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))