import zipfile
import os
import re
import hashlib
import requests
import codecs
import csv
import openpyxl
# задание 1
directory_to_extra_to = 'C:\\zip folder'
arch_file = 'C:\\test.zip'
test_zip = zipfile.ZipFile('test.zip', 'r')
test_zip.extractall(directory_to_extra_to)
test_zip.close()
# задание №2
txt_files = []

for r, d, f in os.walk(directory_to_extra_to):
    for file in f:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(r, file))
print(txt_files)
for file in txt_files:
    fop = open(file, "rb").read()
    print(file, ": ", str(hashlib.md5(fop).hexdigest()))

# задание №3
target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"
target_file = ''
target_file_data = ''
for r, d, f in os.walk(directory_to_extra_to):
    for file in f:
        file_data = open(os.path.join(r, file), "rb").read()
        result = hashlib.md5(file_data).hexdigest()
        if result == target_hash:
            target_file_data = file_data
            target_file = file
print(target_file_data)
print(target_file)
# задание №4
r = requests.get(target_file_data)
result_dct = {}
counter = 0
lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
lst = []
for line in lines:
    if counter == 0:
        headers = re.sub(r'<.*?>', ';', line)
        headers = re.sub(r'\(\+[0-9\s]+\)', ';', headers)
        while headers.find(";;") != -1:
            headers = re.sub(';;', ';', headers)
        headers = headers[5:len(headers) - 1]
        lst.append(headers)

n = int(input('input row n = '))
temp = lst[n]
tmp_list = temp.split(';')
country_name = tmp_list[0]
col1_val = re.sub(r"\xa0", "", tmp_list[1])
col2_val = re.sub(r"\xa0", "", tmp_list[2])
col3_val = re.sub(r"\xa0", "", tmp_list[3])
if tmp_list[3] == "0*":
    col3_val = 0
if tmp_list[4] == "_":
    col4_val = -1
else:
    col4_val = re.sub("\xa0", '', tmp_list[4])
result_dct = dict()
result_dct["country"] = country_name
result_dct["Sick"] = int(col1_val)
result_dct["Died"] = int(col2_val)
result_dct["Recovered"] = int(col3_val)
result_dct["Active case"] = int(col4_val)
print(result_dct)
# задание №5
new_tmp_list = []
for i in range(1, len(lst), 1):
    tmp = lst[i]
    tmp_lst = tmp.split(';')
    country_name = tmp_lst[0]
    col1_val = re.sub(r"\xa0", "", tmp_lst[1])
    col2_val = re.sub(r"\xa0", "", tmp_lst[2])
    col3_val = re.sub(r"\xa0", "", tmp_lst[3])
    if tmp_lst[3] == "0*":
        col3_val = '0'
    if tmp_lst[4] == "_":
        col4_val = '-1'
    else:
        col4_val = re.sub("\xa0", '', tmp_lst[4])
    new_tmp_list.append(country_name)
    new_tmp_list.append(col1_val)
    new_tmp_list.append(col2_val)
    new_tmp_list.append(col3_val)
    new_tmp_list.append(col4_val)
output = codecs.open('data.csv', 'w', 'utf-16')
for key in result_dct.keys():
    output.write(key)
    output.write('\t')
output.write('\n')
cut_list = new_tmp_list[0:5]
for i in range(5):
    output.write(str(cut_list[i]))
    output.write('\t')
output.write('\n')
for i in range(1, len(lst)-2):
    cuts_list = new_tmp_list[(5*i):(5*i+5)]
    for j in range(5):
        output.write(str(cuts_list[j]))
        output.write('\t')
    output.write('\n')
output.close()
output = codecs.open('data.csv', 'r', 'utf-16')
#print(output.read())
output.close()
# задание №6
target_country = input("Введите название страны: ")
for i in range(0, len(lst)-2):
    cuts_list = new_tmp_list[(5*i):(5*i+5)]
    for j in range(5):
        if target_country == cuts_list[j]:
            print(cuts_list)

"""for i in new_tmp_list:
    print(i)
for row in range(len(lst)):
    for col in range(5):
        temp_lst.append(new_tmp_list)"""


"""
output = codecs.open('data.csv', 'w', 'utf-16')
for key in result_dct.keys():
    output.write(key)
    output.write('\t')
output.write('\n')
for value in result_dct.values():
    output.write(str(value))
    output.write('\t')
output.close()
output = codecs.open('data.csv', 'r', 'utf-16')
print(output.read())
output.close()
"""
