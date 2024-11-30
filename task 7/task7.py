class Node:
    def __init__(self, place):
        self.place = place  
        self.alpha = 0  
        self.beta = 0  
        self.gama = 0  
        self.parent = None  
    def __eq__(self, other):
        return self.place == other.place


def heuristic_value(node_place, goal_place):
    
    return abs(node_place[0] - goal_place[0]) + abs(node_place[1] - goal_place[1])


def A_Star(start, goal, grid):
   
    open_list = []
    closed_list = []  

    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)

    while open_list:
        
        current_node = min(open_list, key=lambda node: node.gama)
        open_list.remove(current_node)
        closed_list.append(current_node)

       
        if current_node.place == goal_node.place:
            path = []
            while current_node:
                path.append(current_node.place)
                current_node = current_node.parent
            return path[::-1]  

       
        a, b = current_node.place
        neighbors = [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]

        for next_place in neighbors:
           
            if (next_place[0] < 0 or next_place[0] >= len(grid) or
                next_place[1] < 0 or next_place[1] >= len(grid[0]) or
                grid[next_place[0]][next_place[1]] == 1):
                continue

            neighbor_node = Node(next_place)

            if neighbor_node in closed_list:
                continue

          
            neighbor_node.alpha = current_node.alpha + 1
            neighbor_node.beta = heuristic_value(neighbor_node.place, goal_node.place)
            neighbor_node.gama = neighbor_node.alpha + neighbor_node.beta
            neighbor_node.parent = current_node

            
            if any(open_node for open_node in open_list if open_node == neighbor_node and neighbor_node.gama >= open_node.gama):
                continue

            
            open_list.append(neighbor_node)

    return None  

grid = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
]

initial = (0, 0)  
goal = (4, 4)     

path = A_Star(initial, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found.")
