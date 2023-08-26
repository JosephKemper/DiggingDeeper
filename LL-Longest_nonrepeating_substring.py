from collections import deque

def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    dq = deque()
    for i in range(n):
        while s[i] in dq:
            dq.popleft()
        dq.append(s[i])
        max_len = max(max_len, len(dq))
    return max_len

# Example:
s = "abcabcbb"
print(length_of_longest_substring(s)) # Output: 3


"""
The Longest Substring Without Repeating Characters problem is a classic problem in computer science. Given a string, the goal is to find the length of the longest substring without repeating characters¹.

Here's an example of how you can solve this problem using the `deque` data structure in Python:

```python
from collections import deque

def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    dq = deque()
    for i in range(n):
        while s[i] in dq:
            dq.popleft()
        dq.append(s[i])
        max_len = max(max_len, len(dq))
    return max_len

# Example:
s = "abcabcbb"
print(length_of_longest_substring(s)) # Output: 3
```

In this example, we use a `deque` to keep track of the characters in the current substring. We iterate over the input string `s` from left to right. For each character `s[i]`, we check if it is already in the `deque`. If it is, we remove elements from the left of the `deque` until `s[i]` is no longer in the `deque`. We then append `s[i]` to the right of the `deque`.

After appending `s[i]` to the `deque`, we update the maximum length of the longest substring without repeating characters (`max_len`) by taking the maximum of its current value and the length of the `deque`.

After we finish iterating over the input string, we return the maximum length of the longest substring without repeating characters (`max_len`).

I hope this example helps you understand how to solve the Longest Substring Without Repeating Characters problem using the `deque` data structure in Python! 😊

Source: Conversation with Bing, 8/25/2023
(1) python - Longest Substring Without Repeating Characters - Stack Overflow. https://stackoverflow.com/questions/55794010/longest-substring-without-repeating-characters.
(2) Python Program To Find Length Of The Longest Substring Without .... https://www.geeksforgeeks.org/python-program-to-find-length-of-the-longest-substring-without-repeating-characters/.
(3) Longest Substring Without Repeating Characters - InterviewBit. https://www.interviewbit.com/blog/longest-substring-without-repeating-characters/.
(4) Length of the longest substring without repeating characters. https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/.
"""