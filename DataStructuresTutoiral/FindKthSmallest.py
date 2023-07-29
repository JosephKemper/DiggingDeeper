class Node:
    # Defines the initial state of the Node class when created
    def __init__(self, data): 
        self.data = data # Places input data into created node
        self.left = None # Pointer to left node
        self.right = None # Pointer to right node

class BinarySearchTree:
    # Defines the initial state of the Binary Search Tree upon creation
    def __init__(self): 
        # Sets the root of the tree to None
        self.root = None 

    def insert(self, data): # Tells the tree how to insert data
        new_node = Node(data) # All data in Binary Search trees are stored in nodes
        if self.root is None:
            self.root = new_node # Sets data as root if root is empty
        else:
            # determine where the node will go if not root
            self._insert(new_node, self.root) 

    # Separated _insert from insert to allow for cleaner use of recursion
    def _insert(self, new_node, current_node): # Determines where non-root node will go.
        """
        The first time through, the current_node will be the root node. 
        On recursive function calls, the current_node will be the node trying to be navigated to
        """
        if new_node.data == current_node.data:
            return  # Stops duplicate data from being added to the tree
        
        if new_node.data < current_node.data: # Check if data to be inserted is less than current_node
            if current_node.left is None: # Uses pointer in Node class to identify left node
                current_node.left = new_node # If left node is none, we have found where the data goes
            else:
                # Navigate further down the left branch of the tree using recursion
                self._insert(new_node, current_node.left) 
        else: # Used when number is greater than current node
            if current_node.right is None: # Uses pointer in node class to identify right node
                current_node.right = new_node # If the right node is empty we have found where the data goes
            else:
                # Navigate further down the right branch of the tree using recursion
                self._insert(new_node, current_node.right)

    def print_tree(self): 
        if self.root is None: # Checks if tree is empty
            return # Stops method call by returning none
        else:
            self._print_tree(self.root) # Starts printing process

    # Separated _print_tree from print_tree to allow cleaner use of recursion
    def _print_tree(self, current_node): # Defines how to print the tree
        if current_node is not None: # Prevents the program from trying to print an empty node
            print(current_node.data) # Prints data in current node
            self._print_tree(current_node.left) # Recursively moves current_node down the left branch
            self._print_tree(current_node.right) # Recursively moves current_node down the right branch

    """
    The following, adds functionality to use things like the "in" keyword to check 
    if data is in the binary search tree.
    """
    def __contains__(self, data): 
        return self._contains(data, self.root) 
    
    # Separated _contains from __contains__ to allow cleaner use of recursion
    def _contains(self, data, current_node):
        next_node = None # Initialized for later use
        if data == current_node.data:
            return True # Returns true if data is found
        
        elif current_node.left == None and current_node.right == None:
            return False # Returns false if date is not found
        
        elif data < current_node.data: 
            # Sets next node to left child node if data is less than current node
            next_node = current_node.left 

        elif data > current_node.data:
            # Sets next node to right child node if data is grater than current node
            next_node = current_node.right
        
        return self._contains(data, next_node) # Recursive call to method starting from next_node

    # Enables iteration through the tree using the for keyword
    def __iter__(self): 
        yield from self._iter(self.root)
        
    # Separated _iter from __iter__ for cleaner use of recursion
    def _iter (self, current_node): 
        # teaches the __iter__ method how to iterate through data
        if current_node is not None: # Stops the recursive calls to the method when every option is none
             # Recursively calls the function to grab the left most node
            yield from self._iter(current_node.left)
            # Returns data from current node
            yield current_node.data 
            # Recursively calls the function to grab the right most node
            yield from self._iter(current_node.right) 
        
    def __reversed__(self): # Enables the reversed() keyword
        yield from self._reversed(self.root)

    # Separated _reversed from __reversed__ for cleaner use of recursion
    def _reversed (self, current_node): 
        # Teaches the program how the reversed keyword should operate
        if current_node is not None: # Stops the recursive calls to the method when every option is none
            # Recursively calls the function to grab the right most node
            yield from self._reversed(current_node.right) 
            # Returns data from current node
            yield current_node.data 
            # Recursively calls the function to grab the left most node
            yield from self._reversed(current_node.left) 
    
    def get_height(self): # Enables the program to check 
        if self.root is None: # Default case if tree is empty
            return 0
        else:
            return self._get_height(self.root) 

    # Separated _get_height from get_height for cleaner use of recursion
    def _get_height(self, current_node):
        if current_node is None: # Stops recursive calls to function
            return 0
        else:
            # Recursively calls function adding 1 to each variable each time it is called. 
            left_height = self._get_height(current_node.left) 
            right_height = self._get_height(current_node.right)
            # Selects largest of the two variables and adds 1 for the root. 
        return max(left_height, right_height) + 1 

    def find_kth_smallest(self, k):
        # Check if the root of the tree is None
        if self.root is None:
            return None
        else:
            # Initialize a stack to keep track of nodes
            stack = []
            current_node = self.root
            while True:
                # Traverse to the leftmost node
                while current_node is not None:
                    stack.append(current_node)
                    current_node = current_node.left
                # If the stack is empty, return None
                if not stack:
                    return None
                # Pop the top element from the stack
                current_node = stack.pop()
                # Decrement k
                k -= 1
                # If k is 0, return the data of the current node
                if k == 0:
                    return current_node.data
                # Move to the right subtree
                current_node = current_node.right

    def find_kth_largest(self, k):
        # Check if the root of the tree is None
        if self.root is None:
            return None
        else:
            # Initialize a stack to keep track of nodes
            stack = []
            currentNode = self.root
            while True:
                # Traverse to the rightmost node
                while currentNode is not None:
                    stack.append(currentNode)
                    currentNode = currentNode.right
                # If the stack is empty, return None
                if not stack:
                    return None
                # Pop the top element from the stack
                currentNode = stack.pop()
                # Decrement k
                k -= 1
                # If k is 0, return the data of the current node
                if k == 0:
                    return currentNode.data
                # Move to the left subtree
                currentNode = currentNode.left



bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(17)

print(bst.find_kth_largest(3))
print(bst.find_kth_smallest(3))