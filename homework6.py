my_dict = {'Rihana': 45, 'Bob': 86, 'Gretta': 68}
print("Dict:", my_dict)
print("Existing weight:", my_dict['Bob'])
print("Not existing weight:",my_dict.get('Sara'))
my_dict.update({'Hooper': 92,'Chad': 78})
a = my_dict.pop('Rihana')
print("Deleted value:", a)
print("Updated dict:", my_dict)


my_set = {3, 6, 7, 3, 'Yes', 6, 3}
print("Set:", my_set)
my_set.add(566)
my_set.add(True)
my_set.discard(6)
print("Modified set:", my_set)
