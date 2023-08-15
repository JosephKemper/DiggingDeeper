# Queues

### Why is it Important to Know About Queues?
---
Imagine for a moment, you have been called into a project to help a large server manage data requests. Your goal is to make sure that all requests get processed in the order in which they were received, specifically ensuring that no one gets to cut in line. This is a queue. There are hundreds of examples of where queues are used in real life. The software used by call centers to ensure calls are answered in the order they called, tools that help schedule jobs or projects that need worked next, and the software that keeps track of what document needs printed next are just a few examples of places where the Queue Data structure is used in real life. Chances are, if you are going to be programming, you will need to know how to use the Queue data structure. 

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

Sliding Window Maximum
Given an array of integers and a window size, find the maximum element in each window as it slides along the array. This problem can be solved using a deque (double-ended queue) to keep track of the maximum element in the current window.

### Digging Even Deeper into Queues
---

Shortest Path
Given a maze represented as a matrix of 0s and 1s, where 0 represents an open cell and 1 represents a blocked cell, find the shortest path from a given starting point to a given destination point. This problem can be solved using the Breadth-First Search (BFS) algorithm, which uses a queue to keep track of the cells to be visited.

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
