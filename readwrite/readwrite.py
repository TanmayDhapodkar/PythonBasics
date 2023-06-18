#Read from one file and write in another

with open('test.txt', 'r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

#Copy a picture file from one file to another

# with open('img.png', 'r') as rf:
#     with open('img_copy.png','w') as wf:
#         for line in rf:
#             wf.write(line) #Gives error as we have to convert picture into binary format

with open('img.png', 'rb') as rf: #rb for read binary image file
    with open('img_copy.png','wb') as wf: #wb for write binary image file
        for line in rf:
            wf.write(line)

#Read and write a particular chunk size

with open('img.png', 'rb') as rf: #rb for read binary image file
    with open('img_copy.png','wb') as wf: #wb for write binary image file
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size) #Read and write 4096 bytes
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) #While loop to read full file 
