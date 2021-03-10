class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class BinaryTree:
    def createNode(self, data):
        return Node(data)

    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        
        if data < node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)
        return node

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    



cc = BinaryTree()
root = cc.createNode(5)
cc.insertNode(root,2)
cc.insertNode(root,10)
cc.insertNode(root,7)
cc.insertNode(root,15)
cc.insertNode(root,12)
cc.insertNode(root,20)
cc.insertNode(root,30)
cc.insertNode(root,6)
cc.insertNode(root,8)

print("---------------------This is inorder---------------------------")
cc.inorder(root)
print("---------------------This is preorder---------------------------")
cc.preorder(root)
print("---------------------This is postorder---------------------------")
cc.postorder(root)