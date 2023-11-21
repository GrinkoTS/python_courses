import telebot
import config
import openpyxl



# импортируем токен
TOKEN = config.API_token
# создаем телеграмм-бота
bot = telebot.TeleBot(TOKEN)

# обрабатываем исходный xlsx файл:
# открываем исходный xlsx
wb = openpyxl.load_workbook(filename='people_data_vacation.xlsx')
# указываем рабочую вкладку из файла xlsx
sheet = wb['vacation']
final_dict = {}
# вытаскиваем искомые данные из экселя и забиваем в словарь
for num in range(2, 23):
    company = sheet['D' + str(num)].value
    name = sheet['B' + str(num)].value
    lastname = sheet['A' + str(num)].value
    job_title = sheet['C' + str(num)].value
    work_mail = sheet['E' + str(num)].value

    # заносим данные в словарь
    work_dict = {'name': name, 'company': company, 'job_title': job_title, 'work_mail': work_mail}
    final_dict[lastname] = work_dict


@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я могу помочь тебе найти информацию о конкретном сотруднике\n'
                          f'Просто введи фамилию/ должность/ почту сотрудника и я постараюсь тебе помочь')

@bot.message_handler(content_types = ['text'])
# проверяем информацию о сотруднике
def all_information(message):
    # создаю переменную counter == длине словаря == количеству сотрудников
    counter = len(final_dict)
    for lastname in final_dict:
        # если сотрудник не подходит => вычитаем из counter 1 и проходим цикл дальше
        counter -= 1
        # если есть совпадение => ввыводим данные о сотруднике и прерываем цикл
        if (message.text == lastname) or (message.text in final_dict[lastname].values()):
            bot.send_message(message.chat.id, f"{lastname} {final_dict[lastname]['name']}, {final_dict[lastname]['work_mail']}")
            break
    # если прошлись по циклу и не нашли ни одного совпадения => сотрудника нет в нашейй базе
    if counter == 0 :
        bot.send_message(message.chat.id, f'Такого сотрудника нет в базе\n'
                  f'Введи фамилию/ должность/ почту сотрудника и я постараюсь тебе помочь')

bot.polling()