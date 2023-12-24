def f(s):
    return s.count(min(s))

class Solution:
    def numSmallerByFrequency(self,a,b):
        a,b=list(map(f,a)),sorted(map(f,b))
        for i in range(len(a)):
            a[i]=len(list(filter(lambda x:x>a[i],b)))
        return a
    
S=Solution()

print(S.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))