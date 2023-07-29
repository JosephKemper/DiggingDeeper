# String Methods
In this tutorial, we are exploring the built in Python methods for modifying strings. 

## Capitalize
The Python `capitalize()` method capitalizes the first letter of any string fed into it, whether that be a single letter, word, or whole sentence, it will capitalize the first letter of any string. It uses the ASCII characters to capitalize letters, so if the string you are working with gets beyond the ASCII characters, then the Python interpreter will simply return the string unmodified, for example if you feed a string of numbers with a few letters mixed in, if a number is the first character, then the interpreter will return the string unmodified. 

To use the `capitalize()` method you first assign the string you wish to capitalize to a variable and then use the dot `.` operator and call the `capitalize()` method afterwards. For example:

``` python
example_string = "this is an example of how the capitalize method for strings works in Python."
print(example_string.capitalize())
# Expected output: "This is an example of how the capitalize method for strings works in python."
```

And for non-ASCII characters, (or any character that does not have a predefined upper and lower case version) you would see something like this when using the `capitalize()` method.

```Python
bad_string = "12a45kb"
print(bad_string.capitalize())
# Expected output: "12a45kb"
```