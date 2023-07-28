"""
Given two sets, write a program to return a new set of identical items from both sets.
"""
def shared_values(set1, set2):
    result = set1.intersection(set2)
    return result

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(shared_values(set1, set2))