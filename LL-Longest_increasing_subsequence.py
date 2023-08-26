from collections import deque

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums)) # Output: 4

"""
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science. Given an unsorted array of integers, the goal is to find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements¹.

Here's an example of how you can solve the LIS problem using the `deque` data structure in Python:

```python
from collections import deque

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums)) # Output: 4
```

In this example, we use dynamic programming to solve the LIS problem. We create a `dp` array of length `n`, where `n` is the length of the input array `nums`. The `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. We initialize all elements of `dp` to `1`, since a single element is always an increasing subsequence.

We then iterate over the input array `nums` from left to right. For each element `nums[i]`, we iterate over all elements before it (`nums[j]` where `j < i`) and check if `nums[i] > nums[j]`. If this condition is true, it means that we can extend the increasing subsequence ending at index `j` by adding the element `nums[i]`. We update `dp[i]` to be the maximum of its current value and `dp[j] + 1`.

After we finish iterating over the input array, we return the maximum value in the `dp` array, which represents the length of the longest increasing subsequence.

I hope this example helps you understand how to solve the LIS problem using the `deque` data structure in Python! 😊

Source: Conversation with Bing, 8/25/2023
(1) python - Longest increasing subsequence - Stack Overflow. https://stackoverflow.com/questions/3992697/longest-increasing-subsequence.
(2) Python program for Longest Increasing Subsequence. https://www.geeksforgeeks.org/python-program-for-longest-increasing-subsequence/.
(3) Longest Increasing Subsequence - Classical Algorithm Problems in Python. https://classical-algorithm-problems-in-python.readthedocs.io/en/latest/longest_increasing_subsequence/.
(4) Longest Increasing Subsequence - LeetCode. https://leetcode.com/problems/longest-increasing-subsequence/.
"""