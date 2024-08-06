first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zipped = zip(first, second)

first_result = [len(f) - len(s) for f, s in zipped if len(f) != len(s)]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]


print(list(first_result))
print(list(second_result))