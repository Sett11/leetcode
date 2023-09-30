class Solution:
    def maxDivScore(self,a,d):
        m=0
        r=[]
        for i in d:
            t=len([j for j in a if j%i==0])
            m=max(m,t)
            r.append([t,i])
        return min([i[1] for i in r if i[0]==m])
            
    
s=Solution()

print(s.maxDivScore([20,14,21,10],[5,7,5]))
print(s.maxDivScore([4,7,9,3,9],[5,2,3]))
print(s.maxDivScore([73,13,20,6],
[56,75,83,26,24,53,56,61]))