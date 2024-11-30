class Node:
    def __init__(self, data):
        self.data = data  
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node) 


def BFS(initial_node):
    visit = []  
    queue = [initial_node] 

    while queue:
        current_node = queue.pop(0)  

        if current_node.data not in visit:
            visit.append(current_node.data)  
            print(current_node.data, end=" ") 

            for child in current_node.children:  
                queue.append(child)



root_value = Node("s")
t = Node("t")
u= Node("u")
v = Node("v")
w = Node("w")
x = Node("x")
y = Node("y")


root_value.add_child(t)
root_value.add_child(u)
t.add_child(v)
t.add_child(w)
u.add_child(x)
x.add_child(y)

BFS(root_value)
