import queue
from typing import Optional, Protocol, TypeVar
from Map import Map_Obj 
import heapq


#Code is gotten from redblobgames.com

Location = TypeVar('Location')

def man_dis(a: list, b: list) -> float: #FOR THE FIRST PART, should be simple
        #manhatten distance
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return abs(x1 - x2) + abs(y1-y2)


def a_star_search(map: Map_Obj):
    # start_pos har to koordinater
    start = map.get_start_pos()
    goal = map.get_end_goal_pos()

    open = queue.PriorityQueue() #open list
    open.put((0, start))

    came_from: dict[Location, Optional[Location]] = {}  
    cost_so_far: dict[Location, float] = {}
    visited = []
    
    # came_from[start[0], start[1]] = None 
    # cost_so_far[start[0], start[1]] = 0

    came_from[tuple(start)] = None 
    cost_so_far[tuple(start)] = 0
    
    while not open.empty():
        current = open.get()[1]
        

        neighbour_pos = [
            (current[0], current[1] - 1),
            (current[0], current[1] + 1),
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1])
        ]
        
        if current == goal: #early exit
            break

        for next in neighbour_pos: 

            #må sjekke om noden kan besøkes
            if map.get_cell_value(next) < 0:
                 break
            
            new_cost = cost_so_far[tuple(current)] + map.get_cell_value(next) #map.cost(current, next) = map.get_cell_value #muffens

            print(cost_so_far)

            priority = new_cost + man_dis(next, goal)
            if next not in cost_so_far or priority < cost_so_far[next] or next not in visited: #cost_so_far[next]
                cost_so_far[next] = new_cost
                open.put((priority,next))
                came_from[next] = current
                
        visited.append(current)
        #map.set_cell_value(current, 5)
            
    if current != goal:
            print("No path to the goal!")
    else:
        # Trace back the path to find the fastest route
        path = []
        while current:
            path.insert(0, current.get_pos())
            current = current.parent
        for next in path:
            if next not in [start, goal]:
                # Draw route onto map
                map.set_cell_value(next, 5)
        map.show_map()
    return came_from, cost_so_far


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
