class Solution:
    def numberOfPairs(self,a):
        c,q=0,[]
        while len(set(a))!=len(a):
            t=a.pop(0)
            if t not in a:
                q.append(t)
            else:
                a.pop(a.index(t))
                c+=1
        return [c,len(a+q)]
            
    
s=Solution()

print(s.numberOfPairs([1,3,2,1,3,2,2]))
print(s.numberOfPairs([4,98,80,3,89,14,38,98]))