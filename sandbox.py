from collections import deque

def sliding_window_max(nums, window_size):
  """
  This function finds the maximum element in a sliding window of a given size.

  Args:
    nums: The array to search.
    window_size: The size of the sliding window.

  Returns:
    A list of the maximum elements in the sliding window.
  """

  # Initializing the queue and result variables.
  max_queue = deque()
  result = []

  # Looping over the array.
  for i in range(len(nums)):

    # Removing any elements from the queue that are no longer in the window.
    while max_queue and max_queue[0] < i - window_size + 1:
      max_queue.popleft()

    # Adding the current element to the queue.
    max_queue.append(i)

    # Removing the element at the front of the queue if it is not the maximum element in the queue.
    if max_queue and nums[max_queue[0]] < nums[i]:
      max_queue.popleft()

    # If the current element is the end of the window, add the maximum element in the queue to the result.
    if i >= window_size - 1:
      result.append(nums[max_queue[0]])

  return result

# Example
nums = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(nums, window_size)) # Expected output: [3,3,5,5,6,7]
