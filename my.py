class Solution:
    def diagonalSum(self,a):
        return sum([a[i][len(a[0])-1-i]+a[i][i] for i in range(len(a))])-(a[len(a)//2][len(a[0])//2] if len(a)&1 else 0)
    
s=Solution()

print(s.diagonalSum([
            [ 1 ,2, 3 ],
              [4, 5,6 ],
              [ 7 ,8, 9 ]]))
print(s.diagonalSum([
            [ 1 ,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1 ]]))