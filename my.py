class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_convert_to_array(h):
    r=[]
    c=h
    while c:
        r.append(c.val)
        c=c.next
    return r

class Solution:
    def reverseList(self,h):
        r=list_convert_to_array(h)[::-1]
        c=h
        for i in r:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))