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
    def reverseKGroup(self,h,k):
        a=list_convert_to_array(h)
        n=len(a)
        if n<k:
            return h
        r=sum([a[i:i+k][::-1] if i+k<=n else a[i:i+k] for i in range(0,n,k)],[])
        c=h
        for i in r:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.reverseKGroup(ListNode(7,ListNode(2,ListNode(4,ListNode(3,ListNode(8))))),3))