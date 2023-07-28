"""
One difficult problem that can be solved using a stack is the problem of 
finding the maximum area of a rectangle in a binary matrix. 
A binary matrix is a matrix that contains only 0s and 1s. 
The problem is to find the largest rectangle that contains only 1s.

To solve this problem, you can use a stack to keep track of the heights 
of the bars in a histogram that represents the number of consecutive 
1s in each column of the matrix. 
You iterate over the rows of the matrix and for each row, 
you update the heights of the bars and then use the algorithm for 
finding the largest rectangle in a histogram to find the maximum area for that row. 
You repeat this process for all rows and update the maximum area if necessary.

Here's an example implementation in Python:
"""
def largestRectangleArea(histogram):
    stack = [] # Initialize stack to keep track of the heights of the bars in the histogram
    max_area = 0 # Initialize max_area to keep track of the maximum area of a rectangle
    index = 0 # Initialize index to iterate through the histogram
    while index < len(histogram):
        # If the stack is empty or the current bar is higher than or equal to the bar at the top of the stack
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index) # Add the index of the current bar to the stack
            index += 1 # Move to the next bar
        else:
            top = stack.pop() # Pop the top of the stack
            # Calculate the area with the popped bar as the smallest bar in a rectangle
            area = histogram[top] * (index if not stack else index - stack[-1] - 1)
            max_area = max(max_area, area) # Update max_area if necessary
    while stack:
        top = stack.pop() # Pop the top of the stack
        # Calculate the area with the popped bar as the smallest bar in a rectangle
        area = histogram[top] * (index if not stack else index - stack[-1] - 1)
        max_area = max(max_area, area) # Update max_area if necessary
    return max_area

def maximalRectangle(matrix):
    if not matrix:
        return 0
    max_area = 0 # Initialize max_area to keep track of the maximum area of a rectangle in the matrix
    histogram = [0] * len(matrix[0]) # Initialize histogram to keep track of the heights of bars in each row
    for row in matrix:
        for i, value in enumerate(row):
            # Update histogram by adding 1 to the height of a bar if value is '1', otherwise reset it to 0
            histogram[i] = histogram[i] + 1 if value == '1' else 0
        # Calculate the largest area of a rectangle in this row's histogram and update max_area if necessary
        max_area = max(max_area, largestRectangleArea(histogram))
    return max_area

matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]
print(maximalRectangle(matrix)) # 6

