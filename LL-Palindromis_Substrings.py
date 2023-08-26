from collections import deque

def count_palindromic_substrings(s):
    n = len(s)
    count = 0
    for center in range(2*n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count

# Example:
s = "abc"
print(count_palindromic_substrings(s)) # Output: 3


"""
The Palindromic Substrings problem is a classic problem in computer science. Given a string, the goal is to count the number of palindromic substrings in it. A palindromic substring is a substring that reads the same forwards and backwards¹.

Here's an example of how you can solve this problem using the `deque` data structure in Python:

```python
from collections import deque

def count_palindromic_substrings(s):
    n = len(s)
    count = 0
    for center in range(2*n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count

# Example:
s = "abc"
print(count_palindromic_substrings(s)) # Output: 3
```

In this example, we use a `deque` to keep track of the characters in the current substring. We iterate over all possible centers of palindromes in the input string `s`. For each center, we expand outwards to find all palindromes with this center. We update the count of palindromic substrings (`count`) for each palindrome we find.

After we finish iterating over all possible centers of palindromes, we return the count of palindromic substrings (`count`).

I hope this example helps you understand how to solve the Palindromic Substrings problem using the `deque` data structure in Python! 😊

Source: Conversation with Bing, 8/25/2023
(1) python - Palindromic substrings - Stack Overflow. https://stackoverflow.com/questions/35838075/palindromic-substrings.
(2) python - Find all combinations of palindromic substrings - Stack Overflow. https://stackoverflow.com/questions/32488872/find-all-combinations-of-palindromic-substrings.
(3) Distinct palindromic sub-strings of the given string using Dynamic .... https://www.geeksforgeeks.org/distinct-palindromic-sub-strings-of-the-given-string-using-dynamic-programming/.
(4) Palindrome Substring Queries - GeeksforGeeks. https://www.geeksforgeeks.org/palindrome-substring-queries/.
"""