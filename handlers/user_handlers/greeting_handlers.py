import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode
from loguru import logger

from database.database import get_user_data_from_db
from database.database import insert_user_data_to_database
from database.database import recording_data_of_users_who_launched_the_bot

from database.database import update_name_in_db
from database.database import update_phone_in_db

from keyboards.user_keyboards.user_keyboards import create_contact_keyboard
from keyboards.user_keyboards.user_keyboards import create_data_modification_keyboard
from keyboards.user_keyboards.user_keyboards import create_greeting_keyboard

from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"Пользователь {username} ({user_id}) запустил бота в {join_date}")
    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    greeting_keyboard = create_greeting_keyboard()
    data = (f"<i>{first_name} {last_name}, добро пожаловать в полезный чат-бот скидок и промокодов от "
            f"интернет-магазина «TWIN»</i>\n\n"
            
            f"Чем могу Вам помочь?")
    await bot.send_message(message.from_user.id, text=data, reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == "main_menu")
async def send_start(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

    # Получаем информацию о пользователе
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username
    first_name = callback_query.from_user.first_name
    last_name = callback_query.from_user.last_name
    join_date = datetime.datetime.now()
    logger.info(f"Пользователь {username} ({user_id}) вернулся в начальное меню в {join_date}")

    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    greeting_keyboard = create_greeting_keyboard()
    data = (f"<i>{first_name} {last_name}, добро пожаловать в полезный чат-бот скидок и промокодов от "
            f"интернет-магазина «TWIN»</i>\n\n"

            f"Чем могу Вам помочь?")
    await bot.send_message(callback_query.from_user.id, text=data, reply_markup=greeting_keyboard,
                           parse_mode=ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == "my_details")
async def call_us_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id  # Получаем ID текущего пользователя
    user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных

    # if user_data:
    # Если данные о пользователе найдены в базе данных, отобразите их
    name = user_data.get('name', 'не указано')
    surname = user_data.get('surname', 'не указано')
    phone_number = user_data.get('phone_number', 'не указано')
    # registration_date = user_data.get('registration_date')

    text_mes = (f"🤝 Добро пожаловать, {name} {surname}!\n"
                "Ваши данные:\n\n"
                f"✅ <b>Имя:</b> {name}\n"
                f"✅ <b>Номер телефона:</b> {phone_number}\n")
    edit_data_keyboard = create_data_modification_keyboard()
    await bot.send_message(callback_query.from_user.id, text_mes,
                           reply_markup=edit_data_keyboard,
                           parse_mode=ParseMode.HTML)
    # else:
    #     # Если данные о пользователе не найдены, предложите пройти регистрацию
    #     keyboards_sign_up = create_sign_up_keyboard()
    #     sign_up_text = ("👋 Предлагаем нам с Вами познакомиться!\n\n"
    #                     "Информация о Ваших Ф.И.О., городе и номере телефона нужны для оптимизации и персонализации "
    #                     "работы нашего бота под наших клиентов.\n\n"
    #                     "Для возврата нажмите /start")
    #     await bot.send_message(callback_query.from_user.id, sign_up_text,
    #                            reply_markup=keyboards_sign_up,
    #                            parse_mode=ParseMode.HTML,
    #                            disable_web_page_preview=True)


class MakingAnOrder(StatesGroup):
    """Создание класса состояний"""
    write_name = State()  # Имя
    phone_input = State()  # Передача номера телефона кнопкой


class ChangingData(StatesGroup):
    """Создание класса состояний, для смены данных пользователем"""
    changing_name = State()  # Имя
    changing_phone = State()  # Передача номера телефона кнопкой


@dp.callback_query_handler(lambda c: c.data == "edit_name")
async def edit_name_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новое имя:")
    await ChangingData.changing_name.set()


@dp.message_handler(state=ChangingData.changing_name)
async def process_entered_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_name = message.text
        if update_name_in_db(user_id, new_name):
            text_name = f"✅ Имя успешно изменено на {new_name} ✅\n\n"
            await bot.send_message(user_id, text_name)
            user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных
            name = user_data.get('name', 'не указано')
            surname = user_data.get('surname', 'не указано')
            phone_number = user_data.get('phone_number', 'не указано')
            text_mes = (f"🤝 Добро пожаловать, {name} {surname}!\n"
                        "Ваши данные:\n\n"
                        f"✅ <b>Имя:</b> {name}\n"
                        f"✅ <b>Номер телефона:</b> {phone_number}\n")
            data_modification_keyboard = create_data_modification_keyboard()
            await bot.send_message(user_id, text_mes,
                                   reply_markup=data_modification_keyboard,
                                   parse_mode=ParseMode.HTML)
        else:
            text_name = "❌ Произошла ошибка при изменении имени ❌\n\n" \
                        "Для возврата нажмите /start"
            await bot.send_message(user_id, text_name)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "edit_phone")
