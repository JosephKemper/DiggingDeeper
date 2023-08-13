from collections import deque

def shortest_path(maze, start, end):
    num_rows, num_cols = len(maze), len(maze[0])
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    queue = deque([(start, 0)])
    visited[start[0]][start[1]] = True
    while queue:
        (current_row, current_col), distance = queue.popleft()
        if (current_row, current_col) == end:
            return distance
        for delta_row, delta_col in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            next_row, next_col = current_row + delta_row, current_col + delta_col
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols and not visited[next_row][next_col] and maze[next_row][next_col] == 0:
                visited[next_row][next_col] = True
                queue.append(((next_row, next_col), distance + 1))
    return -1

# Example
maze = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)
print(shortest_path(maze, start, end)) # Expected output: 5
