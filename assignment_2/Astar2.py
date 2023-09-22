import queue
from typing import Optional, Protocol, TypeVar
from Map import Map_Obj 
import heapq

class Node:

    "Class "

    def __init__(self, position, parent=None, cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost

Location = TypeVar('Location')

def man_dis(node, goal) -> float: #FOR THE FIRST PART, should be simple
        #manhatten distance
        x1, y1 = node.position
        x2, y2 = goal.position
        return abs(x1 - x2) + abs(y1-y2)

# def get_neighbours(node):
#      neighbour_pos = [
#             [node.position[0], node.position[1] - 1],
#             [node.position[0], node.position[1] + 1],
#             [node.position[0] - 1, node.position[1]],
#             [node.position[0] + 1, node.position[1]]
#         ]
#      return neighbour_pos


def get_neighbours(node):
    x, y = node.position
    neighbours = []

    # Add adjacent nodes (up, down, left, right)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        neighbours.append(Node((new_x, new_y), parent=node, cost=node.cost + 1))

    return neighbours


def a_star_search(map: Map_Obj):
    # start_pos har to koordinater
    start = map.get_start_pos()
    goal = map.get_end_goal_pos()

    open_list = [] #nodes that are yet to be explored
    closed_list = set() #explored nodes #fjør om fra set() til list()

    heapq.heappush(open_list, (0, start))
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            # Goal reached, construct and return the path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node)

        for neighbour in get_neighbours(current_node):
            if neighbour in closed_list:
                continue

            new_cost = current_node.cost + 1
            if neighbour not in open_list:
                heapq.heappush(open_list, (new_cost + man_dis(neighbour, goal), neighbour))
            elif new_cost < neighbour.cost:
                neighbour.cost = new_cost
                neighbour.parent = current_node



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





