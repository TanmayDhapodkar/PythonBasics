#Tuple is list which are immutable ()
subject = ('Value Education', 'Geometry', 'Biology')
print(subject)

#Assign a tuple to another
subject = ('Value Education', 'Geometry', 'Biology')
subject_2 = ('Algebra')
subject_2 = subject
print(subject_2)

subject_3 = subject_2
print(subject_3)

#Replace 0th value in Tuple
subject[0] = 'Drawing'
print(subject)

#Empty Tuple creation
empty_tuple=()
empty_tuple-tuple()