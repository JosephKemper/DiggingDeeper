from collections import deque

def shortest_path(maze, start, end):
    # Get the rows and columns of the maze
    num_rows, num_cols = len(maze), len(maze[0])
    
    # Create a 2 dimensional list identical in size to the maze 
    # with false in each internal list
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Create a queue to store cells to visit 
    # while populating the starting cell
    queue = deque([(start, 0)])

    # Mark starting cell as visited
    visited[start[0]][start[1]] = True

    # While the queue is not empty
    while queue:
        # Pull the first tuple in the queue out
        # Assign the value in index 0 to current_row
        # Assign the value in index 1 to current_col
        # Add 1 to the value stored in distance. This will start at 0
        (current_row, current_col), distance = queue.popleft()

        # Check if position equals end value then return distance
        if (current_row, current_col) == end:
            return distance
        
        # Queue up modifiers to use to check the neighbors of the current position
        for row_modifier, col_modifier in ((0, 1), (1, 0), (0, -1), (-1, 0)):

            # Modify the current position using the current modifiers
            next_row, next_col = current_row + row_modifier, current_col + col_modifier
            # Check if the position being checked is valid
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols and not visited[next_row][next_col] and maze[next_row][next_col] == 0:
                # Mark true and add to queue if move is valid
                visited[next_row][next_col] = True
                queue.append(((next_row, next_col), distance + 1))
    # Return "No Solution" if there is no way to get to the end of the maze
    return "No Solution"

# Example 
# Key: 0 represents an open space, and 1 represents a wall. 
maze = [
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]
start = (0, 0)
end = (len(maze) - 1, len(maze[0]) - 1)
print(shortest_path(maze, start, end)) # Expected output: 5
