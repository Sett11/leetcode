def check(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]&a[j]:
                return False
    return True

class Solution:
    def longestNiceSubarray(self,a):
        m=0
        a.append(a[-1]+1)
        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                t=a[i:j]
                if not check(t):
                    m=max(m,len(t)-1)
                    break
        return m
    
s=Solution()

print(s.longestNiceSubarray([1,3,8,48,10]))
print(s.longestNiceSubarray([135745088,609245787,16,2048,2097152]))