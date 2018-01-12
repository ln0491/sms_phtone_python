"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
# S phone number
records=set()

# sms
for text in texts:
    # Send phone number
    records.add(text[0])
    # receive_phone_number
    records.add(text[1])
# call
for call in calls:
    # calling phone number
    records.add(call[0])
    # Called telephone number
    records.add(call[1])

print("There are {} different telephone numbers in the records.".format(len(records)))