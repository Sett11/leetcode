class Solution:
    def largestInteger(self,n):
        s=str(n)
        odd=sorted([i for i in s if not int(i)&1],reverse=True)
        even=sorted([i for i in s if int(i)&1],reverse=True)
        return int(''.join([odd.pop(0) if i==0 else even.pop(0) for i in [int(i)&1 for i in s]]))
    
s=Solution()

print(s.largestInteger(65875))
print(s.largestInteger(1234))