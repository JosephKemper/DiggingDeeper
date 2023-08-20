from collections import deque

def sliding_window_max(input_array, window_size):
    """
    This function finds the largest element in a sliding window of a given size. 
    Arguments (inputs):
        input_array: The array to search
        window_size: the size found in the sliding window as it stepped along the array
    
    Returns:
        A list of the largest elements found in the sliding window as it stepped along the array. 
    """

    # # Initializing the queue for window and result variables.
    max_queue = deque()
    result = []
    
    # Looping over the array
    for i in range(len(input_array)):

        # Removing any elements from the queue that are no longer in the window.
        while max_queue and max_queue[0] < i - window_size + 1:
            max_queue.popleft()
        
        # remove elements from the right end of the deque that are smaller than the current element
        while max_queue and input_array[max_queue[-1]] < input_array[i]:
            max_queue.pop()
        
        # Adding the current element to the queue
        max_queue.append(i)

        # If the current element is the end of the window, add the maximum element in the queue to the result.
        if i >= window_size - 1:
            result.append(input_array[max_queue[0]])
    
    # Return a list of integers representing the maximum values found in the sliding window while iterating through the input array
    return result

# Example
number_array = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(number_array, window_size)) # Expected output: [3,3,5,5,6,7]

# Included for example of how versatile this algorithm is. 
letter_array = ["z","v","h","b","j","d","f","n"]
window_size = 3
print(sliding_window_max(letter_array, window_size)) # Expected output: ['z', 'v', 'j', 'j', 'j', 'n']