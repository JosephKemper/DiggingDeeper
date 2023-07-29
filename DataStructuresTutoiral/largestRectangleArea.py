def largestRectangleArea(histogram):
    stack = [] # Initialize stack to keep track of indexes
    maxArea = 0 # Initialize maxArea to keep track of maximum area
    index = 0 # Initialize index to iterate through the histogram
    while index < len(histogram):
        # If stack is empty or current histogram bar is higher than the top of the stack
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index) # Append the index to the stack
            index += 1 # Move to the next index
        else:
            top = stack.pop() # Pop the top of the stack
            # Calculate the area with the popped bar as the smallest bar
            area = histogram[top] * (index if not stack else index - stack[-1] - 1)
            maxArea = max(maxArea, area) # Update maxArea if needed
    while stack: # If there are still elements in the stack
        top = stack.pop() # Pop the top of the stack
        # Calculate the area with the popped bar as the smallest bar
        area = histogram[top] * (index if not stack else index - stack[-1] - 1)
        maxArea = max(maxArea, area) # Update maxArea if needed
    return maxArea

print(largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
