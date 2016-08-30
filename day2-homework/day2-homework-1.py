#!/usr/bin/env python
#20160830_gfuller9_day2-homework-1.py
#Usage: ./day2-homework-1.py {filename}
#Importing sys and opening the file
import sys
file = open(sys.argv[1])

#enumerating through file
for i, item in enumerate(file):
    #ignoring anything in the header
    if "DROME" in item:
        #splitting the lines 
        items = item.split()
        #checking to make sure dataset is full
        if len(items)==4:
            #printing the output, FlyBase ID    ProtID
            print items[-1], "\t", items[-2]
            last = items[-1]
        
            
        
            
        
        

        
    
        
        

        
        
        