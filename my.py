class Solution:
    def minSumOfLengths(self,a,t):
        if t in a and a.count(t)>1:
             return 2
        r=[]
        i=0
        while i<len(a):
            q=[a[i]]
            for j in range(i+1,len(a)):
                if sum(q)==t and (i>=r[-1][2] if r else j):
                    r.append([len(q),i,j])
                    break
                q.append(a[j])
            i+=1
        return [i[0] for i in r]#-1 if len(r)<2 else sum(sorted(r)[:2])
    
s=Solution()

print(s.minSumOfLengths([3,1,1,1,5,1,2,1],3))
print(s.minSumOfLengths([2,1,3,3,2,3,1],6))
print(s.minSumOfLengths([1,1,1,2,2,2,4,4],6))