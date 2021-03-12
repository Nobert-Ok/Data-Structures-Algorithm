class Solution(object):
    def __init__(self):
        self.ans = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ans.append(root.val)
            
        return self.ans