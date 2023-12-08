""" Generators and Iterators in Python """
""" GENERATORS:
>>> Generators are a way to create iterable sequences of data in Python without 
    storing them entirely in memory. This can be very efficient when working with large or 
    potentially infinite sequences.

>>> When we want to return multiple values then we use return statement
    Instead of 'return' statement we use 'yield' statement. 
>>> "yield" statement is used to turn a regualar function into GENERATORS.
"""

# Here's a simple example of a generator function that generates a sequence of numbers from 1 to n:
# def number_sequence(n):
#     for i in range(1, n + 1):
#         yield i

""" Iterators: 
>>> Iterators are objects that can be iterated (looped) over.
>>> They implement the __iter__() and __next__() methods. 
>>> The __iter__() method returns the iterator object itself
>>> the __next__() method returns the next value from the iterator.
>>> When there are no more items to return, the __next__() method raises the StopIteration exception.
>>> In Python, many built-in data types like lists, tuples, and dictionaries are iterable, 
    and you can create custom iterators.
"""

# EXAMPLE 
# class MyIterator:
#     def __init__(self, n):
#         self.n = n
#         self.i = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i <= self.n:
#             result = self.i
#             self.i += 1
#             return result
#         else:
#             raise StopIteration

# # Usage:
# my_iter = MyIterator(5)
# for num in my_iter:
#     print(num)

""" Context Managers: Implement context managers for clean resource 
management using the with statement. """

""" Metaclasses: Explore the concept of metaclasses to customize class creation. """

""" Multiple Inheritance: Understand how to work with multiple inheritance
    and method resolution order (MRO). """
    
""" Descriptors: Learn about descriptors and how they allow you to control attribute access. """    
    
""" Dynamic Attribute Handling: Explore dynamic attribute 
    handling, getattr, setattr, and delattr methods. """    

""" Functional Programming: Dive into functional programming concepts, such as lambda 
    functions and map/reduce/filter. """

""" Concurrency with Threads: Learn about multithreading for concurrent execution of tasks. """    
 
""" Concurrency with Multiprocessing: Understand multiprocessing for parallel task execution. """

""" Asynchronous Programming with Asyncio: Explore asynchronous programming using the asyncio library. """    

""" Decorators for Timing and Profiling: Use decorators to measure function
    execution time and performance. """
 
""" Advanced Exception Handling: Handle exceptions effectively with custom exception
    classes and context management. """    
    
""" Functional Decorators: Implement decorators to enforce functional programming principles. """    
    
""" Context Managers for Database Transactions: Create context managers for database transactions. """    

""" File Handling: Explore advanced file handling, binary data, and working with CSV and JSON files. """    
    
""" LEARNED UPTO POINT-18 """    

    
    
    