from collections import deque

def constrained_subset_sum(number_list, max_distance):
    list_length = len(number_list)
    max_sums = [0] * list_length
    max_sum_indices = deque()
    for i in range(list_length):
        max_sums[i] = number_list[i]
        if max_sum_indices:
            max_sums[i] += max_sums[max_sum_indices[0]]
        while max_sum_indices and max_sum_indices[0] < i - max_distance:
            max_sum_indices.popleft()
        while max_sum_indices and max_sums[max_sum_indices[-1]] < max_sums[i]:
            max_sum_indices.pop()
        max_sum_indices.append(i)
    return max(max_sums)

# Example:
number_list = [10, 2, -10, 5, 20]
k = 2
print(constrained_subset_sum(number_list, k)) # Output: 37




"""
The Constrained Subsequence Sum problem is a classic problem in computer science. 
Given an integer array `nums` and an integer `k`, the goal is to return the maximum 
sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, 
`nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied. 
A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, 
leaving the remaining elements in their original order¹.

Here's an example of how you can solve this problem using the `deque` data structure in Python:

```python
from collections import deque

def constrainedSubsetSum(nums, k):
    n = len(nums)
    dp = [0] * n
    dq = deque()
    for i in range(n):
        dp[i] = nums[i]
        if dq:
            dp[i] += dp[dq[0]]
        while dq and dq[0] < i - k:
            dq.popleft()
        while dq and dp[dq[-1]] < dp[i]:
            dq.pop()
        dq.append(i)
    return max(dp)

# Example:
nums = [10, 2, -10, 5, 20]
k = 2
print(constrainedSubsetSum(nums, k)) # Output: 37
```

In this example, we use dynamic programming to solve the Constrained Subsequence Sum problem. We create a `dp` array of length `n`, where `n` is the length of the input array `nums`. The `dp[i]` represents the maximum sum of a non-empty subsequence ending at index `i` that satisfies the condition `j - i <= k`.

We then iterate over the input array `nums` from left to right. For each element `nums[i]`, we update `dp[i]` to be equal to `nums[i]`. If the `deque` is not empty, we add the value of `dp[dq[0]]` to `dp[i]`. We then remove elements from the left of the `deque` until its first element is within the range `[i-k, i-1]`. We also remove elements from the right of the `deque` until its last element is greater than or equal to `dp[i]`. We then append index `i` to the right of the `deque`.

After we finish iterating over the input array, we return the maximum value in the `dp` array, which represents the maximum sum of a non-empty subsequence that satisfies the condition `j - i <= k`.

I hope this example helps you understand how to solve the Constrained Subsequence Sum problem using the `deque` data structure in Python! 😊

Source: Conversation with Bing, 8/26/2023
(1) Constrained Subsequence Sum - LeetCode. https://leetcode.com/problems/constrained-subsequence-sum/solutions/2672473/python-deque/.
(2) Python solution using deque, 94% faster - Constrained Subsequence Sum .... https://leetcode.com/problems/constrained-subsequence-sum/solutions/1383503/Python-solution-using-deque-94-faster/.
(3) Constrained Subsequence Sum - LeetCode. https://leetcode.com/problems/constrained-subsequence-sum/solutions/597751/JavaC++Python-O%28N%29-Decreasing-Deque/.
(4) [Python/C++] DP with decreasing deque - Constrained Subsequence Sum .... https://leetcode.com/problems/constrained-subsequence-sum/solutions/597693/python-c-dp-with-decreasing-deque/.
(5) Subset Sum Problem using Backtracking - GeeksforGeeks. https://www.geeksforgeeks.org/subset-sum-problem/.
"""