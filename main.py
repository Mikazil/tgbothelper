# Импортируем библиотеки
import requests
import lxml
import telebot
from bs4 import BeautifulSoup

# Подключаемся к боту
bott = '5396465139:AAFvTtWP2Hl7aiWI1snMQiEHJnmAHKY_ez0'
bot = telebot.TeleBot(bott)


# Выводим главное меню
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    #    bot.send_message(message.chat.id, "Здравствуйте, добро пожаловать в KemBot!", reply_markup=keyboard)

    keyboard.row("Гороскоп", "Курс валют")
    keyboard.add("Цены на бензин", "Новости")
    keyboard.add("Пробки", "Оставить отзыв")
    bot.send_message(message.chat.id, "Чего желаете?", reply_markup=keyboard)


# Проверяем, что выбрал пользователь
@bot.message_handler(content_types=['text'])
def choose(message):
    if message.text == "Гороскоп":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, "Гороскоп", reply_markup=keyboard)
        horo(msg)

    elif message.text == "Курс валют":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, "Курс Валют", reply_markup=keyboard)
        curr(msg)

    elif message.text == "Цены на бензин":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, "Цены на бензин", reply_markup=keyboard)
        fuel(msg)

    elif message.text == "Новости":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(len(news_pars())-1):

            bot.send_message(message.chat.id,news_pars()[i], reply_markup=keyboard)
        msg = bot.send_message(message.chat.id,news_pars()[len(news_pars())-1], reply_markup=keyboard)
        start(msg)

    elif message.text == "Пробки":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, "Пробки", reply_markup=keyboard)
        area(msg)

    elif message.text == "Оставить отзыв":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, "Отзыв", reply_markup=keyboard)
        form(msg)


# Создаем клаватуру гороскопа
def horo(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🦂Скорпион🦂", "🐏Овен🐏", "🐂Телец🐂")
    keyboard.add("👬Близнецы👬", "🦀Рак🦀", "🦁Лев🦁")
    keyboard.add("👧Дева👧", "⚖Весы⚖", "🏹Стрелец🏹")
    keyboard.add("🐐Козерог🐐", "🌊Водолей🌊", "🐟Рыбы🐟")
    a = bot.send_message(message.chat.id, "Выберите знак зодиака", reply_markup=keyboard)
    bot.register_next_step_handler(a, horocheck)


# Создаем клавиатуру выбора валюты
def curr(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Доллар $", "Евро €", "Биткоин ฿")
    keyboard.add("Эфир ⟠", "Тенге ₸", "Юань ¥")
    keyboard.add("Ethereum Classic ξ", "ZCash ⓩ", "Litecoin Ł")
    a = bot.send_message(message.chat.id, "Выберите валюту", reply_markup=keyboard)
    bot.register_next_step_handler(a, currcheck)


# Создаем клавиатуру выбора валюты
def fuel(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("ДТ", "АИ-92", "АИ-95", "АИ-98")
    a = bot.send_message(message.chat.id, "Выберите тип топлива", reply_markup=keyboard)
    bot.register_next_step_handler(a, fuelcheck)


# Создаем клавиатуру выбора района пробок
def area(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Заводский", "Центральный", "Ленинский")
    keyboard.add("Кировский", "Рудничный", "Лесная поляна")
    a = bot.send_message(message.chat.id, "Выберите район для показа пробок", reply_markup=keyboard)
    bot.register_next_step_handler(a, areacheck)

# Проверяем какой знак зодиака выбрал пользователь
@bot.message_handler(content_types=['text'])
def horocheck(message):
    if message.text == "🦂Скорпион🦂":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('scorpio'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🐏Овен🐏":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('aries'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🐂Телец🐂":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('taurus'), reply_markup=keyboard)
        start(msg)
    elif message.text == "👬Близнецы👬":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('gemini'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🦀Рак🦀":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('cancer'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🦁Лев🦁":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('leo'), reply_markup=keyboard)
        start(msg)
    elif message.text == "👧Дева👧":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('virgo'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🏹Стрелец🏹":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('sagittarius'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🐐Козерог🐐":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('capricorn'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🌊Водолей🌊":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('aquarius'), reply_markup=keyboard)
        start(msg)
    elif message.text == "🐟Рыбы🐟":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('pisces'), reply_markup=keyboard)
        start(msg)
    elif message.text == "⚖Весы⚖":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, horo_pars('libra'), reply_markup=keyboard)
        start(msg)


# Проверяем, какую валюту выбрал пользователь
@bot.message_handler(content_types=['text'])
def currcheck(message):
    if message.text == "Доллар $":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, curr_pars('USD') + "₽", reply_markup=keyboard)
        start(msg)
    elif message.text == "Евро €":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, curr_pars('EUR') + "₽", reply_markup=keyboard)
        start(msg)
    elif message.text == "Тенге ₸":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, curr_pars('KZT') + "₽ Цена за 100 ед.", reply_markup=keyboard)
        start(msg)
    elif message.text == "Юань ¥":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, curr_pars('CNY') + "₽ Цена за 10 ед.", reply_markup=keyboard)
        start(msg)
    elif message.text == "Биткоин ฿":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Ожидайте ~8 сек")
        msg = bot.send_message(message.chat.id, ccurr_pars('Bitcoin'), reply_markup=keyboard)
        start(msg)
    elif message.text == "Эфир ⟠":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Ожидайте ~8 сек")
        msg = bot.send_message(message.chat.id, ccurr_pars('Ethereum '), reply_markup=keyboard)
        start(msg)
    elif message.text == "Ethereum Classic ξ":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Ожидайте ~8 сек")
        msg = bot.send_message(message.chat.id, ccurr_pars('Ethereum Classic'), reply_markup=keyboard)
        start(msg)
    elif message.text == "ZCash ⓩ":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Ожидайте ~8 сек")
        msg = bot.send_message(message.chat.id, ccurr_pars('ZCash'), reply_markup=keyboard)
        start(msg)
    elif message.text == "Litecoin Ł":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Ожидайте ~8 сек")
        msg = bot.send_message(message.chat.id, ccurr_pars('Litecoin'), reply_markup=keyboard)
        start(msg)


