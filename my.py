class Solution:
    def nextGreaterElement(self,a,b):
        r=[]
        for i in a:
            t=b.index(i)
            if t!=len(b)-1:
                q=b[t+1:]
                m=i
                j=0
                while j<len(q):
                    if q[j]>i:
                        m=q[j]
                        break
                    j+=1
                if m>i:
                    r.append(m)
                else:
                    r.append(-1)
            else:
                r.append(-1)
        return r

s=Solution()

print(s.nextGreaterElement([4,1,2],[1,3,4,2]))
print(s.nextGreaterElement([2,4],[1,2,3,4]))