class NumArray:

    def __init__(self, a):
        self.a = a

    def sumRange(self, l, r):
        return sum(self.a[l:r+1])


s = NumArray([-2, 0, 3, -5, 2, -1])

print(s.sumRange(0, 2))
print(s.sumRange(2, 5))
print(s.sumRange(0, 5))
