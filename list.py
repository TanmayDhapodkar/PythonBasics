courses = ['History', 'Chemistry','Math','Physics']
print(courses)

#Length of list
print(len(courses))

#Access the values in list
print(courses[0])
print(courses[3]) #total length of list -1
print(courses[-1]) #last item of list
#print(courses[5])

#Access range of values in list ##Slicing
print(courses[0:2]) #not include the 2nd index
print(courses[2:]) #2nd and till end
print(courses[:2]) #0th till 2nd value

#Append in list
courses.append('Art') #Default append of Art at the end
print(courses)
print(courses.insert(1,'Geography')) #Insert Geography value in 1st
print(courses)

#Insert list in the list
courses = ['History', 'Chemistry','Math','Physics']
courses_2 = ['Art','Data Science']
courses.insert(0,courses_2)
print(courses) # courses_2 is at the 0th value in courses

#Extend in the list
courses = ['History', 'Chemistry','Math','Physics']
courses_2 = ['Art','Data Science']
courses.extend(courses_2)
print(courses)

#Append
courses = ['History', 'Chemistry','Math','Physics']
courses_2 = ['English','ML']
courses.append(courses_2) #Append courses_2 at the end of courses list
print(courses)

#Pop & Remove
courses = ['History', 'Chemistry','Math','Physics']
courses.remove('Math')
print(courses)

courses = ['History', 'Chemistry','Math','Physics']
courses.pop() #Default removes last value in list
print(courses)

#Sort & Reverse
courses = ['History', 'Chemistry','Math','Physics']
courses.reverse()
print(courses)

courses = ['History', 'Chemistry','Math','Physics']
courses.sort() #Sort Alphabetically order
print(courses)

courses = ['History', 'Chemistry','Math','Physics']
num= [1,3,4,5,2,5]
num.sort() #Smallest  to Largest
courses.sort(reverse=True) #Sorted reverse Alphabetically order
print(num)
print(courses)

#Sorted Function
courses = ['History', 'Chemistry','Math','Physics']
sorted_courses = sorted(courses)
print(sorted_courses) #Sort Alphabetically

#Sum of list
print(sum(num))

#Index Menthod
courses = ['History', 'Chemistry','Math','Physics']
courses.index('Chemistry') #Index of the value in list
#courses.index('Art') #Error as Art is not present in list

#in operator in the list
#print('Art' in courses) #Error
print('Math' in courses)

#For loop in list
for item in courses:
    print(item) #Print each item in new line of list

for courses in num:
    print(courses) #Print each item in new line of list

#Enumerate gives Index and values in list
for index, courses_2 in enumerate(sorted_courses):
    print(index, courses_2)

for index, num in enumerate(num, start=2):
    print(index, num) #indexing start from 2

#Strings in list seperated by ,
courses = ['History', 'Chemistry','Math','Physics']
course_str = ', '. join(courses)
print(course_str)

#Strings in list seperated by -
courses = ['History', 'Chemistry','Math','Physics']
course_str = ' - '. join(courses)
print(course_str)

#Strings in list seperated by { } spaces
courses = ['History', 'Chemistry','Math','Physics']
course_str = ' '. join(courses)
print(course_str)

#Convert modified list into original list
courses = ['History', 'Chemistry','Math','Physics']
course_str = ', '. join(courses)
print(course_str)
old_str = course_str.split(', ') #spilt fucntion to go back to old list
print(old_str)

#Empty List creation
empty_list = ()
empty_list - list()
