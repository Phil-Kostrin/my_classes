
def calculate_structure_sum(item):
    global sum
    if isinstance(item, int):
        sum += item
    elif isinstance(item, str):
        sum += len(item)
    elif isinstance(item, (list, tuple, set)):
        for i in item:
            calculate_structure_sum(i)
    elif isinstance(item, dict):
        for key, value in item.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
    return sum

sum = 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  
