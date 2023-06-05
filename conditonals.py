#Conditional Evaluation of True & False

#False Values
    #False
    #None
    #Zero of any numeric type
    #Any empty sequence like '',(),[]
    #Any empty mapping like {}

condition = False

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
    
condition = None

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

condition = 0 #Zero will evaluate to False

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
    
condition = 2 #Any specific numeric will evaluate to True

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
    
condition = ''

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

condition = []

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
    
condition = {}

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
    
#True Evaluation will be all apart from False Values

condition = [1,2,4]

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
