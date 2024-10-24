# 1-й пункт
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2-й пункт
values_list = [False, 'Apple', 52]
values_dict = {'a':927, 'b':True, 'c':'Бигль'}
print_params(*values_list)
print_params(**values_dict)

# 3-й пункт
values_list_2 = ['Urban', 24.1]
print_params(*values_list_2, 42)
