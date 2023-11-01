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

def next_bigger_number(a,n):
    try:
        return next(i for i in a if i>n)
    except:
        return 0

class Solution:
    def nextLargerNodes(self,h):
        a=list_convert_to_array(h)
        r=[]
        for i in range(len(a)):
            r.append(next_bigger_number(a[i:],a[i]))
        return r

s=Solution()

print(s.nextLargerNodes(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))
print(s.nextLargerNodes(ListNode(18,ListNode(6,ListNode(10,ListNode(3))))))