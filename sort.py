#Sort on DataTypes

#Sorted Func 
li = [4,2,5,6,8,5,3,2,1,7,2]
s_li = sorted(li)
print('Sorted Variable:\t', s_li)
print('Orginal Variable:\t', li)

#Sort method without creating a Variable
li = [4,2,5,6,8,5,3,2,1,7,2]
li.sort()
print('Sorted Variable:\t', s_li)
print('Sorted using method:\t', li)

#Using sort method in a Variable
li = [4,2,5,6,8,5,3,2,1,7,2]
s_li = li.sort()
print('Sorted Variable:\t', s_li) #Will show None as it doesnt include in return
print('Sorted using method:\t', li)

#Sorted func using descending order
li = [4,2,5,6,8,5,3,2,1,7,2]
s_li = sorted(li, reverse = True)
print('Sorted Variable:\t', s_li) #sorting reversed
print('Orginal Variable:\t', li)

#Sort method with reverse order
li = [4,2,5,6,8,5,3,2,1,7,2]
li.sort(reverse = True)
print('Sorted using method:\t', li)

#Sorted function gives more flexibilty than sort method


#Sort tuple

tup = (3,5,7,2,21,1,5,7,84,2)
#tup.sort() #Gives error as Tuple object has no attribute sort

#Using sorted func in Tuple
tup = (3,5,7,2,21,1,5,7,84,2)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

#Sort a dict
di = {'name': 'Tanmay', 'job': 'programming','age': None, 'os':'Windows'}
s_di = sorted(di)
print('Dict:\t', s_di) #gives key in sort format

#sort value on diff criteria

li = [-6,-3,0,2,-4,2,9]
s_li = sorted(li)
print(s_li)

#Convert into absolute value
li = [-6,-3,0,2,-4,2,9]
abs_li = sorted(li, key = abs)
print(abs_li)

#Sorting Objects

class Employee():
    def __int__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({},{},${})'. format(self.name, self.age, self.salary)
        
e1 = Employee('Carl', 35, 7000)
e2 = Employee('Mark', 23, 4300)
e3 = Employee('John', 27, 1095)

employees = [e1,e2,e3]
s_Employees = sorted(employees)
print(s_Employees)


