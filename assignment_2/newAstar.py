import queue
from Map import Map_Obj 


def man_dis(a: list, b: list) -> float: #FOR THE FIRST PART, should be simple
        #manhatten distance
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return abs(x1 - x2) + abs(y1-y2)

def a_star_search(map: Map_Obj):
    start = map.get_start_pos()
    goal = map.get_goal_pos()

    g = 0 #actual cost path from start node to current node
    h = 0 #the actual cost path from the current node to the gole node
    f  = 0 #actual cost path from start node to the goal node
    #f = g+h

    open = [] #nodes that have not yet been explored
    closed = [] #nodes that have been exlpored

    open.append((0, start))
    
    while open:

        # Task 5 moving goal ticker
        if map.get_goal_pos != map.get_end_goal_pos:
            goal = map.tick()
        
        #Sorting open to have lowest f-value on top
        open = sorted(open)

        current = open.pop(0) #fcurrent node is the node with the smalles f-value

        if current[1] == goal: #early exit
            return
        
        neighbour_pos = [
            [current[0], current[1] - 1],
            (current[0], current[1] + 1),
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1])
        ]
        
        for n in neighbour_pos: #undersøker naboene

            if map.get_cell_value(n) > 0:
                new_cost = g + map.get_cell_value(n) #ny kostnad av å gå til n
                
                h = new_cost + man_dis(n, goal)

                if n not in closed or h < f or n not in open:
                    f = new_cost
                    open.append((f, n))

        closed.append(current)
        map.set_cell_value(current, 5)
         

    map.show_map()
    return 


if __name__ == "__main__":
    task_1 = Map_Obj(task=1)
    a_star_search(task_1)

    task_2 = Map_Obj(task=2)
    a_star_search(task_2)

    task_3 = Map_Obj(task=3)
    a_star_search(task_3)

    task_4 = Map_Obj(task=4)
    a_star_search(task_4)

    task_5 = Map_Obj(task=5)
    a_star_search(task_5)




        

      

    
