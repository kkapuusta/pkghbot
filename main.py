import telebot,requests,bs4
from telebot import types
from bs4 import BeautifulSoup as BS
bot = telebot.TeleBot('6423617809:AAGJ6VhJSiafgqcesG2w55Iz5qxZo57V3BY')
global markup_group
@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup()
    markup1.add('Меню:')
    bot.send_message(message.chat.id,'Привет, я бот, который показывает расписание.',reply_markup= markup1)
    bot.register_next_step_handler(message, markup_for_start)
def markup_for_start(message):
    global markup_group
    global msg1
    markup_group = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Меню:':

        bm_btn = types.KeyboardButton('БМ')
        ip_btn = types.KeyboardButton('ИП')
        ir_btn = types.KeyboardButton('ИР')
        ol_btn = types.KeyboardButton('ОЛ')
        pd_btn = types.KeyboardButton('ПД')
        re_btn = types.KeyboardButton('РЭ')
        ra_btn = types.KeyboardButton('РА')
        ca_btn = types.KeyboardButton('СА')
        cr_btn = types.KeyboardButton('СР')
        to_btn = types.KeyboardButton('ТО')
        ts_btn = types.KeyboardButton('ТС')
        ud_btn = types.KeyboardButton('УД')
        yk_btn = types.KeyboardButton('УК')
        ee_btn = types.KeyboardButton('ЭЭ')
        ys_btn =types.KeyboardButton('ЮС')
        markup_group.row(bm_btn,ir_btn,ip_btn,ol_btn,pd_btn,re_btn,ra_btn,ca_btn)
        markup_group.row(cr_btn,to_btn,ts_btn,ud_btn,yk_btn,ee_btn,ys_btn)
        bot.send_message(message.chat.id, 'выбери свою группу',reply_markup=markup_group )
        bot.register_next_step_handler(message, markup_for_start2)
        if message.text == 'БМ':
            bot.register_next_step_handler(message, markup_for_start2)

