class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def preorderTraversal(self,r):
        a=[]
        def f(r):
            if not r:
                return
            a.append(r.val)
            f(r.left)
            f(r.right)
        f(r)
        return a

S=Solution()
t=TreeNode(1,
           None,TreeNode(2,
                         TreeNode(3),None))
print(S.preorderTraversal(t))