from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def keyboard_to_fill_email_size_table():
    """
    Клавиатура заполнения email
    'Заполнить email' - ill_in_email
    'В другой раз' - next_time
    '↩️ Главное меню' - main_menu
    """
    main_menu_key = InlineKeyboardMarkup()
    fill_in_email_button = InlineKeyboardButton(text='Заполнить email', callback_data='ill_in_email')
    next_time_button = InlineKeyboardButton(text='В другой раз', callback_data='next_time_size_table')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    main_menu_key.add(fill_in_email_button, next_time_button)
    main_menu_key.add(main_menu_button)

    return main_menu_key


def keyboard_to_fill_email_guide_25():
    """
    Клавиатура заполнения email
    'Заполнить email' - ill_in_email
    'В другой раз' - next_time
    '↩️ Главное меню' - main_menu
    """
    main_menu_key = InlineKeyboardMarkup()
    fill_in_email_button = InlineKeyboardButton(text='Заполнить email', callback_data='ill_in_email')
    next_time_button = InlineKeyboardButton(text='В другой раз', callback_data='next_time')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    main_menu_key.add(fill_in_email_button, next_time_button)
    main_menu_key.add(main_menu_button)

    return main_menu_key


def next_time_main_menu_ke():
    """Кнопка возврата в главное меню"""
    main_menu_key = InlineKeyboardMarkup()
    fill_in_email_button = InlineKeyboardButton(text='Заполнить email', callback_data='ill_in_email_guide_25')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')

    main_menu_key.add(fill_in_email_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_ke():
    """Кнопка возврата в главное меню"""
    main_menu_key = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')

    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_size_table():
    """
    Кнопка возврата в главное меню
    '↩️ Главное меню' - main_menu
    'Наши магазины' - our_stores
    'Оператор' - operator
    """
    main_menu_key = InlineKeyboardMarkup()

    operator_button = InlineKeyboardButton(text='Оператор',
                                           callback_data="operator")
    our_stores_button = InlineKeyboardButton(text='Наши магазины',
                                             callback_data='our_stores')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    main_menu_key.add(operator_button, our_stores_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_key_avito():
    """Кнопка возврата в главное меню
    '↩️ Главное меню' - main_menu
    'Avito' - http://avito.ru/brands/twin
    """
    main_menu_key = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    avito_button = InlineKeyboardButton(text='Avito', url='http://avito.ru/brands/twin')
    main_menu_key.add(avito_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_key_perfumery():
    """Кнопка возврата в главное меню
    '↩️ Главное меню' - main_menu
    'Перейти на сайт' - https://twin-perfume.ru/
    """
    main_menu_key = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    avito_button = InlineKeyboardButton(text='Перейти на сайт', url='https://twin-perfume.ru/')
    main_menu_key.add(avito_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_key_sneakers():
    """Кнопка возврата в главное меню
    '↩️ Главное меню' - main_menu
    'Перейти на сайт' - https://twin-shoes.ru/
    """
    main_menu_key = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    avito_button = InlineKeyboardButton(text='Перейти на сайт', url='https://twin-shoes.ru/')
    main_menu_key.add(avito_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def main_menu_key_kids_toys():
    """Кнопка возврата в главное меню
    '↩️ Главное меню' - main_menu
    'Перейти на сайт' - https://twin-toys.ru/
    """
    main_menu_key = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    avito_button = InlineKeyboardButton(text='Перейти на сайт', url='https://twin-toys.ru/')
    main_menu_key.add(avito_button)
    main_menu_key.add(main_menu_button)
    return main_menu_key


def create_greeting_keyboard():
    """
    Создаем клавиатуру для приветственного сообщения 👋
    """
    greeting_keyboard = InlineKeyboardMarkup()
    discount_on_first_order_button = InlineKeyboardButton(text='Скидка на первый заказ',
                                                          callback_data='discount_on_first_order')
    our_stores_button = InlineKeyboardButton(text='Наши магазины',
                                             callback_data='our_stores')
    operator_button = InlineKeyboardButton(text='Оператор',
                                           callback_data="operator")
    size_table_button = InlineKeyboardButton(text='Таблица размеров ',
                                             callback_data="size_table")
    guide_25_ways_to_tie_your_shoelaces_button = InlineKeyboardButton(text='Гайд «25 способов завязать шнурки»',
                                                                      callback_data='guide_25_ways_to_tie_your_shoelaces')

    greeting_keyboard.row(discount_on_first_order_button)  # Услуги и цены
    greeting_keyboard.row(our_stores_button, operator_button)  # Самовыкуп
    greeting_keyboard.row(size_table_button)  # Отзывы
    greeting_keyboard.row(guide_25_ways_to_tie_your_shoelaces_button)  # Отзывы

    return greeting_keyboard


def create_main_menu_keyboard():
    """
    Создает клавиатуру для кнопки 'Главное меню'
    'Да, хочу промокод' - agree
    'Нет, в другой раз' - disagree
    '↩️ Главное меню' - main_menu
    """
    main_menu_keyboard = InlineKeyboardMarkup()
    agree_button = InlineKeyboardButton(text='Да, хочу промокод', callback_data='agree')
    disagree_button = InlineKeyboardButton(text='Нет, в другой раз', callback_data='disagree')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    main_menu_keyboard.row(agree_button, disagree_button)
    main_menu_keyboard.row(main_menu_button)
    return main_menu_keyboard


def create_contact_keyboard():
    """Создает клавиатуру для отправки контакта"""
    contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    send_contact_button = KeyboardButton("📱 Отправить", request_contact=True)

    contact_keyboard.add(send_contact_button)
    return contact_keyboard


def create_data_modification_keyboard():
    """Создает клавиатуру для изменения данных"""
    data_modification_keyboard = InlineKeyboardMarkup()
    edit_name_button = InlineKeyboardButton("✏️Изменить Имя", callback_data="edit_name")
    edit_phone_button = InlineKeyboardButton("✏️Изменить Номер 📱 ", callback_data="edit_phone")
    continue_button = InlineKeyboardButton("Продолжить", callback_data="continue")

    data_modification_keyboard.row(edit_name_button, edit_phone_button)
    data_modification_keyboard.row(continue_button)
    return data_modification_keyboard


def continue_keyboard():
    """Клавиатура Продолжить"""
    continue_key = InlineKeyboardMarkup()
    TWIN_on_Avito_bt = InlineKeyboardButton("TWIN на Avito", callback_data="TWIN_on_Avito")
    Perfumery_bt = InlineKeyboardButton("Парфюмерия", callback_data="Perfumery")
    Sneakers_bt = InlineKeyboardButton("Кроссовки", callback_data="Sneakers")
    Kids_toys_bt = InlineKeyboardButton("Детские игрушки", callback_data="Kids_toys")

    continue_key.row(TWIN_on_Avito_bt, Sneakers_bt)
    continue_key.row(Perfumery_bt, Kids_toys_bt)

    return continue_key


if __name__ == '__main__':
    create_main_menu_keyboard()
    create_contact_keyboard()
    create_data_modification_keyboard()
    create_greeting_keyboard()
