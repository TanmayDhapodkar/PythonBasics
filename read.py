#File Objects

#Open the file given and read
f = open('test.txt','r')
print(f.name) #print name of the file
f.close()

#Open the file given and write
f = open('test.txt','w')
print(f.name) #print name of the file
f.close()

#Open the file given and read and write
f = open('test.txt','r+')
print(f.name) #print name of the file
f.close()

#Open the file given and appending to a file
f = open('test.txt','a')
print(f.name) #print name of the file
f.close()

#Fina a mode of the file
f = open('test.txt','w')
print(f.mode)
f.close()

#Open a file using context manager #Recommended
with open ('test.txt', 'r+') as f:
    pass
print(f.closed)
print(f.mode)

#Try to check if youi can read a file with context manager
#with open ('test.txt', 'r+') as f:
#    pass
#print(f.read()) # cant read because we have closed the file
