from collections import deque

def first_unique_char(test_string):
    # Create a queue to store characters
    char_queue = deque()
    # Iterate over each character in the test string
    for char in test_string:
        # If the character is not in the queue, add it to the queue
        if char not in char_queue:
            char_queue.append(char)
        # If the character is already in the queue, remove it from the queue
        else:
            char_queue.remove(char)
    # If the queue is not empty, return the first character in the queue
    if len(char_queue) > 0:
        return char_queue[0]
    # If the queue is empty, tell user there are no unique characters
    else:
        return f"There are no unique characters in the string '{test_string}'"

# Example:
test_string = "Happy"
print(first_unique_char(test_string)) # Output: H




"""
The First Unique Character in a String problem is a classic problem in computer science. 
Given a string, the goal is to find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1¹.

Here's an example of how you can solve this problem using the `deque` data structure in Python:

```python
from collections import deque

def first_unique_char(s):
    dq = deque()
    for char in s:
        if char not in dq:
            dq.append(char)
        else:
            dq.remove(char)
    if len(dq) > 0:
        return s.index(dq[0])
    else:
        return -1

# Example:
s = "leetcode"
print(first_unique_char(s)) # Output: 0
```

In this example, we use a `deque` to keep track of the characters in the input string `s`. We iterate over the input string from left to right. For each character `char`, we check if it is already in the `deque`. If it is not, we append it to the right of the `deque`. If it is, we remove it from the `deque`.

After we finish iterating over the input string, we check if the `deque` is not empty. If it is not empty, we return the index of the first element in the `deque` (`dq[0]`) in the input string `s`. If it is empty, we return -1.

I hope this example helps you understand how to solve the First Unique Character in a String problem using the `deque` data structure in Python! 😊

Source: Conversation with Bing, 8/26/2023
(1) python - First Unique Character in a String - Stack Overflow. https://stackoverflow.com/questions/39651540/first-unique-character-in-a-string.
(2) python - First Unique Character - Stack Overflow. https://stackoverflow.com/questions/68028730/first-unique-character.
(3) First Unique Character using Python | Aman Kharwal - thecleverprogrammer. https://thecleverprogrammer.com/2022/12/14/first-unique-character-using-python/.
(4) First Unique Character in a String (Python). https://losseff.xyz/leetcode/001-first-unique-character-in-a-string/python/."""