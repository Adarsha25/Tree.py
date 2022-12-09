# creating the node with left right and data value
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# data insertion
class Tree:
    def createnode(self, data):
        return Node(data)

    def insert(self, node , data):
        if node is None:
            return self.createnode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def traverse_Inorder(self, root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data)
            self.traverse_Inorder(root.right)

# driver code
tree=Tree()
root=tree.createnode(5)
print('the root of the tree is:-',root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)
print('Traversing in inorder')
tree.traverse_Inorder(root)