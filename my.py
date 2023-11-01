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
    def swapPairs(self,h):
        a=list_convert_to_array(h)
        n=len(a)
        if n<2:
            return h
        r=sum([[a[i+1],a[i]] for i in range(0,n-1,2)],[])
        if n&1:
            r.append(a[-1])
        c=h
        for i in r:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.swapPairs(ListNode(7,ListNode(2,ListNode(4,ListNode(3,ListNode(8)))))))