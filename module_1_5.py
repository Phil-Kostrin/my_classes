immutable_var = 27, False, 'Аквариум', 15.3
print(immutable_var)
# immutable_var[0] = 'Urban'
# print(immutable_var)
# Изменение значения переменных кортежа невозможно, т.к. кортеж не поддерживает обращение к переменным,
# но если значение переменной в кортеже записано в виде списка, то мы можем заменять значения переменных в этом списке.
mutable_list = [66, 'Fish', True, 12532, 864.2, 'Море']
print(mutable_list)
mutable_list[1] = 'Fisherman'
print(mutable_list)
mutable_list[5] = 'Sun'
print(mutable_list)
mutable_list[3] = 'Число'
print(mutable_list)
