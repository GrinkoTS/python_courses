'''Задание 1.
Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт. (целое число).
Напишите программу, преобразующую данные из txt в csv'''

print('Ответ для задачи №1')
import csv

with open('prices.txt', encoding="utf-8") as f:
    data = []
    for line in f:
        data.append(line.rstrip('\n').split('\t'))

with open('prices.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for element in data:
        csv_writer.writerow(element)
print('_' * 100)

'''Задача 2. 
Имеется файл prices.csv с информацией о заказе из интернет магазина. 
В нем каждая строка содержит три колонки: наименование товара; количество товара 
(целое число); цена (в рублях) товара за 1 шт. (целое число). Напишите программу, 
подсчитывающую общую стоимость заказа.'''

print('Ответ для задачи №2', '\n')

with open('prices.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    prices = 0
    for row in csv_reader:
        prices = prices + (int(row[-1])*int(row[-2]))

print(f'Итоговая стоимость продуктов: {prices} рублей')
print('_' * 100)


'''Задача 3. Реализовать конвертер из csv в json формат:
[{column -> value}, ... , {column -> value}]
название столбца — значение (аналог DictReader из модуля csv).
Для csv формата принять
разделитель между значениями, по умолчанию ","
разделитель строк, по умолчанию "\n".
Встроенным модулем csv пользоваться нельзя, json можно.
В результате распечатать json строку с отступами равными 4.'''

print('Ответ для задачи №3', '\n')

import json

WORK_FILE = 'test.csv'

def csv_to_list_dict(filename: str, delimiter: str = ",") -> list[dict]:
    #открываем файл
    with open(filename) as f:
        #построчно считываем его, сразу убирая знак переноса
        csv_reader = f.readline()[:-1]
        #первую строчку преобразуем в список слов для заголовка
        csv_file = csv_reader.split(delimiter)
        print(csv_file)

        csv_tf = []
        for row in f:
            row = row[:-1]
            #остальные строчки преобразуем в список слов и соединяем с заголовками
            row_values = row.split(delimiter)
            csv_tf.append(dict(zip(csv_file, row_values)))

    return csv_tf

print(json.dumps(csv_to_list_dict(WORK_FILE), indent=4))

<<<<<<< HEAD

=======
>>>>>>> 1c3aca1 (Добавила файл с обработкой .xlsx файлов)
test_itog = csv_to_list_dict(WORK_FILE)

with open('test_string.json', 'w') as json_file:
    json.dump(test_itog, json_file)

print('_' * 100)

'''Задача 4. Создайте текстовый файл с абзацем текста (абсолютно любого, 
может быть стихотворение, текст любимой песни или письмо от начальника).
Код должен выдать статиску повторения слов в тексте - спискок различных 
слов и количество их повторения.'''

print('Ответ для задачи №4', '\n')

import collections
import os
# Здесь в функции get_words() производится начальная сегментация текста на слова.
# При этом все пунктуационные знаки удаляются, а переводы стоки заменяется на пробелы.
# Затем происходит разбитие текста на слова. В качестве разделителя по умолчанию применяется пробел.
#/Users/tamara/PycharmProjects/python_courses/tasks/Kukla_koldyna.txt

def get_words(filename):
    words =[]
    for line in filename:
        new_line = line.rstrip().split()
        for text in new_line:
            words.append(text.rstrip('''!()-[]{};?@#$%:'"\,./^&amp;*_'''))
    return words

# Далее в функции get_words_dict() получаем словарь из слов, где ключ -
# это уникальное слово, а значение - количество вхождений данного слова в тексте.
def get_words_dict(words):
    lower_list = []
    for word in words:
        word = word.lower()
        lower_list.append(word)
    second_list = collections.Counter(lower_list)
    return second_list

# Далее осуществляется ввод пути к файлу и вызов выше определенных функций,
# а также вывод всей статистики.
# Давайте еще с помощью модуля os проверим существует ли введенный файл (путь)

filename = input("Введите путь к файлу: ")

# Проверка существования файла или директории:
if os.path.exists(filename):
    print('File or directory exists')
    with open('Kukla_koldyna.txt', 'r') as sing:
        words1 = get_words(sing)
        first_list = collections.Counter(words1)
        print(f'Кол-во слов: {len(first_list.keys())}')
        words2 = get_words_dict(words1)
        print(f'Кол-во уникальных слов: {len(words2.items())}')
        spisok_slov = []
        for pair in words2.items():
            spisok_slov.append(f'{pair[0]} {pair[1]}')

        def comparator(item):
            return item[0]

        spisok_slov = sorted(spisok_slov, key=comparator)
        print('Все использованные слова:')
        print(*spisok_slov, sep='\n')
else:
    print('File or directory does not exist')









