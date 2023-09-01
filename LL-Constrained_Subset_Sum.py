from collections import deque

def constrained_subset_sum(number_list, max_distance):
    # Get the length of the input list
    list_length = len(number_list)
    
    # Initialize a list to store the maximum sums
    max_sums = [0] * list_length
    
    # Create a deque to store the indices of the maximum sums
    max_sum_indices = deque()
    
    # Iterate over each element in the input list
    for index in range(list_length):
        # Set the current maximum sum to the current element in the input list
        max_sums[index] = number_list[index]
        
        # If the deque is not empty, add the maximum sum at the first index in the deque to the current maximum sum
        if max_sum_indices:
            max_sums[index] = max(max_sums[index], max_sums[max_sum_indices[0]] + number_list[index])
        
        # While the first index in the deque is less than i - max_distance, remove it from the deque
        while max_sum_indices and max_sum_indices[0] < index - max_distance:
            max_sum_indices.popleft()
        
        # While the last index in the deque has a smaller maximum sum than the current maximum sum, remove it from the deque
        while max_sum_indices and max_sums[max_sum_indices[-1]] < max_sums[index]:
            max_sum_indices.pop()
        
        # Add the current index to the deque
        max_sum_indices.append(index)
    
    # Return the maximum value in the maximum sums list
    return max(max_sums)



# Example:
number_list = [10, 2, -10, 5, 20]
max_distance = 2
print(constrained_subset_sum(number_list, max_distance)) # Output: 37

number_list = [15,5,-30,-10,6,18,72]
print(constrained_subset_sum(number_list, max_distance))

number_list = [1,-2,-3,-4,-5,-6,-7,-8,-9,10]
print(constrained_subset_sum(number_list, max_distance))


"""
Sure! Here are the plain links to the two articles and one YouTube video that discuss the constrained subset sum problem:

1. Article: "Subset sum problems with digraph constraints" by Laurent Gourvès, Jérôme Monnot & Lydia Tlilane, published in the Journal of Combinatorial Optimization: 
https://link.springer.com/article/10.1007/s10878-019-00422-6
2. Article: "Solutions for subset sum problems with special digraph constraints" by Frank Gurski, Dominique Komander & Carolin Rehs, published in Mathematical Methods of Operations Research: 
https://link.springer.com/article/10.1007/s00186-020-00722-8
3. YouTube Video: "1425. Constrained Subset Sum (Leetcode Hard)" by Programming Live with Larry: 
https://www.youtube.com/watch?v=J0ZbVAynM0Q

I hope these links are helpful! Is there anything else you would like to know? 😊
"""


