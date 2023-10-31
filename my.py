class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self,h):
        c=h
        while c and c.next:
            if c.val==c.next.val:
                c.next=c.next.next
            else:
                c=c.next
        return h

s=Solution()

print(s.deleteDuplicates(ListNode(3,ListNode(1,ListNode(4,ListNode(4,ListNode(9,ListNode(5))))))))