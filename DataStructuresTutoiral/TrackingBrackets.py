def is_balanced(bracket_string):
    # Initialize an empty stack
    bracket_stack = []
    # Iterate over each character in the input string
    for character in bracket_string:
    # Check if the character is an opening bracket
        if character in '({[':
            # Push opening bracket onto the stack
            bracket_stack.append(character)
        # Check if the character is a closing bracket
        elif character in ')}]':
            # Check if the stack is empty
            if not bracket_stack:
                # Return false because the string is not balanced
                return False
            """
            Begin checking for balanced strings
            At this point, all of the opening brackets should be in the stack
            The current character will be a closing bracket
            And we will need to make sure the current closing bracket is the same
            as the last opening bracket we added to the stack
            """
            # Pop top opening bracket of stack
            top = bracket_stack.pop()
            # Check if bracket is not matched set
            # Return false if it is not a matched set
            if character == ')' and top != '(':
                return False 
            elif character == '}' and top != '{':
                return False 
            elif character == ']' and top != '[': 
                return False 

    # Return true if stack is empty because the string is balanced
    return not bracket_stack


print(is_balanced("{[()]}")) # True - This string has matching brackets
print(is_balanced("{[(])}")) # False - This string has unmatched brackets