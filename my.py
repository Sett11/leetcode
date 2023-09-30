class Solution:
    def countDistinctIntegers(self,a):
        return len(set(list(map(lambda e:int(str(e)[::-1]),a))+a))

s=Solution()

print(s.countDistinctIntegers([1,13,10,12,31]))