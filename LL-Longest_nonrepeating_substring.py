from collections import deque

def length_of_longest_nonrepeating_substring(sample_string):
    # Get the length of the input string
    string_length = len(sample_string)
    # Initialize a variable to store the maximum length of the substring
    max_length = 0
    # Create a deque to store the characters of the substring
    substring_chars = deque()
    # Iterate over each character in the input string
    for i in range(string_length):
        # While the current character is in the deque, remove characters from the left of the deque
        while sample_string[i] in substring_chars:
            substring_chars.popleft()
        # Add the current character to the right of the deque
        substring_chars.append(sample_string[i])
        # Update the maximum length of the substring if necessary
        max_length = max(max_length, len(substring_chars))
    # Return the maximum length of the substring
    return max_length

# Example:
sample_string = "abcabcbb"
print(length_of_longest_nonrepeating_substring(sample_string)) # Output: 3




"""
Source
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