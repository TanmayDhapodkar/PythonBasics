#Read the content of file with context manager
with open ('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

#Read the file in a given list
with open ('test.txt', 'r') as f:
    f_contents = f.readlines() #Redlines give file info in list
    print(f_contents, end='')

#Read a first line in a file
with open ('test.txt', 'r') as f:
    f_contents = f.readline() #Readline gives first file in list
    print(f_contents, end='')

#Read 2 lines in a file
with open('test.txt', 'r') as f:
    f_contents = f.readline() #End is not added so we have a space after this
    print(f_contents)

    f_contents = f.readline() #End is not added so we have a space after this
    print(f_contents)

#Read 2 lines in a file without spaces
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents,end='')

#Read each line one by one
with open('test.txt', 'r') as f:
    for line in f:
        print(line,end='')

#Reach a particular thing a file
with open('test.txt', 'r') as f:
    print('\n')
    f_contents = f.read(10)
    print(f_contents)

#Size to read variable instead of hardcoded
with open('test.txt', 'r') as f:
    print('\n')
    size_to_read  = 20
    f_contents = f.read(size_to_read)

#Find the variable and add / on every nth character
with open('test.txt', 'r') as f:
    size_to_read  = 20
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='/') #Find 10 character and add / to it
        f_contents = f.read((size_to_read))

#Find the position of vaiable in a file
with open('test.txt', 'r') as f:
    print('\n')
    size_to_read  = 20
    f_contents = f.read(size_to_read)
    print(f.tell())

#Find 10 char and find another 10 char
with open('test.txt', 'r') as f:
    print('\n')
    size_to_read  = 20

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)
    print(f_contents)

#Find 10 chr and start again from start and print 10 chr

with open('test.txt', 'r') as f:
    print('\n')
    size_to_read  = 20

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)
    
    f_contents = f.read(size_to_read)
    print(f_contents)
