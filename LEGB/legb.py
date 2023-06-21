#LEGB - Local, Enclosing, Global, Built in

#Defining global and local variables
x = 'global x'

def test():
    y = 'local x'
    print(y)
test()

x = 'global x'
def test():
    y = 'local x'
    print(x) #checks x in local scope test() and afterwards checks global scope
test()
#print(y) # Gives error as y cant be printed as Y is in local scope and print is in global scope

x = 'global x'
def test():
    x = 'local x'
    print(x) #checks x in local scope test() and afterwards checks global scope
test()
print(x)

#Make local variable global inside function

#x = 'global x'
def test():
    global x
    x = 'local x'
    print(x) #checks x in local scope test() and afterwards checks global scope
test()
print(x) #local x picked as its defined global even if we comment the orginal global variable

#Error if global x inside function is not defined

#x = 'global x'
def test():
    #global x
    x = 'local x'
    print(x) #checks x in local scope test() and afterwards checks global scope
test()
print(x)

# Defining variable in function

def test(z):
    x = 'local x'
    print(z)
    
test('local z')
#print(z) cant print local variable in function outside the fucntion in global variable
 
#Built in scope

# m = min ([5,7,3,5,2,1])
# print(m)
# #print(dir(builtins)) #gets all built in functions

# def min():
#     pass #doesnt get any Error

# m = min ([5,7,3,5,2,1]) # min fucntion we created was been searched in dir and ignored that min fucntion from global scope
# print(m)

m = min ([5,7,3,5,2,1])
print(m)
#print(dir(builtins)) #gets all built in functions

def my_min():
    pass



#Nested Function scope

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer()

#comment local function variable x
def outer():
    x = 'outer x'
    def inner():
       # x = 'inner x'
        print(x) # printed outer x as its enclosing function as it doesnt have any local function
    inner()
    print(x)
outer()

#comment global function variable
def outer():
    # x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) # error as px is not defined
    inner()
    print(x)
outer()

#Non local statement

def outer():
    x = 'outer x'
    def inner():
        nonlocal x #makes x in inner fucntion as non local so that its global
        x = 'inner x'
        print(x) 
    inner()
    print(x)
outer()


# Work with Global variable with enclosed function variable and inner function
x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) 
    inner()
    print(x)
outer()
print(x)

x = 'global x'
def outer():
    x = 'outer x'
    def inner():
       # x = 'inner x'
        print(x) 
    inner()
    print(x)
outer()
print(x)

x = 'global x'
def outer():
    # x = 'outer x'
    def inner():
       # x = 'inner x'
        print(x) 
    inner()
    print(x)
outer()
print(x)


