class Solution:
    def hasCycle(self,h):
        s=set()

        while h:
            if h.next in s:
                return True
            s.add(h)
            h=h.next
        
        return False

S=Solution()

print(S.hasCycle())