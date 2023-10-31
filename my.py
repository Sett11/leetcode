class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self,h):
        r=[]
        c=h
        while c:
            r.append(c.val)
            c=c.next
        r.sort(reverse=True)
        c=h
        while c:
            c.val=r.pop()
            c=c.next
        return h

s=Solution()

print(s.sortList(ListNode(3,ListNode(1,ListNode(4,ListNode(4,ListNode(9,ListNode(5))))))))