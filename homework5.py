
immutable_var = (6, 564, 'Hide', 'Seek')
print(immutable_var)

# immutable_var[3] = 'Run'
# print(immutable_var)

# Попытка напрямую изменить данные кортежа - ошибка типизации, недопустимое действие для кортежа


# immutable_var[1] = '761'
# print(immutable_var)

# Нельзя изменить значение строки внутри кортежа напрямую
var = 1
mutable_list = (1, 999, (4 < var), [3, 6, 9])
print((mutable_list))
var = 7
mutable_list = (1, 999, (4 < var), [3, 6, 9])
print(mutable_list)

# Меняем значение переменной и логическое выражение внутри кортежа меняется в виду динамической типизации(как я понял)


mutable_list[3][1] = 7
print(mutable_list)

# Меняем значение внутри элемента кортежа - списка

mutable_list = (1, 999, (4 < var), [3, 6, 9])



