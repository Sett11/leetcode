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
    def insertGreatestCommonDivisors(self,h):
        c,next=h,h.next
        while next:
            n=ListNode(gcd(c.val,next.val))
            c.next=n
            n.next=next
            c=next
            next=next.next
        return list_convert_to_array(h)

s=Solution()

#print(s.insertGreatestCommonDivisors(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))
print(s.insertGreatestCommonDivisors(ListNode(18,ListNode(6,ListNode(10,ListNode(3))))))