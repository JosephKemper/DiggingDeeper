# Queues

### Why is it Important to Know About Queues?
---
Imagine for a moment, you have been called into a project to help a large server manage data requests. Your goal is to make sure that all requests get processed in the order in which they were received, specifically ensuring that no one gets to cut in line. This is a queue. There are hundreds of examples of where queues are used in real life. The software used by call centers to ensure calls are answered in the order they called, tools that help schedule jobs or projects that need worked next, and the software that keeps track of what document needs printed next are just a few examples of places where the Queue Data structure is used in real life. Chances are, if you are going to be programming, you will need to know how to use the Queue Data Structure. 

### What is a Queue?
---
The Queue is a data structure that operates on a first come first serve basis. The easiest way to visualize a queue (and one that most people will be familiar with) is to think of a grocery store cash register. If you walk up to the register and there are three other people in line, then you must get in line. The process of adding data to a queue is called enqueue. Then, when the next person in line gets to check out, they are removed from the front of the queue. The process of removing data from the front of a queue is called dequeue. In Python, you have three options for how you could implement the Queue. 

* A list (when using a specific set of commands)
* The `collections.deque` module (also through using specific commands)
* The `queue.Queue` module

When using the list as a Queue Data Structure, you get O(1) performance for most commands, but when removing items, you get O(n) performance. The `collections.deque` module allows O(1) performance for append and pop operations, making it popular for larger data sets. The `queue.Queue` module is implemented using a double linked list, which means that under ideal circumstances it can have O(1) performance, but because of the size requirements involved in storing the data, it can quickly degrade when storing large amounts of data or when using computers with fewer resources. 

### Python Related Queue Commands
---
There are three options we can use when trying to implement the Queue Data Structure in Python. The traditional list, the `queue.Queue` module, and the `collections.deque` module. The list is a dynamic array. The `queue.Queue` module is a doubly-linked list, and the `collections.deque` module is a double-ended queue.

If you want to dig deeper into dynamic arrays, doubly-linked lists, or double-ended queues, then here are a few places you can start. 

