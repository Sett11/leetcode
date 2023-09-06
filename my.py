class Solution:
    def thirdMax(self,a):
        r=sorted(set(a),reverse=True)
        return max(r) if len(r)<3 else r[2]

    
s=Solution()

print(s.thirdMax([1,1,2]))