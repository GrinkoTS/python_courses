import openpyxl
from docxtpl import DocxTemplate
from pprint import pprint
import re

# открываем исходный xlsx
wb = openpyxl.load_workbook(filename='people_data_vacation.xlsx')
# указываем рабочую вкладку из файла xlsx
sheet = wb['vacation']
# указываю путь к папке, куда сохранить шаблоны документов
folder_doc = '/Users/tamara/PycharmProjects/python_courses/Reg_exp/Lab_4/application/'
# шаблон doc документа
doc = DocxTemplate('Заявление на отпуск.docx')

# вытаскиваем искомые данные из экселя и забиваем в словарь
for num in range(2, 23):
    company = sheet['D' + str(num)].value
    name = sheet['B' + str(num)].value
    lastname = sheet['A' + str(num)].value

    start_date = sheet['F' + str(num)].value
    start_date = (str(start_date).split())
    start_date = start_date[0].split('-')
    start_date = start_date[-1] + '.' + start_date[-2] + '.' + start_date[0]

    finish_date = sheet['G' + str(num)].value
    finish_date = (str(finish_date).split())
    finish_date = finish_date[0].split('-')
    finish_date = finish_date[-1] + '.' + finish_date[-2] + '.' + finish_date[0]

    dict_name = {'company': company, 'name': name, 'lastname': lastname, 'start_date': start_date, 'finish_date':
        finish_date}
    # заносим данные из словаря в doc документ
    doc.render(dict_name)
    # сохраняем документы в нужной папке
    doc.save(folder_doc + (str(lastname) + '_final.docx'))

# создаю список неверно введенных email адресов
# создаю словарь bad_mail
bad_mail = {}
# прохожусь по всем строчкам файла
for i in range(2, 23):
    # задаю pattern с верным видом почты
    pattern = '[a-zA-Z][a-zA-Z0-9_.-]*@[a-z]*\.[a-z]+$'
    mail = sheet['E' + str(i)].value
    # если почта не подходит под стандартное значение
    if re.fullmatch(pattern, mail) == None:
        # заношу в словарь фамилию невнимательного сотрудника и его почту
        bad_mail[sheet['A' + str(i)].value] = mail
pprint(bad_mail)