def markup_for_start2(message):
    global markup_group
    global choice_group
    btn_to_back = types.KeyboardButton('Назад')
    choice_group = 'Выберите группу'
    if message.text == 'БМ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bm_23_6 = types.KeyboardButton('БМ 23-6')
            bm_22_6 = types.KeyboardButton('БМ 22-6')
            bm_21_6 = types.KeyboardButton('БМ 21-6')
            bm_20_6 = types.KeyboardButton('БМ 20-6')
            markup.add(bm_23_6,bm_22_6,bm_21_6,bm_20_6,btn_to_back, row_width=2)
            bot.send_message(message.chat.id,'Выберите группу',reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)


    if message.text == 'ИП':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ip_23_3 = types.KeyboardButton('ИП 23-3')
            ip_23_7k = types.KeyboardButton('ИП 23-7к')
            ip_22_3 = types.KeyboardButton('ИП 22-3')
            ip_22_7k = types.KeyboardButton('ИП 22-7к')
            ip_20_3 = types.KeyboardButton('ИП 20-3')
            ip_21_3 = types.KeyboardButton('ИП 21-3')
            ip_21_18k =types.KeyboardButton('ИП 21-18к')
            ip_20_7k = types.KeyboardButton('ИП 20-7к')
            ip_21_7k = types.KeyboardButton('ИП 21-7к')
            markup.add(ip_23_3,ip_23_7k, ip_22_3,ip_22_7k,ip_20_3,ip_21_3,ip_21_18k,ip_20_7k,ip_21_7k,btn_to_back, row_width=3)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'ИР':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ir_23_4 = types.KeyboardButton('ИР 23-4')
            ir_22_4 = types.KeyboardButton('ИР 22-4')
            ir_21_4 = types.KeyboardButton('ИР 21-4')
            ir_20_4 = types.KeyboardButton('ИР 20-4')
            markup.add(ir_23_4,ir_22_4,ir_21_4,ir_20_4,btn_to_back, row_width=2)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'ОЛ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ol_23_24k = types.KeyboardButton('ОЛ 23-24к')
            ol_22_24k = types.KeyboardButton('ОЛ 22-24к')
            markup.add(ol_23_24k,ol_22_24k,btn_to_back)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'ПД':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            pd_23_16 = types.KeyboardButton('ПД 23-16')
            pd_23_17 = types.KeyboardButton('ПД 23-17')
            pd_22_16 = types.KeyboardButton('ПД 22-16')
            pd_22_17 = types.KeyboardButton('ПД 22-17')
            pd_21_17 = types.KeyboardButton('ПД 21-17')
            pd_21_16 = types.KeyboardButton('ПД 21-16')
            pd_20_17 = types.KeyboardButton('ПД 20-17')
            pd_20_16 = types.KeyboardButton('ПД 20-16')
            markup.add(pd_23_16,pd_23_17,pd_22_16,pd_22_17,pd_21_16,pd_21_17,pd_20_16,pd_20_17,btn_to_back, row_width=4)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'РА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ra_22_5 = types.KeyboardButton('РА 22-5')
            ra_21_5 = types.KeyboardButton('РА 21-5')
            ra_20_5 = types.KeyboardButton('РА 20-5')
            markup.add(ra_22_5,ra_21_5,ra_20_5,btn_to_back, row_width=1)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'РЭ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            re_23_20 = types.KeyboardButton('РЭ 23-20')
            re_23_21 = types.KeyboardButton('РЭ 23-21')
            markup.add(re_23_20,re_23_21,btn_to_back,row_width=1)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'СА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ca_23_1 = types.KeyboardButton('СА 23-1')
            ca_23_2 = types.KeyboardButton('СА 23-2')
            ca_22_1 = types.KeyboardButton('СА 22-1')
            ca_22_2 = types.KeyboardButton('СА 22-2')
            ca_21_1 = types.KeyboardButton('СА 21-1')
            ca_21_2 = types.KeyboardButton('СА 21-2')
            ca_20_1 = types.KeyboardButton('СА 20-1')
            ca_20_2 = types.KeyboardButton('СА 20-2')
            markup.add(ca_23_1,ca_23_2,ca_22_2,ca_22_1,ca_21_1,ca_21_2,ca_20_2,ca_20_1,btn_to_back,row_width=4)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'СР':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cr_23_12 = types.KeyboardButton('СР 23-12')
            cr_22_12 = types.KeyboardButton('СР 22-12')
            cr_22_13 = types.KeyboardButton('СР 22-13')
            cr_21_12 = types.KeyboardButton('СР 21-12')
            cr_21_13 = types.KeyboardButton('СР 21-13')
            markup.add(cr_23_12,cr_22_13,cr_22_12,cr_21_13,cr_21_12,btn_to_back,row_width=3)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'ТО':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            to_23_8 = types.KeyboardButton('ТО 23-8')
            to_22_8 = types.KeyboardButton('ТО 22-8')
            to_22_9 = types.KeyboardButton('ТО 22-9')
            to_21_8 = types.KeyboardButton('ТО 21-8')
            to_21_9 = types.KeyboardButton('ТО 21-9')
            to_20_8 = types.KeyboardButton('ТО 20-8')
            to_20_9 = types.KeyboardButton('ТО 22-9')
            markup.add(to_23_8,to_22_8,to_22_9,to_21_8,to_21_9,to_20_9,to_20_8,btn_to_back, row_width=4)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'ТС':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ts_23_9 = types.KeyboardButton('ТC 23-9')
            markup.add(ts_23_9,btn_to_back)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'УД':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yd_23_11 = types.KeyboardButton('УД 23-11')
            yd_22_11 = types.KeyboardButton('УД 22-11')
            yd_21_11 = types.KeyboardButton('УД 21-11')
            yd_20_11 = types.KeyboardButton('УД 20-11')
            markup.add(yd_23_11,yd_22_11,yd_21_11,yd_20_11,btn_to_back,row_width=2)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

    if message.text == 'УК':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yk_23_10 = types.KeyboardButton('УК 23-10')
            yk_22_10 = types.KeyboardButton('УК 22-10')
            yk_21_10 = types.KeyboardButton('УК 21-10')
            yk_20_10 = types.KeyboardButton('УК 20-10')
            yk_20_11 = types.KeyboardButton('УК 20-11')
            markup.add(yk_23_10,yk_22_10,yk_21_10,yk_20_10,yk_20_11,btn_to_back, row_width=3)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)
    if message.text == 'ЭЭ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ee_23_23 = types.KeyboardButton('ЭЭ 23-23')
            ee_22_23 = types.KeyboardButton('ЭЭ 22-23')
            ee_21_23s = types.KeyboardButton('ЭЭ 21-23c')
            markup.add(ee_23_23,ee_22_23,ee_21_23s,btn_to_back,row_width=2)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)
    if message.text == 'ЮС':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ys_23_14 = types.KeyboardButton('ЮС 23-14')
            ys_23_15 = types.KeyboardButton('ЮС 23-15')
            ys_22_14 = types.KeyboardButton('ЮС 22-14')
            ys_22_15 = types.KeyboardButton('ЮС 22-15')
            ys_22_14k = types.KeyboardButton('ЮС 22-14k')
            ys_21_14 = types.KeyboardButton('ЮС 21-14')
            ys_21_15 = types.KeyboardButton('ЮС 21-15')
            markup.add(ys_23_15,ys_23_14,ys_22_14k,ys_22_14,ys_22_15,ys_21_15,ys_21_14,btn_to_back, row_width=4)
            bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
            bot.register_next_step_handler(message, markup_for_start3)

