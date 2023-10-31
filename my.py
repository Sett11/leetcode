class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self,h,n):
        c=h
        while c and c.next:
            if c.next.val==n:
                c.next=c.next.next
            else:
                c=c.next
        if h and h.val==n:
            h=h.next
        return h

s=Solution()

print(s.removeElements(ListNode(3,ListNode(1,ListNode(4,ListNode(4,ListNode(9,ListNode(5)))))),3))