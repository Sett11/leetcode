fib=[1134903170, 701408733, 433494437, 267914296, 165580141, 102334155, 63245986, 39088169, 24157817, 14930352, 9227465, 5702887, 3524578, 2178309, 1346269, 832040, 514229, 317811, 196418, 121393, 75025, 46368, 28657, 17711, 10946, 6765, 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]
class Solution:
    def findMinFibonacciNumbers(self,n):
        r=[]
        for i in list(filter(lambda x:x<=n,fib)):
            while i<=n:
                r.append(i)
                if sum(r)>n:
                    r.pop()
                    break
        return len(r)
    
S=Solution()

print(S.findMinFibonacciNumbers(19))