#homework1
correct = 0
questions = {'2 * 2 = ': '4', '3,14 is integer or float? ': 'float', 'How many bytes use one symbol in UTF-16? ':'2', 'Which loop isn\'t for python: for, foreach or while? ': 'foreach',
                'Answer to the Ultimate Question of Life, The Universe, and Everything ':'42'}
for question in questions:
    answer = input(question)
    if answer.lower() == questions[question]:
        correct += 1
        print('Great! Correct answers:', correct)
    else:
        print('Wrong!')

print('Total correct answers:', correct)
