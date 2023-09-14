class Solution:
    def checkValidGrid(self, a):
        m = len(a)
        i = j = n = 0
        while n != m*m-1:
            t = [k for k in [[i+2, j+1], [i-2, j-1], [i-2, j+1], [i+2, j-1], [i+1, j+2], [i-1, j-2],
                             [i-1, j+2], [i+1, j-2]] if 0 <= k[0] < m and 0 <= k[1] < m and a[k[0]][k[1]] == n+1]
            if not t:
                return False
            n += 1
            i, j = t[0]
        return not a[0][0]


s = Solution()

print(s.checkValidGrid([[0, 11, 16, 5, 20],
                        [17, 4, 19, 10, 15],
                        [12, 1, 8, 21, 6],
                        [3, 18, 23, 14, 9],
                        [24, 13, 2, 7, 22]]))
print(s.checkValidGrid([[8,3,6],
                        [5,0,1],
                        [2,7,4]]))
