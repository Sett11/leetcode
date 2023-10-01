class Solution:
    def trimMean(self,a):
        l=len(a)
        while l-len(a)<l/100*10:
            a.remove(max(a))
            a.remove(min(a))
        return round(sum(a)/len(a),5)
    
s=Solution()

print(s.trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9 ,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))