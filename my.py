class Solution:
    def fizzBuzz(self,n):
        return ['FizzBuzz' if not i%5 and not i%3 else 'Fizz' if not i%3 else 'Buzz' if not i%5 else str(i) for i in range(1,n+1)]

s=Solution()

print(s.fizzBuzz(51))