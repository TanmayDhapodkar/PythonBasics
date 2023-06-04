#Sets are value are unordered and no duplicate values

engg_courses ={'Maths 1', 'Maths 2', 'Maths 3', 'Maths 4'}
print(engg_courses)

#Remove duplicates
engg_courses ={'Maths 1', 'Maths 2', 'Maths 3', 'Maths 4','Maths 2'}
print(engg_courses)

#Test a vlaue of set # Membership Test
engg_courses ={'Maths 1', 'Maths 2', 'Maths 3', 'Maths 4'}
print('Maths 1' in engg_courses) #Check if Maths 1 is there in set
print('Maths 5' in engg_courses)

#Check common values within sets
courses = {'History', 'Chemistry','Math','Physics'}
engg_courses = {'Algebra', 'Math', 'Geometry'}
print(courses.intersection(engg_courses)) #Math is common

#Difference Menthod
courses = {'History', 'Chemistry','Math','Physics'}
engg_courses = {'Algebra', 'Math', 'Geometry'}
print(courses.difference(engg_courses)) #Difference in both the sets

#Union Method to get both set values
courses = {'History', 'Chemistry','Math','Physics'}
engg_courses = {'Algebra', 'Math', 'Geometry'}
print(courses.union(engg_courses))

#Empty Set
empty_set = {} #This is an empty set. It will be termed as dictonaries
