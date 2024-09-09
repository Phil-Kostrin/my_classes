my_dict = {'Phil': 1997, 'Danil': 1998, 'Kirill': 2000, 'Timur':1996}
print('Мой словарь:', my_dict)
print('Год рождения Фила:', my_dict['Phil'])
print('Год рожения Никиты:', my_dict.get('Nikita', 'Данные отсутсвуют'))
my_dict.update({'Masha': 1997, 'Nikolay': 1995})
a = my_dict.pop('Danil')
print('Удаленное значение:', a)
print('Обновленный словарь:', my_dict)

my_set = {1, 'Tree', True, 1, 3, 3, 2, True, 5, 'Tree'}
print('Моё множесто:', my_set)
my_set.add(6)
my_set.add(False)
my_set.remove(3)
print('Обновленное множество:', my_set)