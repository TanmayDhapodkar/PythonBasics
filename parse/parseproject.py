import csv
html_output = ''
names = []

with open('names.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data)) #get list of csv data instead of loop
    
    next(csv_data) #remove header in csv file
    next(csv_data) #remove introduction in csv file
    
    for line in csv_data:
        print(line) #print csv line by line
        
#append names from the list in csv file
with open('names.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data)) #get list of csv data instead of loop
    
    next(csv_data) #remove header in csv file
    next(csv_data) #remove introduction in csv file
    
    for line in csv_data:
        names.append(f"{line[0]} {line[1]}")
        
for name in names:
    print(name)
        
#remove data from a given line within a csv file 
with open('names.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data)) #get list of csv data instead of loop
    
    next(csv_data) #remove header in csv file
    next(csv_data) #remove introduction in csv file
    
    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")
        
for name in names:
    print(name)
    
#Convert this first and last names file into html_output
with open('names.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data)) #get list of csv data instead of loop
    
    next(csv_data) #remove header in csv file
    next(csv_data) #remove introduction in csv file
    
    for line in csv_data:
        if line[0] == 'No Reward': #whereever there is no reward break
            break
        names.append(f"{line[0]} {line[1]}") #append all the data in names
        
html_output += f'<p>There are currently {len[names]} contributors. Thank You!<p>' #sentence to tell lines in html
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}<\li>' #convert into html

html_output += '\n<ul>'
print(html_output)

#Use DictReader DictWriter instead of Reader and writer classmethod

html_output = ''
names = []

with open('names.csv','r') as data_file:
    csv_data = csv.DictReader(data_file)
    
    for item in csv_data:
        print(item)
        
#2

html_output = ''
names = []

with open('names.csv','r') as data_file:
    csv_data = csv.DictReader(data_file)
    
     next(csv_data) #remove introduction in csv file
     
     for line in csv_data:
        if line['FirstName'] == 'No Reward': #whereever there is no reward in firstaname break
            break
        names.append(f"{line['FirstName']} {line['LastName']}") #append all the data with firstname and lastname
