from collections import deque

def sliding_window_max(nums, window_size):
    num_elements = len(nums)
    max_queue = deque()
    result = []
    for i in range(num_elements):
        while max_queue and max_queue[0] < i - window_size + 1:
            max_queue.popleft()
        while max_queue and nums[max_queue[-1]] < nums[i]:
            max_queue.pop()
        max_queue.append(i)
        if i >= window_size - 1:
            result.append(nums[max_queue[0]])
    return result

# Example
nums = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(nums, window_size)) # Expected output: [3,3,5,5,6,7]
nums = ["z","v","h","b","j","d","f","n"]
window_size = 3
print(sliding_window_max(nums, window_size)) # Expected output: ['z', 'v', 'j', 'j', 'j', 'n']