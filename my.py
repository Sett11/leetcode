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
    def reverseEvenLengthGroups(self,h):
        a=list_convert_to_array(h)
        r=[a.pop(0)]
        i=1
        while a:
            t=a[i-1:i+i]
            r.extend(t if len(t)&1 else t[::-1])
            del a[0:i]
            i+=1
        c=h
        for i in r:
            c.val=i
            c=c.next
        return h

s=Solution()

print(s.reverseEvenLengthGroups(ListNode(7,ListNode(2,ListNode(4,ListNode(3,ListNode(8,ListNode(9,ListNode(10,ListNode(23,ListNode(76,ListNode(98))))))))))))