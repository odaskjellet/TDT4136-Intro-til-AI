from Map import Map_Obj


class Node():
    def __init__(self, parent, pos: list[int, int], g: int, h: int):
        self.pos = pos
        self.parent = parent
        self.g = g #actual cost path from start node to current node
        self.h = h #the actual cost path from the current node to the gole node

    def get_pos(self):
        return self.pos

    #actual cost path from start node to the goal node
    def get_f(self): 
        return self.g + self.h


def a_star_search(map: Map_Obj):
    start = map.get_start_pos()
    goal = map.get_goal_pos()

    open = [] #nodes that have not yet been explored
    closed = [] ##nodes that have been exlpored

    open.append(Node(None, start, 0, man_dis(start, goal)))

    while open:

        # Task 5 moving goal ticker
        if map.get_goal_pos != map.get_end_goal_pos:
            goal = map.tick()

        # Using priority queue did not work, must sort queue manually
        open.sort(key=lambda x: x.get_f())

        # Getting the node with the lowest f
        current = open.pop(0)

        current_pos = current.get_pos()

        # Early exit, check if goal is reached
        if current_pos == goal:
            break

        # Find neighbours
        neighbour_nodes = [
            [current_pos[0], current_pos[1] - 1],
            [current_pos[0], current_pos[1] + 1],
            [current_pos[0] - 1, current_pos[1]],
            [current_pos[0] + 1, current_pos[1]]
        ]

        for next in neighbour_nodes:
            # Check if neighbour can be traversed
            if map.get_cell_value(next) > 0:

                # Calculate the cost from the start to this position
                g = current.g + map.get_cell_value(next)
                #Create neighbour node based on new current g 
                child = Node(current, next, g, man_dis(next, goal))

                # Check if the possible child node is already in open or closed 
                if next not in [item.get_pos() for item in open] and next not in [item.get_pos() for item in closed]:
                    open.append(child)

        closed.append(current)

    #If this prints, too bad :(
    if current_pos != goal:
        print("No path to the goal!")
    else:
        # Trace back the path to find the fastest route
        path = []
        while current:
            path.insert(0, current.get_pos())
            current = current.parent
        for next in path:
            if next not in [start, goal]:
                map.set_cell_value(next, 10)
        map.show_map()



def man_dis(a: list, b: list) -> float: #FOR THE FIRST PART, should be simple
    #manhatten distance
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return abs(x1 - x2) + abs(y1-y2)


#To run the program
if __name__ == "__main__":
    task_1 = Map_Obj(1)
    a_star_search(task_1)

    task_2 = Map_Obj(2)
    a_star_search(task_2)

    task_3 = Map_Obj(3)
    a_star_search(task_3)

    task_4 = Map_Obj(4)
    a_star_search(task_4)

    task_5 = Map_Obj(5)
    a_star_search(task_5)