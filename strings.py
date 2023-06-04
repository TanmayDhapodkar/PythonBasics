#First Code
print('Hello World')

#Assign Variable and print
message = 'Hello World'
print(message)

#Use Single Quotes in Strings
message_2 = 'Tanmay''s World'
print(message_2)
message_3 = 'Tanmay\'s World'
print(message_3)

#Multiline Strings
message_4 = '''Today is a good day 
and the weather seems to be perfect'''
print(message_4)

#Find how many characters are in string
print(len(message))

#Location of the character in string
print(message[0])
print(message[0:2]) #0 & 1 location character displayed
print(message[3:5]) #3 & 4 character location is printed

print(message[2:]) #2 and onwards is printed
print(message[:5]) #0 to 4 is printed
#print(message[11]) #11th char not present hence giving error

#Methods in string
print(message.lower())
print(message.upper())
print(message.count('Hello')) #find how many times hello is there in message
print(message.count('l')) #find how many l are there

print(message.find('World')) #return location of first char in World in message
print(message.find('Universe')) #error because the work universe is not in message variable hence return -1

message_replace = message.replace('World','Universe') #Replace any word/letter in string
message_l = message.replace('l','z')
print(message_replace)
print(message_l)

#Concatenation of Variable strings
greeting = 'Hello'
name = 'Tanmay'
print(greeting + name)
print(greeting + ' ' + name)
print(greeting + ' ' + name + '. Welcome! ')

new_message = '{},{}. Welcome!'.format(greeting,name) #placeholder for variable strings
print(new_message)

