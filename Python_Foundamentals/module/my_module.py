print('Imported my module...')

test = 'Test String'

def find_index(to_search, target):
    """find the index of a string in a sequence of strings"""

    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1