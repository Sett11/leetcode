from math import gcd

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
    def oddEvenList(self,h):
        a=list_convert_to_array(h)
        n=len(a)
        r=a[0:n:2]+a[1:n:2]
        c=h
        for i in r:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.oddEvenList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))