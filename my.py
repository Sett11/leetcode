class Solution:
    def bestHand(self,a,b):
        if len(set(b))==1:
            return 'Flush'
        if [i for i in a if a.count(i)>2]:
            return 'Three of a Kind'
        if [i for i in a if a.count(i)>1]:
            return 'Pair'
        return 'High Card'
    
s=Solution()

print(s.bestHand([13,2,3,1,9],["a","a","a","a","a"]))
print(s.bestHand([4,3,2,4,4],["d","a","a","b","c"]))
print(s.bestHand([10,10,7,7,4],["d","a","a","b","c"]))