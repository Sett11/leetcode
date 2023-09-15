class Solution:
    def countElements(self,a):
        m,n=min(a),max(a)
        return len([i for i in a if m<i<n])
    
s=Solution()

print(s.countElements([11,7,2,15]))
print(s.countElements([-3,3,3,90]))