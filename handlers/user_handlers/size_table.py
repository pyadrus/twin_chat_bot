from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from loguru import logger

from database.database import recording_data_email, get_user_data_from_db_email
from keyboards.user_keyboards.user_keyboards import keyboard_to_fill_email_size_table
from keyboards.user_keyboards.user_keyboards import main_menu_size_table
from keyboards.user_keyboards.user_keyboards import next_time_main_menu_ke
from system.dispatcher import bot, dp


class Email(StatesGroup):
    email = State()


@dp.callback_query_handler(lambda c: c.data == "size_table")
async def size_table(callback_query: types.CallbackQuery, state: FSMContext):
    """Таблица размеров"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        user_data = get_user_data_from_db_email(callback_query.from_user.id)
        if user_data:
            greeting_message = f"Таблица размеров «TWIN»"
            main_menu_key = main_menu_size_table()
            with open('media/photos/size_table.jpg', 'rb') as photo_file:
                await bot.send_photo(callback_query.from_user.id,  # ID пользователя
                                     caption=greeting_message,  # Текст для приветствия 👋
                                     photo=photo_file,
                                     reply_markup=main_menu_key,
                                     parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
        else:
            main_menu_key = keyboard_to_fill_email_size_table()
            text_mes = 'Пожалуйста, укажите адрес электронной почты.'
            await bot.send_message(callback_query.from_user.id, text_mes, reply_markup=main_menu_key)
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == 'ill_in_email')
async def ill_in_email(callback_query: types.CallbackQuery, state: FSMContext):
    """Заполнение email"""
    try:
        await state.reset_state()
        await Email.email.set()
        text_mes = "Введите ваш email. Например: twin@mail.ru."
        await bot.send_message(callback_query.from_user.id, text_mes)
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == 'next_time_size_table')
async def next_time(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.reset_state()
        text_mes = ('Если у вас остались вопросы или вы хотели бы уточнить наличие определенных моделей вашего '
                    'размера, свяжитесь с нами через WhatsApp менеджера интернет-магазина:\n\n'
                    '👇\n'
                    'Задать вопрос (https://wa.me/79198438647)')
        main_menu_key = next_time_main_menu_ke()
        await bot.send_message(callback_query.from_user.id, text=text_mes, reply_markup=main_menu_key)
    except Exception as error:
        logger.exception(error)


@dp.message_handler(state=Email.email)
async def write_email_handler(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(name=email)
    registration_date = message.date.strftime("%Y-%m-%d %H:%M:%S")
    recording_data_email(message.from_user.id, message.from_user.username, email, registration_date)
    greeting_message = f"Таблица размеров «TWIN»"
    main_menu_key = main_menu_size_table()
    with open('media/photos/size_table.jpg', 'rb') as photo_file:
        await bot.send_photo(message.from_user.id,  # ID пользователя
                             caption=greeting_message,  # Текст для приветствия 👋
                             photo=photo_file,
                             reply_markup=main_menu_key,
                             parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки


def register_size_table_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(size_table)
    dp.register_message_handler(next_time)
