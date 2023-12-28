from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from loguru import logger

from database.database import get_user_data_from_db_email
from database.database import recording_data_email
from keyboards.user_keyboards.user_keyboards import keyboard_to_fill_email_guide_25
from keyboards.user_keyboards.user_keyboards import main_menu_ke
from keyboards.user_keyboards.user_keyboards import main_menu_size_table
from keyboards.user_keyboards.user_keyboards import next_time_main_menu_ke
from system.dispatcher import bot, dp


class Email_guide_25(StatesGroup):
    email_guide_25 = State()


@dp.callback_query_handler(lambda c: c.data == "guide_25_ways_to_tie_your_shoelaces")
async def guide_25_ways_to_tie_your_shoelaces(callback_query: types.CallbackQuery, state: FSMContext):
    """Гайд 25 способов завязать шнурки"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        user_data = get_user_data_from_db_email(callback_query.from_user.id)
        if user_data:
            greeting_message = f'Полезный контент от TWIN!'
            logger.info('Грузим файл Гайд_TWIN.pdf')
            main_menu_key = main_menu_ke()
            with open('media/document/Гайд_TWIN.pdf', 'rb') as documents:
                await bot.send_document(callback_query.from_user.id,  # ID пользователя
                                        caption=greeting_message,  # Текст для приветствия 👋
                                        document=documents,
                                        reply_markup=main_menu_key,
                                        parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
        else:
            main_menu_key = keyboard_to_fill_email_guide_25()
            text_mes = ('Пожалуйста, укажите адрес электронной почты, на которую необходимо отправить гайд '
                        '«25 способов завязать шнурки».')
            await bot.send_message(callback_query.from_user.id, text_mes, reply_markup=main_menu_key)
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == 'next_time')
async def next_time(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        text_mes = ('Если у вас остались вопросы или вы хотели бы уточнить наличие определенных моделей вашего '
                    'размера, свяжитесь с нами через WhatsApp менеджера интернет-магазина:\n\n'
                    '👇\n'
                    'Задать вопрос (https://wa.me/79198438647)')
        main_menu_key = next_time_main_menu_ke()
        await bot.send_message(callback_query.from_user.id, text=text_mes, reply_markup=main_menu_key)
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == 'ill_in_email_guide_25')
async def ill_in_email(callback_query: types.CallbackQuery, state: FSMContext):
    """Заполнение email"""
    try:
        await state.reset_state()
        await Email_guide_25.email_guide_25.set()
        text_mes = "Введите ваш email. Например: twin@mail.ru."
        await bot.send_message(callback_query.from_user.id, text_mes)
    except Exception as error:
        logger.exception(error)


@dp.message_handler(state=Email_guide_25.email_guide_25)
async def write_email_handler(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(name=email)
    registration_date = message.date.strftime("%Y-%m-%d %H:%M:%S")
    recording_data_email(message.from_user.id, message.from_user.username, email, registration_date)
    greeting_message = f"Таблица размеров «TWIN»"
    main_menu_key = main_menu_size_table()
    with open('media/document/Гайд_TWIN.pdf', 'rb') as documents:
        await bot.send_document(message.from_user.id,  # ID пользователя
                                caption=greeting_message,  # Текст для приветствия 👋
                                document=documents,
                                reply_markup=main_menu_key,
                                parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки


def register_shoelaces_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(guide_25_ways_to_tie_your_shoelaces)
    dp.register_message_handler(next_time)
