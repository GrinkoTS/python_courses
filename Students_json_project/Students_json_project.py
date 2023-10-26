import json
import csv

#считываю данные из файла student_list.json и преобразуйте в словарь students
f = open('student_list.json')
students = json.load(f)

'''Задание1: Средний балл по всем предметам'''
#создаю функцию, которая возвращает словарь со средним балом всех студентов
def average_score(names:dict) -> dict:
    #создаю вспомогательный словарь
    average_score = {}
    #прохожусь по всем студентам из нашего списка
    for name in names.keys():
        #создаю переменную для подсчета среднего бала
        count = 0
        #прохожусь по списку предметов
        for subj in names[name]["subjects"]:
            #ищу общий балл для каждого студента
            count += names[name]["grades"][subj]
            #записываю в словарь студент:его средний балл
            average_score[name] = count / len(names[name]["subjects"])
    return average_score
#создаю функцию, для подсчета и вывода информации по среднему баллу для каждого студента
def get_average_score(names:dict):
    all_students = average_score(names)
    for student in all_students.keys():
        print(f'Средний балл для студента {student}: {all_students[student]}')

get_average_score(students)
print('_' * 100)

'''Задание2: Наилучший и худший студент'''
#функция для нахождения лучшего студента
def get_best_student(names:dict):
    #all_students - словарь -> студент:средний балл
    all_students = average_score(names)
    #создаю функцию-объект -> возвразает последний элемент кортежа
    def best_score(para):
        return para[-1]
    #сортирую словарь по ключу - средний балл по убыванию
    all_pair = sorted(list(all_students.items()), key=best_score, reverse=True )
    return f'Наилучший студент: {(all_pair)[0][0]} (Средний балл: {(all_pair)[0][1]})'

#функция для нахождения худшего студента
def get_worst_student(names:dict):
    # all_students - словарь -> студент:средний балл
    all_students = average_score(names)
    # создаю функцию-объект -> возвразает последний элемент кортежа
    def worst_score(para):
        return para[-1]
    # сортирую словарь по ключу - средний балл по возрастанию
    all_pair = sorted(list(all_students.items()), key=worst_score)
    return f'Худший студент: {(all_pair)[0][0]} (Средний балл: {(all_pair)[0][1]})'

print(get_best_student(students))
print(get_worst_student(students))
print('_' * 100)

'''Задание3: Поиск по имени'''

def find_student(name):
    #если студента нет в искомом файле
    if name not in students.keys():
        print('Студент с таким именем не найден')
    #если есть, выводим инормацию о нем из словаря по ключам
    else:
        print(f'Имя: {name}')
        #проходимся по кортежу данных нашего студента и выводим данные о нем
        for elem in students[name].items():
            if elem[0] == 'age':
                print(f'Возраст: {elem[1]}')
            if elem[0] == 'subjects':
                print(f'Предметы: {elem[1]}')
            if elem[0] == 'grades':
                print(f'Оценки: {elem[1]}')

find_student('Olivia')
print('_' * 100)

'''Задание4: Сортировка студентов'''
# all_students - словарь -> студент:средний балл
all_students = average_score(students)
# создаю функцию-объект -> возвразает последний элемент кортежа
def para(para):
    return para[-1]
# сортирую словарь по ключу - средний балл по убыванию
all_pair_students = sorted(list(all_students.items()), key=para, reverse=True)
print('Сортировка студентов по среднему баллу:')
# выводим данные о каждом студенте на печать
for people in all_pair_students:
    print(f'{people[0]}: {people[1]}')

'''Задание5. Преобразуйте словарь в список словарей данного формата'''

# делаю полную копию словаря -> для изменения первоначального
students_reserve = students.copy()
# создаю список студентов
students = []
# прохожусь по всем студентам
for name in students_reserve.keys():
    # делаю вспомогательный словарь для записи данных о каждом студенте
    vspom_dict = {}
    # записываю в него имя
    vspom_dict['name'] = name
    # добавляю все остальные записи о нем из изначального файла
    vspom_dict.update(students_reserve[name])
    # добавляю данные в новый список
    students.append(vspom_dict)

print(*students, sep='\n')
print('_' * 100)

'''Задание 6. Сформируйте csv'''
#создаю список для записи информации
data_csv = []
#создаю заголовок таблицы
first_data = ['name','age', 'grade']
#добавляю в итоговый список первую строчку - заголовок таблицы
data_csv.append(first_data)
#прохожусь по всем студентам из словаря со среднем балом
for student in all_students.keys():
    #находим имя студента
    name_vs = student
    #из первого словаря вытаскиваем его возраст
    age_vs = str(students_reserve[student]['age'])
    #находим средний балл искомого студента
    grade_vs = str(all_students[student])
    #добавляем в наш список запись по каждому студенту в нужном формате
    data_csv.append([name_vs, age_vs, grade_vs])

# Открываем CSV файл для записи
with open('all_students.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Записываем строки в CSV файл
    for row in data_csv:
        csv_writer.writerow(row)

