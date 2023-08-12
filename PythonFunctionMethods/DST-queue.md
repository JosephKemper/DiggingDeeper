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

Queue related List commands in Python

|Common Queue Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|enqueue(value)|Adds "value" to the back of the queue|my_queue.append(value)|O(1) - Performance of adding to the end of the dynamic array|
|dequeue()|Two approaches: Remove and return the item from the front of the queue; or pop off index 0|value = my_queue [0] del my_queue[0] or value = my_queue.pop(0)|O(n) - Performance of obtaining and removing from the beginning of the dynamic array|
|size() |Return the size of the queue|length = len(my_queue)|O(1) - Performance of returning the size of the dynamic array|
|empty()|Returns true if the length of the queue is zero.|if len(my_queue) == 0:|O(1) - Performance of checking the size of the dynamic array|

Table sourced from [here](https://byui-cse.github.io/cse212-course/lesson04/04-prepare.html)

When using `collections.deque` instead of a list, to remove an item from the data structure, you would use `.popleft()`instead. For example this code would remove and print the number 1 from the deque object. 

```Python
from collections import deque

my_deque = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(my_deque.popleft())
```

The rest of the basic commands are the same between a list and a deque object. 

Commands for the `queue.Queue` Python module

|Common Queue Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|enqueue(value)|Adds "value" to the back of the queue|my_queue.put(1)|O(1)|
|dequeue()|Two approaches: Remove and return the item from the front of the queue; or pop off index 0|my_queue.get()|O(1)|
|size() |Return the size of the queue|my_queue.qsize() *Note, this is not always accurate|O(1)|
|empty()|Returns true if the length of the queue is zero.|my_queue.empty()|O(1)|

If you want to dig deeper into this using the deque and queue objects, then here are a few articles/sites you can start with. 
* `collections.deque`
    - [realpython.com](https://realpython.com/python-deque/)
    - [python.org](https://docs.python.org/3/library/collections.html#collections.deque)
    - [section.io](https://www.section.io/engineering-education/queue-data-structure-python/)
    - [note.nkmk.me](https://note.nkmk.me/en/python-collections-deque/)
* `queue.Queue`
    - [python.org](https://docs.python.org/3/library/queue.html)
    - [geeksforgeeks.org](https://www.geeksforgeeks.org/queue-in-python/)
    - [askpython.com](https://www.askpython.com/python-modules/python-queue)
    - [geeksforgeeks.org](https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/)
### Examples of Queues
---


### Digging Deeper into Queues
---


### Digging Even Deeper into Queues
---


### Digging Even Deeper Still into Queues
---



[Back to Data Structure Tutorial Index](index.md)
