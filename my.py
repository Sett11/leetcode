def f(a,q):
    if len(a) <= 1:
        q.extend(a[0])
        return q

    q.extend(a.pop(0))

    if not a or not a[0]:
        return q

    for i in range(len(a)):
        q.append(a[i].pop(len(a[i])-1))
    
    if not a or not a[0]:
        return q

    q.extend(a.pop(-1)[::-1])

    if not a or not a[0]:
        return q
    
    for i in range(len(a)-1, -1, -1):
        q.append(a[i].pop(0))

    if not a or not a[0]:
        return q

    return f(a, q)


class Solution:
    def spiralOrder(self, a):
        return f(a,[])


s = Solution()

print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder([[3],[2],[1]]))
