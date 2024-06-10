def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

Boo = False
values_list = [Boo, 45, [1, 5, 18]]
values_dict = {"a": 3, "b": 'Hello', "c": False}
values_list_2 = [1.234, "two"]

print_params(*values_list_2, 42)
print_params(**values_dict)
print_params(*values_list_2, values_dict)
