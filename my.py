class Solution:
    def luckyNumbers (self,a):
        b=[max(i) for i in zip(*a)]
        c=[min(i) for i in a]
        return list(set(b).intersection(set(c)))

s=Solution()

print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(s.luckyNumbers([[7,8],[1,2]]))