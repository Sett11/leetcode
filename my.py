class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self,h):
        c=h
        r=[]
        while c and c.next:
            if c.val==c.next.val:
                r.append(c.val)
            c=c.next
        c=h
        while c and c.next:
            if c.next.val in r:
                c.next=c.next.next
            else:
                c=c.next
        if h and h.val in r:
            h=h.next
        return h

s=Solution()

print(s.deleteDuplicates(ListNode(3,ListNode(1,ListNode(4,ListNode(4,ListNode(9,ListNode(5))))))))