def markup_for_start3(message):
    if message.text == 'Назад':
        global markup_group
        global choice_group
        markup_group = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bm_btn = types.KeyboardButton('БМ')
        ip_btn = types.KeyboardButton('ИП')
        ir_btn = types.KeyboardButton('ИР')
        ol_btn = types.KeyboardButton('ОЛ')
        pd_btn = types.KeyboardButton('ПД')
        re_btn = types.KeyboardButton('РЭ')
        ra_btn = types.KeyboardButton('РА')
        ca_btn = types.KeyboardButton('СА')
        cr_btn = types.KeyboardButton('СР')
        to_btn = types.KeyboardButton('ТО')
        ts_btn = types.KeyboardButton('ТС')
        ud_btn = types.KeyboardButton('УД')
        yk_btn = types.KeyboardButton('УК')
        ee_btn = types.KeyboardButton('ЭЭ')
        ys_btn = types.KeyboardButton('ЮС')
        markup_group.row(bm_btn, ir_btn, ip_btn, ol_btn, pd_btn, re_btn, ra_btn, ca_btn)
        markup_group.row(cr_btn, to_btn, ts_btn, ud_btn, yk_btn, ee_btn, ys_btn)
        bot.send_message(message.chat.id,f'{choice_group}.',reply_markup=markup_group)
        bot.register_next_step_handler(message, markup_for_start2)
    if message.text == 'ПД 22-16':
        r = requests.get('https://pkgh.edu.ru/obuchenie/25.html')
        html = BS(r.content, 'lxml')
        page_all_font = html.find_all('font')

        for el in page_all_font:
            a = el.text
            if a == '1-я':
                continue
            if a == '2-я':
                continue
            if a == '3-я':
                continue
            if a == '4-я':
                continue
            if a == '5-я':
                continue
            if a == '6-я':
                continue
            if a == '7-я':
                continue
            if a == 'Время':
                continue

            if a == 'Пары':
                continue

            if a == (''
                     ''):
                continue
            b = ''.join(a)
            bot.send_message(message.chat.id, b)


bot.polling(none_stop=True)