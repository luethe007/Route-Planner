import heapq
import math
def shortest_path(M, start: int, end: int) -> list:
    """
        Implements A* route plannnig algorithm.
        :Params:
        :M: Map object
        :start: start intersection
        :end: end intersection
    """
    # Handle edge case
    if start == end:
        return [start]
    
    # f_distance = g_distance + h_distance
    # g_distance: path cost
    # h_distance: estimated distance to goal
    q = []
    heapq.heappush(q, (0, [[start], 0])) # (f_distance, [path, g_distance])
    frontier = []
    
    # Iterate over map until route to target is found
    while q:
        f_distance, path_data = heapq.heappop(q) # get most promising path
        path, g_distance = path_data
        current_city = path[-1]
        if current_city == end: # check if we already reached our target
            return path
        frontier = M.roads[current_city] # fill the frontier
        for point in frontier :
            if point not in path: # going back does not make sense
                path_cost = g_distance + get_distance(M.intersections[current_city], 
                                                      M.intersections[point])
                estimated_cost = get_distance(M.intersections[point], M.intersections[end])
                
                # Add new path to the priority queue
                heapq.heappush(q, (path_cost+estimated_cost, [path + [point], path_cost]))
    
    # Return empty list if no route exists
    return []
    

def get_distance(a, b):
    x_delta = abs(a[0] - b[0])
    y_delta = abs(a[1] - b[1])
    return math.sqrt(x_delta**2 + y_delta**2)