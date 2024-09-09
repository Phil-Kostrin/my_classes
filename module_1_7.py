# Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Переводим множество students в список и упорядочиваем имена в алфавитном порядке
students = sorted(list(students))
# Для наглядности посчитаем средний балл для каждого ученика
# x_A = sum(grades[0])/len(grades[0])
# x_B = sum(grades[1])/len(grades[1])
# x_J = sum(grades[2])/len(grades[2])
# x_K = sum(grades[3])/len(grades[3])
# x_S = sum(grades[4])/len(grades[4])
# Составим список из средних баллов (в задании не указано можно ли сразу подставить в словарь присвоенные выше переменные "x_A, x_B и т.д.",
# поэтому мною было принято решение составить из них список)
average_score = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
# С помощью функции dict составляем словарь с помощью извлечения соответсвующих элементов из списков students и average_score.
X = dict([(students[0], average_score[0]), (students[1], average_score[1]), (students[2], average_score[2]), (students[3], average_score[3]), (students[4], average_score[4])])
print('Средний балл учеников:', X)
