from sys import set_int_max_str_digits
set_int_max_str_digits(20000)

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
    def doubleIt(self,h):
        L=ListNode()
        c=L
        n=list(map(int,str(int(''.join(map(str,list_convert_to_array(h))))*2)))
        l=len(n)
        for i in range(l):
            c.val=n[i]
            c.next=ListNode() if i!=l-1 else None
            c=c.next
        return L

s=Solution()

print(s.doubleIt(ListNode(7,ListNode(2,ListNode(4,ListNode(3,ListNode(8,ListNode(9))))))))