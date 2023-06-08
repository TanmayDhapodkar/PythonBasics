#Import Modules

print('Importing the module')

test = 'Test String'

def findindex(to_search,target):
    '''Find a index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
