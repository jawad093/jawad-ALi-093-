class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, current_node, data):
        current_node.left = Node(data)

    def insert_right(self, current_node, data):
        current_node.right = Node(data)

    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)    
            self.pre_order(node.right)   

    def in_order(self, node):
        if node:
            self.in_order(node.left)   
            print(node.data, end=" ")   
            self.inorder(node.right)    

    def post_order(self, node):
        if node:
            self.post_order(node.left)   
            self.post_order(node.right)  
            print(node.data, end=" ")    


tree = Binary_Tree("a")
tree.insert_left(tree.root, "b")
tree.insert_right(tree.root, "c")
tree.insert_left(tree.root.left, "d")
tree.insert_right(tree.root.left, "e")
tree.insert_left(tree.root.right, "f")
tree.insert_right(tree.root.right, "g")

print("Pre_order Traversal:")
tree.pre_order(tree.root)
print("In_order Traversal:")
tree.in_order(tree.root)
print("Post_order Traversal:")
tree.post_order(tree.root)
