from random import choice

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
    def __init__(self,h):
        self.h=h
    def getRandom(self):
        return choice(list_convert_to_array(self.h))

s=Solution(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))

print(s.getRandom())