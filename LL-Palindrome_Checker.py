from collections import deque

def is_palindrome(string):
    # Create a deque to store the characters of the string
    char_deque = deque(string)
    
    # Iterate until the deque is empty or the characters at the front and rear are different
    while len(char_deque) > 1:
        # Remove the characters at the front and rear of the deque
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        
        # If the characters are different, return False
        if first_char != last_char:
            return False
    
    # If all characters have been checked and are equal, return True
    return True

# Test the function with some sample input
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("madam"))    # Output: True
print(is_palindrome("testtset")) # Output: True