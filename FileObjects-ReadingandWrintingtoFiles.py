# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:12:34 2022

@author: mcurral
"""
# to work the images,... we need to convert to binary and write etc!
with open('sunglasses.jpg', 'rb') as rf: #('test.txt', 'r') as rf:
    with open('sunglasses_copy.png', 'wb') as wf: #'test_copy.txt', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size) # a copy until nothing to read.... from
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
        # for line in rf: # can't decode byte in the position 0, so in order to work with images we're going to have to open these files and binary mode 
        #     wf.write(line)
# with open('test2.txt', 'w') as f:
#     f.write('Test')#pass # # nsupportedOperation: not writable when open as mode read
#     f.seek(0)
#     f.write('R')
    # f_contents = f.read(100)
    # print(f_contents, end='')
    
    # f_contents = f.read(100)
    # print(f_contents, end='')
    
    # f_contents = f.read(100)
    # print(f_contents, end='') # if I add more other f.read(100) , program will return (read and print) instead a empty string!
# since we dont know exacctly how long the file will be we're going
# put a variable here called
    # size_to_read = 10

    # f_contents = f.read(size_to_read)
    # print(f_contents, end="")
    
    # f.seek(0) #start in beginning of
    
    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # print(f.tell())
    # # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)
# a loop that iterates over small chuncks at time
    #pass
    # for line in f:
    #     print(line, end='')
        
    # f_contents = f.readline()
    # print(f_contents, end='')
#f = open('test.txt', 'r')
# File Objects
#print(f.closed)
#print(f.read())
#print(f.name)
#     pass 
# #f = open('test.txt', 'r')
#f.close()
# print(f.read())#closed) #name)

#f.close()
    # f_contents = f.readline()
    # print(f_contents, end='')
    
    