* For dynamic arrays:
    - [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    - [Real Python](https://realpython.com/python-lists-tuples/)

* For doubly-linked lists:
    - [GeeksforGeeks](https://www.geeksforgeeks.org/doubly-linked-list/)
    - [Programiz](https://www.programiz.com/dsa/doubly-linked-list)

* For double-ended queues:
    - [Python documentation](https://docs.python.org/3/library/collections.html#collections.deque)
    - [Real Python](https://realpython.com/how-to-implement-python-stack/)

Queue related List commands in Python

|Common Queue Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|enqueue(value)|Adds "value" to the back of the queue|my_queue.append(value)|O(1) - Performance of adding to the end of the dynamic array|
|dequeue()|Two approaches: Remove and return the item from the front of the queue; or pop off index 0|value = my_queue [0] del my_queue[0] or value = my_queue.pop(0)|O(n) - Performance of obtaining and removing from the beginning of the dynamic array|
|size() |Return the size of the queue|length = len(my_queue)|O(1) - Performance of returning the size of the dynamic array|
|empty()|Returns true if the length of the queue is zero.|if len(my_queue) == 0:|O(1) - Performance of checking the size of the dynamic array|

Table sourced from [here](https://byui-cse.github.io/cse212-course/lesson04/04-prepare.html)

Queue related commands for the `collections.deque` Python Module

queue.Queue Related queue operations
|Common Queue Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|enqueue(value)|Adds "value" to the back of the queue|my_queue.put(value)|O(1) - Performance of adding to the end of th doubly-linked list|
|dequeue()|Two approaches: Remove and return the item from the front of the queue; or pop off index 0|my_queue.get()|O(1) - Performance of obtaining and removing from the beginning of the doubly-linked list|
|size() |Return the size of the queue|my_queue.qsize() *Note, this is not always accurate|O(1) - Performance of returning the size of the doubly-linked list|
|empty()|Returns true if the length of the queue is zero.|my_queue.empty()|O(1) - Performance of checking the size of the doubly-linked list|

Commands for the `queue.Queue` Python module

|Common Queue Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|enqueue(value)|Adds "value" to the back of the queue|my_queue.put(value)|O(1) - Performance of adding to the end of th doubly-linked list|
|dequeue()|Two approaches: Remove and return the item from the front of the queue; or pop off index 0|my_queue.get()|O(1) - Performance of obtaining and removing from the beginning of the doubly-linked list|
|size() |Return the size of the queue|my_queue.qsize() *Note, this is not always accurate|O(1) - Performance of returning the size of the doubly-linked list|
|empty()|Returns true if the length of the queue is zero.|my_queue.empty()|O(1) - Performance of checking the size of the doubly-linked list|

### Examples of Queues
---
The Queue Data Structure implemented via the list in Python. 

```Python
my_queue = []

# enqueue(value)
my_queue.append(1)

# dequeue()
value = my_queue.pop(0)

# size()
length = len(my_queue)

# empty()
is_empty = len(my_queue) == 0
```

The Queue Data Structure implemented via the `collections.deque` module in Python. 

```Python
from collections import deque

my_queue = deque()

# enqueue(value)
my_queue.append(1)

# dequeue()
value = my_queue.popleft()

# size()
length = len(my_queue)

# empty()
is_empty = len(my_queue) == 0
```

The Queue Data Structure implemented via the `queue.Queue` in Python. 

```Python
from queue import Queue

my_queue = Queue()

# enqueue(value)
my_queue.put(1)

# dequeue()
value = my_queue.get()

# size()
length = my_queue.qsize()

# empty()
is_empty = my_queue.empty()
```

### Digging Deeper into Queues
---
Now, with that foundation into the Queue Data Structure, we are going to look a little deeper into the queue, and dive head first into some algorithms along the way. Our first step is to look at the Sliding Window Maximum algorithm. Here are a few resources you can use to dig a little deeper into the Sliding Window Maximum algorithm. 
* [Sliding Window Maximum - Algorithms For Solving Problems](https://howigotjob.com/data-structure/sliding-window-maximum/)
* [Sliding Window Maximum (Maximum of all subarrays of size K)](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)
* [Sliding Window Maximum - Monotonic Queue - Leetcode 239](https://www.youtube.com/watch?v=DfljaUwZsOk)

While our problem can be described accurately in something as succinct as this statement "Given an array of integers and a window size, find the maximum element in each window as it slides along the array. This problem can be solved using a deque (double-ended queue) to keep track of the maximum element in the current window." I personally find that lacking for what I would want in a description to a problem. 

First off, the sliding window maximum algorithm can be used for more than just integers. Real life applications of this algorithm include [analyzing stock prices](https://howigotjob.com/data-structure/sliding-window-maximum/) through finding the highest price (or with a bit of adjustment to the algorithm) even the lowest price within a given time period. It can be used in [image processing](https://howigotjob.com/data-structure/sliding-window-maximum/) through things like comparing pixel brightness. Really it is possible to use this algorithm in almost any situation where we are trying to look at patterns, highs or (with a small tweak to the algorithm) lows in data is likely a situation where the Sliding Window Maximum algorithm can be used. So, while for our purposes, we will restrict our deep dive into this problem to just integers, there is a lot more that can be done with this algorithm. 

We want to get an idea of what we will take into the function we will be building and what we want to put out. 
* Inputs
    - An array of integers
    - Window size

* Outputs
    - A sample of the maximum values picked from the window as it moved across the array

The array is simple to understand, it is just a list of random numbers, they can be positive or negative, they just need to be numbers (simply because we have chosen to restrict this example to just numbers). 

The window size is the sample size we are going to look at when examining the data stored in the array. For our example, we will choose a window size of 3. When we first start out, we will look at one number at a time until we get 3 numbers in our window. From there, we will pick the largest from that group of three integers and remove the first integer we looked at (the one in the 0 index spot of our array) and then add the next integer in the array to the window we are looking at. This will effectively move the window down the array we are examining. And we will continue to do this until we have looked at every number in the array. So, what this means is that when we build a loop to iterate over the list, the leading edge of the window will be the value currently being pointed to by our loop. When we write our code, we do not want to extend the window beyond the end of the array, so we will need to put a stop in the code to prevent that from happening. We also, do not want the program to try to pick the maximum number unless the window has a total of 3 values in it. So, we will need to prevent that as well. 

So, translating that into some notes for the code, we could end up with something that looks like this:

```Python
from collections import deque

def sliding_window_max(input_array, window_size):
    """
    This function finds the largest element in a sliding window of a given size. 
    Arguments (inputs):
        input_array: The array to search
        window_size: the size found in the sliding window as it stepped along the array
    
    Returns:
        A list of the largest elements found in the sliding window as it stepped along the array. 
    """

    # Initialize the queue for tracking the numbers in the window and result variables.
    
    # Loop over the array

    # Remove any elements from the queue that are no longer in the window.
        
    # Remove elements from the right end of the deque that are smaller than the current element 
    # This puts the largest item at the front of the queue
        
    # Add the current element to the queue 
    
    # If the current element is the end of the window, add the maximum element in the queue to the result.
    
    # Return a list of integers representing the maximum values found in the sliding window while iterating through the input array
    
# Example
number_array = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(number_array, window_size)) # Expected output: [3,3,5,5,6,7]

# Included for example of how versatile this algorithm is. 
letter_array = ["z","v","h","b","j","d","f","n"]
window_size = 3
print(sliding_window_max(letter_array, window_size)) # Expected output: ['z', 'v', 'j', 'j', 'j', 'n']
```
Then, taking our plan and research, we could build this as one potential implementation of the program to solve our problem. 

```Python
from collections import deque

def sliding_window_max(input_array, window_size):
    """
    This function finds the largest element in a sliding window of a given size. 
    Arguments (inputs):
        input_array: The array to search
        window_size: the size found in the sliding window as it stepped along the array
    
    Returns:
        A list of the largest elements found in the sliding window as it stepped along the array. 
    """

    # Initializing the queue for tracking the numbers in the window and result variables.
    max_queue = deque()
    result = []
    
    # Looping over the array
    for i in range(len(input_array)):

        # Removing any elements from the queue that are no longer in the window.
        # This puts the largest item at the front of the queue
        while max_queue and max_queue[0] < i - window_size + 1:
            max_queue.popleft()
        
        # remove elements from the right end of the deque that are smaller than the current element
        while max_queue and input_array[max_queue[-1]] < input_array[i]:
            max_queue.pop()
        
        # Adding the current element to the queue
        max_queue.append(i)

        # If the current element is the end of the window, add the maximum element in the queue to the result.
        if i >= window_size - 1:
            result.append(input_array[max_queue[0]])
    
    # Return a list of integers representing the maximum values found in the sliding window while iterating through the input array
    return result

# Example
number_array = [1,3,-1,-3,5,3,6,7]
window_size = 3
print(sliding_window_max(number_array, window_size)) # Expected output: [3,3,5,5,6,7]

# Included for example of how versatile this algorithm is. 
letter_array = ["z","v","h","b","j","d","f","n"]
window_size = 3
print(sliding_window_max(letter_array, window_size)) # Expected output: ['z', 'v', 'j', 'j', 'j', 'n']
```

### Digging Even Deeper into Queues
---
For this challenge, your goal is to take a two dimensional list that will be formed into a maze consisting of 1's and 0's nested in lists like this  
``` Python
maze = [
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]
```
And write a program to find the shortest path from the first spot in the to the last spot in the maze. You do not count the starting spot, and only count the moves you make. In the case of the provided example, the shortest path would take 9 moves to get there. 

In the maze, a 1 represents a wall and a 0 represents a path. To help you a bit, we used a Breadth-First Search algorithm to solve the problem. You can read about that here. 

* [Breadth-first search and its uses](https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/breadth-first-search-and-its-uses)
* [The breadth-first search algorithm (BFS)](https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/the-breadth-first-search-algorithm)
* [Breadth First Search (BFS): Visualized and Explained](https://www.youtube.com/watch?v=xlVX7dXLS64)

Remember, that whatever way you choose to solve this problem, your goal is to get to know the queue data structure better. When you're done figuring out your solution, compare it to ours and join in the comments below about what you learned. 

[Solution](shortest_path.py)

### Digging Even Deeper Still into Queues
---
For this problem, we are going to explore another algorithm in our attempts at digging deeper into queues with Python. In this problem, we can use Kruskal’s algorithm to solve the problem in question. This will also require a bit of knowledge about graph theory and priority queues to complete.

If you do not know Kruskal’s algorithm, you can get a wonderful introduction to it [here](https://www.youtube.com/watch?v=XFhW6vhvC64). You can also dig deeper into the algorithm on [Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm), [GeeksforGeeks](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/), [Scaler](https://www.scaler.com/topics/data-structures/kruskal-algorithm/), and [Programize](https://www.programiz.com/dsa/kruskal-algorithm)

To learn about graph theory, here are a few videos and articles to get you started. 

* Videos
 - [“Graph theory full course for Beginners” by Academic Lesson](https://www.youtube.com/watch?v=sWsXBY19o8I)
 - [“INTRODUCTION to GRAPH THEORY - DISCRETE MATHEMATICS” by TrevTutor](https://www.youtube.com/watch?v=HkNdNpKUByM)
* Articles
 - [“Graph Theory 101” by Science in the News](https://sitn.hms.harvard.edu/flash/2021/graph-theory-101/)
 - [“Graph Theory” by Britannica](https://www.britannica.com/topic/graph-theory)

For this problem our goal is to take a connected and undirected graph with weighted edges, and find a subset of the edges that connect all the vertices together without any cycles and with the minimum possible total weight. 

For example, if we had the following graph:
```Python
graph = [
    [(1,4),(2,8)],
    [(2,11),(4,-4)],
    [(3,-5),(5,-2)],
    [(4,-6)],
    [(5,-3)],
    []
]
```
The program we write should expect to be able to find the following points with our solution:
```Python
[(1,4),(2,-5),(4,-6),(5,-3),(3,-2)]
```
Join in the discussion below to discuss your solution to this problem. 

[Back to Data Structure Tutorial Index](index.md)
