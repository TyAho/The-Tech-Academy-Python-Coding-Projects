import os
import sys
import time

os.listdir('C:\\Users\\nidge\\Documents\\script')

myFiles = ['first.txt', 'second.txt', 'third.rtf', 'fourth.xlsx', 'fifth.rar', 'sixth.pptx', 'seventh.rtf', 'eighth.docx', 'ninth.xlsx', 'tenth.xlsx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\nidge\\Documents\\script', filename))

#Path for  first txt file

path = ('C:\\Users\\nidge\\Documents\\script\\first.txt')

# find the time of the last edit

try:
    modification_time = os.path.getmtime(path)
    print("Last modification time:", modification_time)


except OSError: 
    print("Path '%s' does not exists or is inaccessible" %path) 
    sys.exit() 

# converts the time in seconds
# to local time

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)


#path for second txt file

path = ('C:\\Users\\nidge\\Documents\\script\\second.txt')

# find the time of the last edit

try:
    modification_time = os.path.getmtime(path)
    print("Last modification time:", modification_time)


except OSError: 
    print("Path '%s' does not exists or is inaccessible" %path) 
    sys.exit() 

# converts the time in seconds
# to local time

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)