async def edit_city_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новый номер телефона:")
    await ChangingData.changing_phone.set()


@dp.message_handler(state=ChangingData.changing_phone)
async def process_entered_edit_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_phone = message.text
        if update_phone_in_db(user_id, new_phone):
            text_phone = f"✅ Номер телефона успешно изменен на {new_phone} ✅\n\n"
            await bot.send_message(user_id, text_phone)
            user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных
            name = user_data.get('name', 'не указано')
            surname = user_data.get('surname', 'не указано')
            phone_number = user_data.get('phone_number', 'не указано')
            text_mes = (f"🤝 Добро пожаловать, {name} {surname}!\n"
                        "Ваши данные:\n\n"
                        f"✅ <b>Имя:</b> {name}\n"
                        f"✅ <b>Номер телефона:</b> {phone_number}\n")
            data_modification_keyboard = create_data_modification_keyboard()
            await bot.send_message(user_id, text_mes,
                                   reply_markup=data_modification_keyboard,
                                   parse_mode=ParseMode.HTML)

        else:
            text_phone = "❌ Произошла ошибка при изменении номера телефона ❌\n\n" \
                         "Для возврата нажмите /start"
            await bot.send_message(user_id, text_phone)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "agree")
async def agree_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await MakingAnOrder.write_name.set()
    text_mes = ("👤 Введите ваше имя (желательно кириллицей):\n"
                "Пример: Иван, Ольга, Анастасия")
    await bot.send_message(callback_query.from_user.id, text_mes)


@dp.message_handler(state=MakingAnOrder.write_name)
async def write_name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    sign_up_texts = (
        "Для ввода номера телефона вы можете поделиться номером телефона, нажав на кнопку или ввести его вручную.\n\n"
        "Чтобы ввести номер вручную, просто отправьте его в текстовом поле.")
    contact_keyboard = create_contact_keyboard()
    await bot.send_message(message.from_user.id, sign_up_texts,
                           reply_markup=contact_keyboard,  # Set the custom keyboard
                           parse_mode=types.ParseMode.HTML,
                           disable_web_page_preview=True)
    await MakingAnOrder.phone_input.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=MakingAnOrder.phone_input)
async def handle_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


@dp.message_handler(lambda message: message.text and not message.contact, state=MakingAnOrder.phone_input)
async def handle_phone_text(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


async def handle_confirmation(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardRemove(selective=False)  # Remove the keyboard
    await message.answer("Спасибо за предоставленные данные.", reply_markup=markup)
    # Извлечение пользовательских данных из состояния
    user_data = await state.get_data()
    name = user_data.get('name', 'не указан')
    phone_number = user_data.get('phone_number', 'не указан')
    registration_date = datetime.datetime.now()
    # Получение ID аккаунта Telegram
    user_id = message.from_user.id
    # Составьте подтверждающее сообщение
    text_mes = (f"🤝 Рады познакомиться! 🤝\n"
                "Ваши регистрационные данные:\n\n"
                f"✅ <b>Ваше Имя:</b> {name}\n"
                f"✅ <b>Ваш номер телефона:</b> {phone_number}\n\n"
                "Вы можете изменить свои данные в меню \"Мои данные\".\n\n"
                "Для возврата нажмите /start")
    insert_user_data_to_database(user_id, name, phone_number, registration_date)
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
    data_modification_keyboard = create_data_modification_keyboard()
    await bot.send_message(message.from_user.id, text_mes, reply_markup=data_modification_keyboard)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
