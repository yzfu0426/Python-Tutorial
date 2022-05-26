import sys
sys.path.append('/Users/fuuchiku/Desktop/Python Tutorial/my_module_new_dir')

from my_module1 import find_index


courses = ['History', 'Math', 'Physics', 'CompSci']

index_of_CompSci = find_index(courses, 'CompSci')
print(f'Index of CompSci is {index_of_CompSci}')


print(sys.path)