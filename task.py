# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random
def Task1():
    print('1. Определите группу с наилучшим средним баллом:\n')
    rows = 7
    columns = random.randint(20,30)
    numbers = [0] * rows
    count = 0
    scores = 0
    answer = 1
    the_best_group_scores = 0
    the_best_group_number = 0

    for i in range(len(numbers)):
        columns =  random.randint(20,30)
        numbers[i] = list(0 for _ in range(columns))
        for j in range(columns):
            numbers[i][j] = random.randint(2,5)
            count += numbers[i][j]
        scores = count / columns

        if the_best_group_scores < scores:
            the_best_group_scores = scores
            the_best_group_number = answer
        print(f'Средний балл группы {answer}:')    
        print(round(scores,2))
        count = 0
        answer += 1

    print('\nОбщая таблица групп:')
    for row in numbers:
        print(row)

    print(f'\nЛучшая группа № {the_best_group_number} со средним баллом {round(the_best_group_scores,2)}. \n')

Task1()


#  Задача 2.Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
def Task2():
    print('2. Cумма элементов каких строк превосходит сумму главной диагонали матрицы?\n')
    rows = columns = 5
    sum_of_diagonal = 0
    count = 0
    numbers = [0] * rows 
    answer = 1

    for i in range(len(numbers)):
        numbers[i] = list(0 for _ in range(columns))

    for i in range(rows):
        for j in range(columns):
            numbers[i][j] = random.randint(0,30)
            if i == j:
                sum_of_diagonal += numbers[i][j]
            
    print("Kвадратная матрица, заполненная случайными числами: ")
    for row in numbers:
        print(row)

    print(f'\nСуммa главной диагонали: {sum_of_diagonal}.')  

    for i in range(rows):
        for j in range(columns):
            count += numbers[i][j]
        if count > sum_of_diagonal:
            print(f'Сумма элементов {answer} строки: {count} - больше суммы диагонали.')
        count = 0
        answer += 1

Task2()    

#Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
from datetime import datetime, timedelta

def Task3():
    print('\n3. Определите самый жаркий и самый холодный 7-дневный промежуток периода: ')
    temperature = [0] * 5
    value = []
    value_sum = 0
    weekly_maximum = 0
    weekly_minimum = 1000
    may = 0
    june = 1
    jule = 2
    august = 3
    september = 4
    temperature[may] = list(random.randint(6, 18) for i in range(31))
    temperature[june] = list(random.randint(11, 23) for i in range(30))
    temperature[jule] = list(random.randint(14, 24) for i in range(31))
    temperature[august] = list(random.randint(11, 21) for i in range(31))
    temperature[september] = list(random.randint(6, 15) for i in range(30))
    for row in temperature:
        print(row)
    for i in range(len(temperature)):
        for j in range(len(temperature[i])):
            value.append(temperature[i][j])
    for i in range(len(value) - 6):
        value_sum = 0
        value_sum = value[i] + value[i+1] + value[i+2] + value[i+3] + value[i+4] + value[i+5] + value[i+6]
        if value_sum > weekly_maximum:
            weekly_maximum = i
        elif value_sum < weekly_minimum:
            weekly_minimum = i
    start_data = '2022-05-01' 
    dt = datetime.strptime(start_data, '%Y-%m-%d')
    result_start_max_day = (dt + timedelta(days=weekly_maximum)).strftime('%Y-%m-%d')
    result_finish_max_day = (dt + timedelta(days=weekly_maximum+7)).strftime('%Y-%m-%d')
    result_start_min_day = (dt + timedelta(days=weekly_minimum)).strftime('%Y-%m-%d')
    result_finish_min_day = (dt + timedelta(days=weekly_minimum+7)).strftime('%Y-%m-%d')
    print(f'\nСамая теплая неделя начивается с {result_start_max_day} по {result_finish_max_day}.')
    print(f'Самая холодная неделя начивается с {result_start_min_day} по {result_finish_min_day}.')

Task3()