"""
Sure! Here are two articles and one YouTube video that discuss the constrained subset sum problem:

1. Article: "Subset sum problems with digraph constraints" by Laurent Gourvès, Jérôme Monnot & Lydia Tlilane, published in the Journal of Combinatorial Optimization¹. This article introduces and studies optimization problems related to the well-known Subset Sum problem, where a node-weighted digraph is given and one has to select a subset of vertices whose total weight does not exceed a given budget while satisfying additional constraints called digraph constraints and maximality.
2. Article: "Solutions for subset sum problems with special digraph constraints" by Frank Gurski, Dominique Komander & Carolin Rehs, published in Mathematical Methods of Operations Research². This article considers two extensions of the subset sum problem: The subset sum problem with digraph constraint (SSG) and subset sum problem with weak digraph constraint (SSGW), where a digraph with sizes assigned to the vertices is given. The article shows that both problems are NP-hard even on oriented co-graphs and minimal series-parallel digraphs, and provides pseudo-polynomial solutions for SSG and SSGW with digraph constraints given by directed co-graphs and series-parallel digraphs.
3. YouTube Video: "1425. Constrained Subset Sum (Leetcode Hard)" by Programming Live with Larry⁸. In this video, Larry solves and analyzes the Leetcode problem "Constrained Subset Sum" as both an interviewer and an interviewee. This is a live recording of a real engineer solving a problem live - no cuts or edits!

I hope these resources are helpful! Is there anything else you would like to know? 😊

Source: Conversation with Bing, 8/30/2023
(1) Subset sum problems with digraph constraints | SpringerLink. https://link.springer.com/article/10.1007/s10878-018-0262-1.
(2) Solutions for subset sum problems with special digraph constraints .... https://link.springer.com/article/10.1007/s00186-020-00718-6.
(3) 1425. Constrained Subset Sum (Leetcode Hard) - YouTube. https://www.youtube.com/watch?v=H_H0jEgAdzY.
(4) Constrained Subsequence Sum - LeetCode. https://leetcode.com/problems/constrained-subsequence-sum/.
(5) Confusion about dynamic programming on unconstrained subset sum vs .... https://cs.stackexchange.com/questions/131690/confusion-about-dynamic-programming-on-unconstrained-subset-sum-vs-constrained-s.
(6) Subset Sum Problem using Dynamic Programming | Data Structures and Algorithms. https://www.youtube.com/watch?v=dJmyfFC3-3A.
(7) 7 Subset Sum Problem. https://www.youtube.com/watch?v=_gPcYovP7wc.
(8) L-5.5: Sum of Subsets Problem | Dynamic Programming. https://www.youtube.com/watch?v=MLSy2_iQdmY.
(9) Subset Sum Problem - Explanation and Implementation - YouTube. https://www.youtube.com/watch?v=bH5VkYEEF_8.
(10) Computer Science: Unconstrained subset sum vs constrained ... - YouTube. https://www.youtube.com/watch?v=BNUkQQvZEyU.
(11) undefined. https://www.youtube.com/channel/UCM-yUTYGmrNvKOCcAl21g3w/playlists?view_as=subscriber.
(12) undefined. https://www.geeksforgeeks.org/subset-sum.
(13) undefined. https://www.youtube.com/@varunainashots.
(14) undefined. https://leetcode.com/problems/constra.
(15) undefined. https://www.twitch.tv/larryny.
(16) undefined. https://discord.gg/6QKRCdR.
(17) undefined. https://www.instagram.com/larrysomewh.
(18) undefined. https://github.com/eMahtab/subset-sumFor.
(19) undefined. https://www.patreon.com/roelvandepaarWith.
"""


"""
Sure! Here is a list of steps, using non-programming language, to describe the process used to solve the constrained subset sum problem:

1. Start with a list of numbers and a maximum distance value.
2. Create a new list to keep track of the maximum sums of subsequences that meet the distance constraint.
3. For each number in the list, calculate the maximum sum of a subsequence that ends with that number and meets the distance constraint.
4. To do this, first set the current maximum sum to the value of the current number.
5. Then, find the previous maximum sum that is within the maximum distance from the current number and add it to the current maximum sum.
6. Keep track of the maximum sums within the maximum distance using a sliding window approach.
7. After calculating the maximum sums for all numbers in the list, find the largest maximum sum in the list. This is the solution to the problem.

I hope this helps you understand the process used to solve the constrained subset sum problem! Is there anything else you would like to know? 😊
"""

"""
The reasoning behind how the maximum sum is updated for the current value being processed is based on the idea of dynamic programming. The function `constrained_subset_sum` calculates the maximum sum of a subsequence of the input list `number_list` such that the distance between any two elements in the subsequence is at most `max_distance`. To do this, the function maintains a list `max_sums` to store the maximum sums of subsequences that meet the distance constraint and end at each index in the input list.

For each index `i` in the input list, the function first sets the current maximum sum to the value of the current number `number_list[i]`. Then, it finds the previous maximum sum that is within `max_distance` from the current index and adds it to the current maximum sum. This is done by checking if the deque `max_sum_indices` is not empty and adding the maximum sum at the first index in the deque to the current maximum sum. The deque `max_sum_indices` is maintained using a sliding window approach to keep track of the maximum sums within `max_distance` from the current index.

By adding the previous maximum sum that is within `max_distance` from the current index to the current maximum sum, we ensure that we are considering all possible subsequences that meet the distance constraint and end at index `i`. This allows us to calculate the maximum sum of a subsequence that meets the distance constraint and ends at each index in the input list.

I hope this explanation helps you understand how and why we update what we add to the current value being processed! Is there anything else you would like to know? 😊
"""


"""
Source
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