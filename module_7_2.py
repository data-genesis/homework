import io
from pprint import pprint

file = "file_name.txt"

def custom_write(file_name, string):
    with open(file_name, "wсра") as a:
        result_dict = {}
        num_of_string = 1
        for text in string:
            pos = a.tell()
            result_dict[(num_of_string, pos)] = text
            a.write(f"{text}\n")
            num_of_string += 1
    return result_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', info)
for elem in result.items():
    print(elem)