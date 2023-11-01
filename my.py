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
    def isPalindrome(self,h):
        s=' '.join(map(str,list_convert_to_array(h)))
        return s==s[::-1]

s=Solution()

print(s.isPalindrome(ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))))