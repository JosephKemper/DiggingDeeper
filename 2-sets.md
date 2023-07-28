# Sets

### Why is it Important to Know About Sets?
---

Imagine you have just gotten a contract to help a popular blog build software to better track the unique visitors to their site. Because of how their backend software works, you need to use Python to build this software. You need to keep an ongoing list of all the unique IP addresses that visit their site. For this project, they are not concerned about trying to keep track of how many times someone visits the site; instead, they just want to get a real feel for how many unique visitors come to their site. They already have a tool that claims to do this for them but they think there is something wrong with it and are trying to use your project to get this done. You know that, if you can get this done in the quickest and cheapest manner possible, then they will happily talk you up on their blog enough that it will likely help you get your dream job because you’ve seen the same thing happen in the past. Your best friend in this task is going to be the Set. It does exactly what they are looking for. You just need to build the method for them to feed every IP address that visits their blog into the Set and it will do the rest. 

After you rock their expectations with your impressive knowledge of sets which let you quickly and easily build a tool to start gathering evidence for their unique visitor problem, they confide in you another problem they are struggling with. They have had a lot of different authors over the years and have no idea how many different tags they are using in their various blog posts. Their current web hosting company does not give a reliable method to search for tags in use, only to download them, but, with the massive number of blog posts they have, trying to even think about manually combing through them is an impossible task in the limited time they have. They then offer you more money and ask if you could also build them something to help figure out what tags they have in use. You know, if they are offering you more work, that means they are ready to start talking you up and that, if you get this right, they might even give you a referral to get hired on at your dream job. And yes, again, Stacks will be your friend.

Just then, you hear one of the head writers call up the CEO of the company you want to get hired on at and start to tell him all about how he thinks that the CEO should hire you when a panic erupts in the office abruptly ending the call. It turns out that the web hosting company for the blog got a virus that randomly inserts profanity in any string of text. They have already been planning on switching who was hosting their blog and this was the last straw. Unfortunately, the damage is already done and their normally children-oriented blog is now laced with profanity. In a panic, they ask if you could write them a program to remove all the profanity that the virus put into their blog and, knowing how Sets work, you know that it will be an easy job. ...Before you get to your car, you get a text from the HR department of the company you've wanted to get a job at for years, asking when you can come in for an interview.

Truly knowing how to use Sets matters. 

### What is a Set?
---
Sets are a built in data type within the Python programming language. Unlike lists, they are unordered which basically means that, to access the data inside, you reference the data itself and not the index. Because of the way Sets store values, duplicate data is not allowed in sets. Python handles all of the conflicts with adding data to the set automatically but there is a value in knowing about how Python handles conflict resolution, especially when you get into building your own data structures. Thanks to how Python handles Sets, it is able to add, remove, and test for membership in O(1) time. 

While the rest of this is not needed for learning about Sets, digging deeper into it will set you up for greater success when you start building your own data structures. 

On a basic level, what Python does with Sets is to store data based on its value. So, if we were to explain this in terms of a list that stores numbers, then you would say that 0 goes in index 0 and 1 goes in index 1. But, as you might already have figured out, that could get really cumbersome when it comes to memory requirements. Just imagine how much memory you would need to store the amount of the United States debt in a Set - terrifying to say the least. That is where hashing comes in. Hashing is a technique that Python uses to achieve O(1) performance in Sets while still not completely destroying every hope you have of storing larger numbers. To better explain how hashing works, we will explain it using terms you might use in a list or, more specifically, a sparse list. A sparse list is a list where not all indexes contain data. One way you could do this is to place the number into the list by using the modulo (%) operator and storing the larger numbers based on what is left after dividing it by 10. Then, you could have a sparse list of just size 10 and then, as long as you don't have numbers with the same digit in the ones place, you could easily store any number you want. This then gets into conflict resolution because, as you have likely already figured out, real life is not going to be that simple, especially when you factor in the idea that not everything can be hashed. For example, Lists, Sets and Dictionaries all cannot be hashed. 

So, this brings us to conflict resolution. There are two main methods of conflict resolution commonly used, open addressing and chaining. With open addressing, if we stick with our sparse list example, then we would just move the conflicting number to the next open spot, but, if you are not careful, then this could quickly go from an O(1) performance to an O(n) performance. That is where chaining comes in. Instead of moving conflicting numbers to a different spot in the sparse list, we would just chain it into the same spot. And, if you are building your own data structure and defining how the structure will handle conflicts, you can create specific rules to tell it how to chain data together in a way to continue to maintain O(1) performance, which is an important thing to keep in mind because, if you are not careful, then it could quickly get into O(n) performance. 


### Python Related Set Commands
---

|Common Set Operation|Description|Python Code|Performance|
|--------------------|-----------|-----------|-----------|
|add(value)|Adds "value" to the set|my_set.add(value)|O(1) - Performance of hashing the value (assuming good conflict resolution)|
|remove(value)|Removes the "value" from the set|my_set.remove(value)|O(1) - Performance of hashing the value (assuming good conflict resolution)|
|member(value)|Determines if "value" is in the set|if value in my_set:|O(1) - Performance of hashing the value (assuming good conflict resolution)|
|size()|Returns the number of items in the set|length = len(my_set)|O(1) - Performance of returning the size of the set|

