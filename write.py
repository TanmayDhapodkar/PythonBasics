#Try file which is in read mode
#with open('test.txt', 'r') as f:
#    f.write('Test') #Error as it is read mode

#Create a write file
with open('test2.txt', 'w') as f:
    pass

#Create a write file and print Test
with open('test2.txt', 'w') as f:
    f.write('Test')

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test') #Prints Test side by side

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0) #Seek defaults to zero and write Test again
    f.write('Test')

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0) #Seek defaults to zero and write Test again
    f.write('R') # 0th chr is replaced with R
