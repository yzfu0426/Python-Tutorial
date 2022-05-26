import my_module as mm
import sys

#directly import the function, but imported message still got printed out
#from my_module import find_index as fi, test

#makes it hard to track down problems
#from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index_of_CompSci = mm.find_index(courses, 'CompSci')
print(f'Index of CompSci is {index_of_CompSci}')

#a list
print(sys.path)