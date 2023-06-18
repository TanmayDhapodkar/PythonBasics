import csv

#read a csv file and print line by line
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line) 
        print(line[2])
        print(line[3])

#skip the first line in csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for line in csv_reader:
        print(line) 
        
#write a file using a read csv file
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
with open('new_file.csv','w') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '-') #will put '' where - is there in csv
    
    for line in csv_reader:
        csv_writer.writerow(line)

# tab used as delimiter 
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
with open('tab_file.csv','w') as tab_file:
    csv_writer = csv.writer(tab_file, delimiter = '\t') 
    
    for line in csv_reader:
        csv_writer.writerow(line)
        
#read the new file writen which has tab delimiter 
with open('tab_file.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
     for line in csv_reader:
        print(line) #will print every line as one string as t doesnt identify tab as delimiter
        
#dict reader method to write the csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #dict reader will give each row a header of csv file
    
      for line in csv_reader:
        print(line) #easy to parse out the csv file using dictreader

#dict writer method to write the csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
with open('new_file.csv','w') as new_file:
    
    fieldnames = ['first_name', 'last_name','email']
    csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter= '-')
    csv_writer.writeheader()
    
    for line in csv_reader:
        csv_writer.writerow(line)
        
#Remove the email using DictWriter
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
with open('new_file.csv','w') as new_file:
    
    fieldnames = ['first_name', 'last_name'] #remove email from the list
    csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter= '-')
    csv_writer.writeheader()
    
    for line in csv_reader:
        del line['email'] #del email using for loop
        csv_writer.writerow(line)
