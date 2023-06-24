#Handling errors in Python using Try & Except Block

try:
    f = open('main.py')
except Exception:
    print('Sorry. File not found')

try:
    f = open('main.py') #No error
    var = bad_var #Error as bad_var not found
except Exception:
    print('Sorry. File not found')

try:
    f = open('main.py')
    var = bad_var
except FileNotFoundError:
    print('Sorry. File not found')
except Exception:
    print('Sorry. Something went wrong')

#Default message 

try:
    f = open('main.py')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
    
#Print the file as there are no expection

try:
    f = open('main.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    
#Finally statement - close the code irrespective of valid or Exception

try:
    f = open('main2.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')

#Raise an exception:

try:
    f = open('main.py')
    if f.name == 'main.py':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
