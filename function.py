#Function
def hello_func():
    pass
print(hello_func)

def hello_func():
    print("Hello Function")
hello_func()

#DRY - Dont repeat yourself

def dont_repeat():
    print("Non Repeative Value")

dont_repeat()
dont_repeat()
dont_repeat()
dont_repeat()
dont_repeat()

# Return used in function

def function_one():
    return 'Hello World!'
    
function_one() # prints nothing

def function_one():
    return 'Hello World!'
print(function_one())

#add method - upper in function

def function_one():
    return 'Hello World!'
print(function_one().upper())

#add parameter in function

def hello(greeting):
    return '{}, Function.'.format(greeting)
print(hello('Hi'))

def learning(Subject, Name):
    return '{} {} is great.'.format(Subject, Name)
print(learning('Data','Science'))

#Multiple Parameter with default set

def full_name(First, Last = ''):
    return '{} {} is my name.'.format(First,Last)
print(full_name('Tanmay'))

#Replace default in paramter of function 

def full_name(First, Last = ' '):
    return '{} {} is my name.'.format(First,Last)
print(full_name('Tanmay', Last = 'Dhapodkar'))

#Function with Positional keyword

def info(*args, **kwargs): #can be kept anything
    print(args) #Arguments
    print(kwargs) #Keyword Arguments
    
info('Math', 'Art', Name = 'Tanmay', age = 27)
#Here Math and Art are args and Name and age are kwargs


def student_info(*args, **kwargs): #can be kept anything
    print(args) #Arguments
    print(kwargs) #Keyword Arguments

courses = ['Math', 'Art']
info = {'name': 'Tanmay', 'age': 27}

student_info(courses,info) #Clubbed both as it is not identify args kwargs

def student_info(*args, **kwargs): #can be kept anything
    print(args) #Arguments
    print(kwargs) #Keyword Arguments

courses = ['Math', 'Art']
info = {'name': 'Tanmay', 'age': 27}

student_info(*courses,**info) #Unpacks as we add * & ** to args and kwargs
