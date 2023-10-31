class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_sort(a):
    for i in range(1,len(a)):
        k=i
        while k and a[k]>a[k-1]:
            a[k],a[k-1]=a[k-1],a[k]
            k-=1

class Solution:
    def insertionSortList(self,h):
        r=[]
        c=h
        while c:
            r.append(c.val)
            c=c.next
        insert_sort(r)
        c=h
        while c:
            c.val=r.pop()
            c=c.next
        return h

s=Solution()

print(s.sortList(ListNode(3,ListNode(1,ListNode(4,ListNode(4,ListNode(9,ListNode(5))))))))