@bot.message_handler(content_types=['text'])
def fuelcheck(message):
    if message.text == "ДТ":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, fuel_pars()[0], reply_markup=keyboard)
        start(msg)
    elif message.text == "АИ-92":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, fuel_pars()[1], reply_markup=keyboard)
        start(msg)
    elif message.text == "АИ-95":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, fuel_pars()[2], reply_markup=keyboard)
        start(msg)
    elif message.text == "АИ-98":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, fuel_pars()[3], reply_markup=keyboard)
        start(msg)


@bot.message_handler(content_types=['text'])
def areacheck(message):
    if message.text == "Центральный":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.108098,55.348506&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)
    elif message.text == "Заводский":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.041749,55.332925&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)
    elif message.text == "Ленинский":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.169010,55.341268&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)
    elif message.text == "Кировский":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.017412,55.400095&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)
    elif message.text == "Рудничный":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.116743,55.408508&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)
    elif message.text == "Лесная поляна":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         "https://static-maps.yandex.ru/1.x/?ll=86.232752,55.419335&spn=0.07,0.0&l=map,trf")
        msg = bot.send_message(message.chat.id, "Хорошей дороги!", reply_markup=keyboard)
        start(msg)


@bot.message_handler(content_types=['text'])
def form(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "https://forms.yandex.ru/u/6321ea93965c9217c3e91bba")
    msg = bot.send_message(message.chat.id, "Спасибо за проявление интереса к нашему боту!", reply_markup=keyboard)
    start(msg)


# Парсинг гороскопа с elle.ru
def horo_pars(x):
    url = f"https://www.elle.ru/astro/{x}/day/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    ht = soup.find_all("div", class_="articleParagraph articleParagraph_dropCap")
    for x in ht:
        print(x.get_text())
        return x.get_text()


# Парсинг валют c Центрального Банка России
def curr_pars(x):
    url = "https://cbr.ru/currency_base/daily/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    td = soup.find_all("td")
    element = 0

    for i in td:
        if i.text == f"{x}":
            c = element
            break
        element += 1

    return td[c + 3].text


# Парсинг Криптовалют с myfin.by
def ccurr_pars(x):
    url = "https://myfin.by/crypto-rates"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    sbl = soup.find_all("tbody", class_="table-body")
    ind = 0
    elm = 0
    for i in sbl:
        sbold = soup.find_all("a", class_="s-bold")
        for j in sbold:
            if j.text == x:
                elm = ind
            ind += 1
    td = soup.find_all("td")
    sum = td[6 * elm + 1].text
    sum = sum.split("$")

    return sum[0] + "$"


def fuel_pars():
    save = []
    url = f"https://fuelprices.ru/sibfo/kemerovo"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    ht = soup.find_all("div", class_="price")
    for x in ht:
        save.append(x.get_text())
    for i in range(len(save)):
        save[i] = save[i][1:6] + " ₽"
    return save

def news_pars():
    a = []
    url = f"https://lenta.ru/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    ht = soup.find_all("a", class_="card-mini _topnews")
    for x in ht:
       a.append(x["href"])

    for i in a:
        if i[:1] == "h":
            a.remove(i)
    for i in range(len(a)):
        a[i]="lenta.ru"+a[i]



    return a


bot.polling()