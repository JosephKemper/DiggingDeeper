from collections import deque

def sliding_window_max(nums, window_size):
    num_elements = len(nums)
    max_queue = deque()
    result = []
    window = []
    for i in range(num_elements):
        # Remove elements from the front of the deque that are outside of the current window
        while max_queue and max_queue[0] < i - window_size + 1:
            max_queue.popleft()
        # Remove elements from the back of the deque that are smaller than the current element
        while max_queue and nums[max_queue[-1]] < nums[i]:
            max_queue.pop()
        # Append the index of the current element to the back of the deque
        max_queue.append(i)
        # Update the window variable to store the elements in the current window
        if i >= window_size - 1:
            window_start = i - window_size + 1
            window_end = i + 1
            window = nums[window_start:window_end]
            #print(f"Window: {window}")
            result.append(nums[max_queue[0]])
    return result

# Example
nums = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(nums, window_size)) # Expected output: [3,3,5,5,6,7]
