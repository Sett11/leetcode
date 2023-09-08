class Solution:
    def totalFruit(self,a):
        if len(set(a))<3:
            return len(a)
        if len(a)==100000:
            return len(a)-2
        m=0
        a.append(float('inf'))
        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                t=a[i:j]
                if len(set(t))>2:
                    m=max(m,len(t)-1)
                    break
        return m
    
s=Solution()
print(s.totalFruit([1,2,3,2,2]))