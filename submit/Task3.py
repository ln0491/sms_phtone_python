"""
Intro to Python Lab 1, Task 3

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#1

def get_form_bangalore(input_list):
    temp_list = set()
    for call in input_list:
        if str(call[0]).startswith("(080)"):
            temp_list.add(call[1])
    return temp_list

from_bangalore_list=get_form_bangalore(calls)

area_list=list()
for num in from_bangalore_list:
    if  str(num).startswith("(0"):
        temp=str(num)[0:str(num).index(")")+1]
        area_list.append(temp)
    elif " " in num:
        '''
        判断号码中有无空格
        差截取前4位
        '''
        temp=num[0:4]
        area_list.append(temp)

# sorted and no duplicates
'''
先去重，再排序
'''
result_set=sorted(set(area_list))
# result and print
'''
只在开始输出一次
'''
print("The numbers called by people in Bangalore have codes:")
for result in result_set:
    print(result)


# 2
    '''
    获取以(080)开头的主叫号码并以 (080)接听的电话
    :param input_list:  这是个列表
    :return: 一个列表 不在去重
    '''
def get_revice_numbers(input_list):

    temp_list = list()
    for call in input_list:
        if str(call[0]).startswith("(080)") and str(call[1]).startswith("(080)"):
            temp_list.append(call[1])
    return temp_list
'''
获取所有 bangalor打出的电话
'''
def get_send_numbers(input_list):
    '''
    获取以(080)开头的主叫号码
    :param input_list:  这是个列表
    :return: 一个列表 不在去重
    '''
    temp_list = list()
    for call in input_list:
        if str(call[0]).startswith("(080)") :
            temp_list.append(call[1])
    return temp_list

bangalor_revice_list=get_revice_numbers(calls)
bangalor_send_list=get_send_numbers(calls)

print("{} percent of calls from fixed lines in Bangalore are callsto other fixed lines in Bangalore.".format('%.2f' %(len(bangalor_revice_list)/len(bangalor_send_list)*100) ))