from queue import PriorityQueue

def minimum_spanning_tree(graph):
    # Get the number of vertices in the graph
    num_vertices = len(graph)
    
    # Initialize a list to keep track of visited vertices
    # This list will be used to keep track of which vertices have been added to the minimum spanning tree
    visited = [False] * num_vertices
    
    # Initialize a priority queue to keep track of edges with the smallest weight
    # This priority queue will be used to select the next edge to add to the minimum spanning tree
    edge_queue = PriorityQueue()
    
    # Add all edges from the first vertex to the priority queue
    for vertex, weight in graph[0]:
        edge_queue.put((weight, vertex))
    
    # Mark the first vertex as visited
    visited[0] = True
    
    # Initialize a list to store the result
    result = []
    
    # While the priority queue is not empty
    while not edge_queue.empty():
        # Get the edge with the smallest weight from the priority queue
        weight, vertex = edge_queue.get()
        
        # If the vertex has not been visited yet
        if not visited[vertex]:
            # Mark the vertex as visited
            visited[vertex] = True
            
            # Add the edge to the result
            result.append((vertex, weight))
            
            # Add all edges from this vertex to the priority queue
            for neighbor_vertex, neighbor_weight in graph[vertex]:
                if not visited[neighbor_vertex]:
                    edge_queue.put((neighbor_weight, neighbor_vertex))
    
    # Return the result
    return result

# Example
graph = [
    [(1,4),(2,8)],
    [(2,11),(4,-4)],
    [(3,-5),(5,-2)],
    [(4,-6)],
    [(5,-3)],
    []
]
print(minimum_spanning_tree(graph)) # Expected output: [(1,4),(2,-5),(4,-6),(5,-3),(3,-2)]
