#Boolean Output

if True:
    print('Conditional was true')
    
if False:
    print('Conditional was true')

#Variable in if statement

language = 'python'
if language == 'python':
    print('Conditional was true')
    
#Comparison operators and negative check

if language == 'Python':
    print('Conditional was true')
else:
    print('No Match')

#Elif Statement

language = 'JavaScript'
if language == 'Python':
    print('Language is Python')
elif language == 'JavaScript':
    print('Language is Java Script')
else:
    print('No Match')

#Elif Statement Part 2   
language = 'C++'
if language == 'Python':
    print('Language is Python')
elif language == 'JavaScript':
    print('Language is Java Script')
elif language == 'C++':
    print('Language is C++')
else:
    print('No Match')
    
#Boolean Operation - AND

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in == True:
    print('Admin Page')
else:
    print('Bad Credentials')
    
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in == True:
    print('Admin Page')
else:
    print('Bad Credentials')

#Boolean Operation - OR

user = 'Normal User'
logged_in = True

if user == 'Admin' or logged_in == True:
    print('Admin Page')
else:
    print('Bad Credentials')
    
user = 'Normal User'
logged_in = False

if user == 'Normal User' or logged_in == True:
    print('Admin Page')
else:
    print('Bad Credentials')
    
#Boolean Operator - NOT

logged_in = True

if not logged_in:
    print('Please login')
else:
    print('Not Logged in')

logged_in = False

if not logged_in:
    print('Please login')
else:
    print('Not Logged in')
    
#List comparison

a = [1,2,3]
b = [1,2,3]

print (a==b)
print (a is b) # two objects are not in same location

print(id(a))
print(id(b))
print(a is b)

#2nd example 

a = [1,2,3]
b = a

print (a==b)
print (a is b) # two objects are in same location

print(id(a))
print(id(b))
print(a is b)
print(id(a)==id(b))
