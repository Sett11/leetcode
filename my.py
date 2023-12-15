class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def postorderTraversal(self,r):
        a=[]
        def f(r):
            if not r:
                return
            f(r.left)
            f(r.right)
            a.append(r.val)
        f(r)
        return a

S=Solution()
t=TreeNode(1,
           None,TreeNode(2,
                         TreeNode(3),None))
print(S.postorderTraversal(t))