import os 

#os.chdir('/Users/HP/PycharmProjects/Videos')
print(os.getcwd()) #Get the file path of the videos stored

for f in os.listdir():
    print(f) #list all the file names in the dir
  
#Spilt the extention from file names, tuples are created after using spiltext 
for f in os.listdir():
    print(os.path.splitext(f)) 

#Save the spilt tuples in variable    
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    
#Spilt the filename in file_name with -
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
    
#Give variables to the spilt texts
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_title, file_course, file_num = file_name.split('-')
    print(file_title)
    print(file_course)
    print(file_num)
    
#print formatted string from file names stored into variables
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_title, file_course, file_num = file_name.split('-')
    
    file_title = file_title.strip()
    file_course = file_course.strip()
    file_num = file_num.strip()[1:] #Remove # from the file name
    
    print('{}-{}-{}{}'.format(file_num,file_course,file_title,file_ext))

#Add 0 to the numbers using zfill
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_title, file_course, file_num = file_name.split('-')
    
    file_title = file_title.strip()
    file_course = file_course.strip()
    file_num = file_num.strip()[1:].zfill(2) #this function adds 0 at start
    
    print('{}-{}{}'.format(file_num,file_title,file_ext))

#Store the renamed file name into a variable and dynamically use to change in dir
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_title, file_course, file_num = file_name.split('-')
    
    file_title = file_title.strip()
    file_course = file_course.strip()
    file_num = file_num.strip()[1:].zfill(2) #this function adds 0 at start
    
    new_name = ('{}-{}{}'.format(file_num,file_title,file_ext))
    
    os.rename(f,new_name)
