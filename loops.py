#For Loop
nums = [1,2,3,4,5]
for num in nums:
    print(num)

#Two Keywords used in for loop - break & continue
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('Found!') # if 3 is found print Found!
        break # break and print numbers 1,2
    print(num)

nums = [1,2,3,4,5]
for num in nums:
    if num == 5:
        print('Found!') # if 5 is found print Found!
        continue # Continue after finding 5
    print(num)

#For loop within a for loop

nums = [5,6,7,8]
for num in nums:
    for letter in 'abc': #a b c are seperately tagged with 5 6 7 8
        print(num,letter)

#Range in a For Loop
for i in range(13): #print range of num from 1 to 12
    print(i)

#Range in for loop with starting number
for i in range(5,13): # starting with 5 but not including 13
    print(i)

#While Loop
x = 0
while x < 10: #iterate the loop till < 10
    print(x)
    x+=1

#Break in while loop
x = 10
while x < 15: #iterate the loop till < 10
    if x == 13: #if x == 13 then break
        break
    print(x)
    x += 1

#Infinite while Loop - Dont run

x = 2
while True: #infinite loop
    print(x)
    x+=1