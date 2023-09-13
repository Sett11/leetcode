from re import sub
class Solution:
    def areNumbersAscending(self,s):
        return eval('<'.join([i for i in sub(r'\D',' ',s).split(' ') if i]))
    
s=Solution()

print(s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(s.areNumbersAscending("hello world 5 x 5"))