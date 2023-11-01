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
    def swapNodes(self,h,k):
        a=list_convert_to_array(h)
        a[k-1],a[-k]=a[-k],a[k-1]
        c=h
        for i in a:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.swapNodes(ListNode(7,ListNode(2,ListNode(4,ListNode(3,ListNode(8,ListNode(9)))))),2))