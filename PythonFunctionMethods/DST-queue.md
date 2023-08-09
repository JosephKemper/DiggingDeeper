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


### Examples of Queues
---


### Digging Deeper into Queues
---


### Digging Even Deeper into Queues
---


### Digging Even Deeper Still into Queues
---



[Back to Data Structure Tutorial Index](index.md)
