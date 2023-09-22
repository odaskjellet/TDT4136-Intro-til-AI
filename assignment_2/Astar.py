import queue
from typing import Optional, Protocol, TypeVar
from Map import Map_Obj 
import heapq


Location = TypeVar('Location')
class Graph(Protocol):
    def neighbors(self, id: Location) -> list[Location]: pass

# class PriorityQueue:
#     def __init__(self):
#         self.elements: list[tuple[float, T]] = []
    
#     def empty(self) -> bool:
#         return not self.elements
    
#     def put(self, item: T, priority: float):
#         heapq.heappush(self.elements, (priority, item))
    
#     def get(self) -> T:
#         return heapq.heappop(self.elements)[1]


class WeightedGraph(Graph):
    def cost(self, from_id: Location, to_id: Location) -> float: pass



def man_dis(a: list, b: list) -> float: #FOR THE FIRST PART, should be simple
        #manhatten distance
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return abs(x1 - x2) - abs(y1-y2)



def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = queue.PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current: Location = frontier.get()
        
        if current == goal: #early exit
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + man_dis(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

# def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
#     frontier = PriorityQueue()
#     frontier.put(start, 0)
#     came_from: dict[Location, Optional[Location]] = {}
#     cost_so_far: dict[Location, float] = {}
#     came_from[start] = None
#     cost_so_far[start] = 0
    
#     while not frontier.empty():
#         current: Location = frontier.get()
        
#         if current == goal: #early exit
#             break
        
#         for next in graph.neighbors(current):
#             new_cost = cost_so_far[current] + graph.cost(current, next)
#             if next not in cost_so_far or new_cost < cost_so_far[next]:
#                 cost_so_far[next] = new_cost
#                 priority = new_cost + man_dis(next, goal)
#                 frontier.put(next, priority)
#                 came_from[next] = current
    
#     return came_from, cost_so_far


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
