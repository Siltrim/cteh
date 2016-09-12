#homework1.2
import sys

__author__ = 'gia_sebua'

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

separator = ';' #separator between question and answer in file with questions
correct = 0
questions = open('questions.txt','r')
results = open('results.txt','a')
name = input_function('Hi, what\'s your name? ')

for line in questions:
    line = line.split(separator)
    answer = input_function(line[0].strip())
    if answer == line[1].strip():
        correct += 1
        print('hell yeah! Correct answers:', correct)
    else:
        print('wrong answer')

print('{} you have {} correct answers'.format(name, correct))
output = name + ' ' + str(correct)+'\r\n'
results.write(output)
results.close()
questions.close()
