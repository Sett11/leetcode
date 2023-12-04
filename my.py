from re import sub
from collections import Counter

class Solution:
    def shortestCompletingWord(self,s,a):
        b,c=Counter(sub(r'[^A-z]','',s.lower())),sorted(map(lambda x:[x,Counter(x.lower())],a),key=lambda x:len(x[0]))
        
        for i,j in c:
            if all(k in i and j[k]>=b[k] for k in b):
                return i
    

S=Solution()

print(S.shortestCompletingWord("1s3 456",["looks","pest","stew","show"]))