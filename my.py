from itertools import product as p
class Solution:
    def letterCombinations(self,s):
        o={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return [''.join(j) for j in p(*[o[i] for i in s]) if j]

s=Solution()

print(s.letterCombinations(''))