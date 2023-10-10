class Solution:
    def equalPairs(self,a):
        b=[list(i) for i in zip(*a)]
        c=0
        for i in a:
            for j in b:
                if i==j:
                    c+=1
        return c
    
s=Solution()

print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))