"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# 1 get all send and revice phone list and
send_phone_list=set()
revice_phone_list=set()
for call in calls:
    send_phone_list.add(call[0])
    revice_phone_list.add(call[1])

# 2 get all no revice sms list

no_revice_sms_list=set()
for text in  texts:
    no_revice_sms_list.add(text[1])
# 集合的交集：
marketing_list=list(send_phone_list.intersection(revice_phone_list).intersection(no_revice_sms_list))
# 3 result
for market_phone in set(marketing_list):
    print("These numbers could be telemarketers: {} ".format(market_phone))
