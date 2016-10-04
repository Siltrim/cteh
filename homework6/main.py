__author__ = 'gia_sebua'



import re
import pickle

PIK = 'pickle.dat'

string = 'add Vasya Petrov from 7A got 5 on english'
string1 = 'add Dima Ivanov from 4A got 2 on english'

action = re.findall(r'^\w+', string)
name = re.findall(r'[A-Z]\w+\s[A-Z]\w+', string)
grade = re.findall(r'[0-9][A-Z]', string)
mark = re.findall(r'[0-9]\s', string)

data = [name, grade, mark]

with open(PIK, 'wb') as f:
    pickle.dump(data, f)
print('-----------')
name = re.findall(r'[A-Z]\w+\s[A-Z]\w+', string1)
grade = re.findall(r'[0-9][A-Z]', string1)
mark = re.findall(r'[0-9]\s', string1)
print(data)

data = [name, grade, mark]

with open(PIK, 'wb') as f:
    pickle.dump(data, f)

data2=[]
with open(PIK, 'rb') as f:
    for _ in range(len(pickle.load(f))):
        data2.append(pickle.load(f))


print(data2)



