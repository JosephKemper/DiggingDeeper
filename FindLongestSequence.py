"""
Find the longest consecutive subsequence in an array.
"""

def findLongestSequence (arr, n):
    # Create an empty set
    elements = set()
    # Initialize the maximum length of consecutive subsequence
    max_length = 0
    # Add all elements of the array to the set
    for element in arr:
        elements.add(element)
    # Iterate over the array
    for i in range(n):
        # If the previous element is not in the set
        if (arr[i]-1) not in elements:
            # Initialize a counter variable to count the length of the current subsequence
            current_element = arr[i]
            # While the current element is in the set
            while(current_element in elements):
                # Increment the counter variable
                current_element += 1
            # Update the maximum length of consecutive subsequence
            max_length = max(max_length, current_element-arr[i])
    # Return the maximum length of consecutive subsequence
    return max_length

# Test the function with an example array
arr = [1, 9, 3, 10, 4, 20, 2]
n = len(arr)
print(findLongestSequence(arr, n))
# Expected output: 4 (the longest consecutive subsequence is [1, 2, 3, 4])