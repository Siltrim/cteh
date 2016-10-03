__author__ = 'gia_sebua'

import re

class Pupil(object):
    def __init__(self, name, grade, mark):
        self.name = name
        self.grade = grade
        self.mark = mark

    def name_of_pupil(self):
        return self.name


commands = ['add', 'show', 'show all marks']

#inp = input('enter command: ')

string =  'add Vasya Petrov from 7A got 5 on russian lesson'
string1 = 'show Vasya Petrov from 7A marks'
string2 = 'show all marks'


result = re.findall(r'^\w*', string)
name = re.findall(r'[A-Z]\w+\s[A-Z]\w+', string)
grade = re.findall(r'[0-9][A-Z]', string)
mark = re.findall(r'[0-9]\s', string)
p = {'name': name, 'grade': grade}

student = Pupil(name, grade, mark)

print(result)
print(name)
print(grade)
print(mark)

print(student.name_of_pupil())
