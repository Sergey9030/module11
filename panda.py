"""
Файл Data.txt
Первая стока является индексами столбцов
остальные строки это данные
"""

import pandas as pd

lines = []
column_index = []
with open('Data.txt', 'r', encoding='utf-8') as file:
    s = file.readline()  # Читаем первую строку (индексы)
    if len(s) > 0:
        column_index = s.split()
    s = file.readline()
    while len(s) > 0:  # Читаем данные построчно
        line = s.split()  # Разбиваем строку на подстроки
        for i in range(len(line)):
            line[i] = int(line[i])  # Меняем строковое значение на int
        lines.append(line)  # Добавляем строку целых чисел к массиву строк
        s = file.readline()
df = pd.DataFrame(lines, columns=column_index)  # Создаем объект DataFrame

print('Наша таблица', '='*30)
print(df)
print('Печать трех верхних рядов таблицы', '='*30)
print(df.head(3))
print('Печать трех нижних рядов таблицы', '='*30)
print(df.tail(3))
print('Печать индексов строк', '='*30)
print(df.index)
print('Печать индексов столбцов', '='*30)
print(df.columns)
print('Печать таблицы без индексов строк и столбцов', '='*30)
print(df.to_numpy())
print('Краткая статистическая сводка', '='*30)
print(df.describe())
print('Сортировка по индексу', '='*30)
print(df.sort_index(axis=1, ascending=False))
print('Сортировка по значениям столбца', '='*30)
print(df.sort_values(by='B',ascending=False))
print('Выводим столбец А', '='*30)
print(df['A'])
print('Выводим строки 1..3', '='*30)
print(df[1:3])
