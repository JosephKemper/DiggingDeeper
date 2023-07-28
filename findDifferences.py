"""
Write a Python program to find the difference between two lists.
"""
# Define a function that takes two lists as arguments and returns their symmetric difference
def diff(list1, list2):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)
    # Use the set method 'symmetric_difference' to find the elements that are unique to each set
    result = set1.symmetric_difference(set2)
    # Convert the result back to a list and return it
    return list(result)

# Create two lists of numbers
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Call the diff function with the two lists as arguments and print the result
print(diff(list1, list2))
# Expected Output: [1, 2, 5, 6]
