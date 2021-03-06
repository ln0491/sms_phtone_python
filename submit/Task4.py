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

no_sms_list=set()
for text in  texts:
    no_sms_list.add(text[0])
    no_sms_list.add(text[1])
# 集合去重相减 ：
'''
先去重，再排序
'''
marketing_list=sorted(set(send_phone_list-revice_phone_list-no_sms_list))
# 3 result

'''
仅在开头输出一次
'''
print("These numbers could be telemarketers:")
for market_phone in marketing_list:
    print(market_phone)
