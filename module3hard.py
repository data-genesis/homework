def calculate_structure_sum(data_structure):
    result = 0

    if isinstance(data_structure, (int, float)):
        result += data_structure
    elif isinstance(data_structure, str):
        result += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            result += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            result += calculate_structure_sum(key)
            result += calculate_structure_sum(value)

    return result

data = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data))