If you want to dig deeper into set related commands (and we highly recommend you do), then you can check out either [W3 Schools](https://www.w3schools.com/python/python_ref_set.asp) for the short version or the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) for the more in depth version. Checking both would be a great idea. 

### Examples of Sets
---
The first task we had to do in our story was to write a program to find the unique visitors to a website and, for that, all we literally need to do is to add the IP addresses to a Set and the problem is solved. With the way Sets work in Python, if the value is already in there, it will not get added; if it is not, then it will be added. 
``` python
# List of IP addresses representing visitors to a website
visitors = ['192.168.0.1', '192.168.0.2', '192.168.0.1', '192.168.0.3', '192.168.0.2']

# Create a set from the list of visitors to remove duplicates and get unique visitors
uniqueVisitors = set(visitors)

# Print the set of unique visitors
print(uniqueVisitors)
# Expected Results: {'192.168.0.3', '192.168.0.2', '192.168.0.1'}
```

As with the first problem, finding unique tags is also easily solvable using Sets. 
``` Python
# List of blog posts, each post is a dictionary with a title and tags
blogPosts = [
    {'title': 'Post 1', 'tags': ['python', 'web development']},
    {'title': 'Post 2', 'tags': ['javascript', 'web development']},
    {'title': 'Post 3', 'tags': ['python', 'data science']},
    {'title': 'Post 4', 'tags': ['javascript', 'web development']}
]

# Create an empty set to store unique tags
uniqueTags = set()

# Loop through each post in the list of blog posts
for post in blogPosts:
    # Loop through each tag in the current post's tags
    for tag in post['tags']:
        # Add the tag to the set of unique tags
        uniqueTags.add(tag)

# Print the set of unique tags
print(uniqueTags)
# Expected Results: {'python', 'web development', 'javascript', 'data science'}
```

The last problem we had involved removing undesirable words from a bunch of blog posts. We could use one of the prior two solutions to build a set of undesirable words and then use this simple code to remove all the undesirable words from the text and feed it back to their post. Obviously, the implementation would be a little different and robust, but the same principle would apply. 
``` Python
# Text to be filtered
text = "the quick brown fox jumps over the lazy dog"

# Set containing words to be filtered
wordsToFilter = {'the', 'over'}

# Split the text into a list of words
words = text.split()

# Create an empty list to store the filtered words
filteredWords = []

# Iterate over each word in the list of words
for word in words:
    # Check if the word is not in the set of words to filter
    if word not in wordsToFilter:
        # If the word is not in the set, add it to the list of filtered words
        filteredWords.append(word)

# Join the list of filtered words into a string
filteredText = ' '.join(filteredWords)

# Print the filtered text
print(filteredText)
```

### Digging Deeper into Sets
---
For this challenge our goal is take two Sets and find the shared data within two Sets. To start with, I want to review some of the other methods that exist inside of Sets and it does not take long before I find that there is a method called `intersection` that takes in two Sets and returns the common elements in both Sets inside of a new Set. That sounds like exactly what we are trying to do. With that in mind, I have generally found python.org lackluster when it comes to explaining things or at least organizing them in a way to find them easily. So, after a quick search online, I found a wonderful [tutorial on w3schools.com](https://www.w3schools.com/python/ref_set_intersection.asp) detailing how to use the intersection method. From there, I want to put this in a function to make it more easily reusable and then I am done. 

``` Python
# Define a function that takes two sets as arguments and returns their intersection
def sharedValues(set1, set2):
    # Use the set method 'intersection' to find the common elements between the two sets
    result = set1.intersection(set2)
    # Return the result
    return result

# Create two sets of numbers
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Call the sharedValues function with the two sets as arguments and print the result
print(sharedValues(set1, set2))

# Expected Return: {40, 50, 30}
```

### Digging Even Deeper into Sets
---
For this challenge, the goal is to take two different lists of numbers and use Sets to find the shared numbers between them. For example, if you had a list containing the numbers 1 through 10 and a second list containing the numbers 9 through 15, then your program should find the numbers 9 and 10 and return those in a form that can be printed to the screen looking as follows [9, 10]. 

``` python
def diff(list1, list2):
    # Solution goes here

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(diff(list1, list2))
# Expected output [1, 2, 5, 6]
```

[Solution](findDifferences.py)

### Digging Even Deeper Still into Sets
---
For this challenge, the goal is to take in an list of numbers and its length to then find the longest consecutive sequence of numbers from that list using a Set. For example, with the number list [1, 9, 3, 10, 4, 20, 2], your goal would be to print the sequence [1, 2, 3, 4]. If you need to modify the arguments for the function, or even add additional functions, that is fine. The real goal is to take a list like this [1, 9, 3, 10, 4, 20, 2] and produce a printable sequence returned by the call of the function that looks like this [1, 2, 3, 4] and enable the program to work with any sized sequence of random numbers to produce the longest Set in order from smallest to largest.
``` python
def findLongestSequence (arr, n):
    # Solution goes here
    

# Test the function with an example list
arr = [1, 9, 3, 10, 4, 20, 2]
n = len(arr)
print(findLongestSequence(arr, n))
# Expected output: 4 (the longest consecutive subsequence is [1, 2, 3, 4])
```

Work out a solution for yourself, and then join us in a discussion about different possibilities to solve this problem afterwards. 

[Back to Welcome Page](0-welcome.md)